/**
 * Parte de incidencia — Netlify Function
 * ======================================
 * GET  /api/salud        → comprueba que la función está viva y configurada
 * POST /api/incidencias  → recibe el parte y envía el correo con las fotos
 *
 * Variables de entorno (Netlify → Site settings → Environment variables):
 *   SMTP_HOST       smtp.gmail.com
 *   SMTP_PORT       587
 *   SMTP_USER       eperezgamarro@gmail.com
 *   SMTP_PASS       contraseña de aplicación de Gmail (16 caracteres)
 *   DESTINATARIOS   tmh_moldtrans@moldtrans.com
 *   ARCHIVO_BCC     (opcional) copia oculta para guardar histórico
 *   MODO_PRUEBA     1 mientras se hacen pruebas, 0 en producción
 */

import nodemailer from "nodemailer";

const env = (k, def = "") => process.env[k] || def;

const SMTP_HOST = env("SMTP_HOST", "smtp.gmail.com");
const SMTP_PORT = Number(env("SMTP_PORT", "587"));
const SMTP_USER = env("SMTP_USER");
const SMTP_PASS = env("SMTP_PASS");
const DESTINATARIOS = env("DESTINATARIOS", "tmh_moldtrans@moldtrans.com")
  .split(",").map(s => s.trim()).filter(Boolean);
const ARCHIVO_BCC = env("ARCHIVO_BCC");
const MODO_PRUEBA = env("MODO_PRUEBA", "1") === "1";

const MAX_FOTOS = 5;
const OBLIGATORIOS = ["referencia", "operario", "expedicion", "tipo", "ubicacion", "reserva"];

/* ── Utilidades ───────────────────────────────────────────── */
const limpio = (t, n = 600) => String(t ?? "").trim().slice(0, n);

const escapar = t => limpio(t)
  .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
  .replace(/\n/g, "<br>");

function decodificarFoto(dataUrl) {
  const m = /^data:image\/(jpeg|jpg|png);base64,(.+)$/i.exec(dataUrl || "");
  if (!m) return null;
  try {
    return { contenido: Buffer.from(m[2], "base64"), ext: m[1] === "png" ? "png" : "jpg" };
  } catch {
    return null;
  }
}

/* ── Plantilla del correo ─────────────────────────────────── */
function cuerpoHtml(d, nFotos) {
  const fila = (k, v) => `<tr>
    <td style="padding:9px 14px;background:#EFE9DC;border-bottom:1px solid #D6CDBA;
        font:600 12px/1.4 Arial,sans-serif;letter-spacing:.06em;text-transform:uppercase;
        color:#5A6468;white-space:nowrap;">${k}</td>
    <td style="padding:9px 14px;border-bottom:1px solid #D6CDBA;
        font:14px/1.5 Arial,sans-serif;color:#141A1C;">${v}</td></tr>`;

  const filas = [
    ["Operario", escapar(d.operario)],
    ["Expedición", `<b>${escapar(d.expedicion)}</b>`],
    ["Tipo", `[${escapar(d.codigo_tipo)}] ${escapar(d.tipo)}`],
    ["Ubicación", escapar(d.ubicacion) +
      (d.ubicacion_nfc ? ' <span style="color:#8A6A16;">(leída por NFC)</span>' : "")],
  ];
  if (limpio(d.detalle)) filas.push(["Posición", escapar(d.detalle)]);
  filas.push(["Reserva", escapar(d.reserva)]);
  if (limpio(d.observaciones)) filas.push(["Observaciones", escapar(d.observaciones)]);
  filas.push(["Fotos", `${nFotos} adjunta${nFotos === 1 ? "" : "s"}`]);

  const momento = new Date().toLocaleString("es-ES", {
    timeZone: "Europe/Madrid", dateStyle: "short", timeStyle: "short",
  });

  return `<!DOCTYPE html><html><body style="margin:0;padding:26px 12px;background:#16262C;">
<table role="presentation" width="100%" style="max-width:600px;margin:0 auto;border-collapse:collapse;">
  <tr><td style="height:6px;background:#F0A81C;"></td></tr>
  <tr><td style="background:#16262C;padding:22px 14px 24px;">
    <div style="font:400 11px/1 Arial,sans-serif;letter-spacing:.22em;text-transform:uppercase;
                color:#7E96A0;">Moldtrans · Almacén Montornès</div>
    <div style="font:700 30px/1 Arial,sans-serif;text-transform:uppercase;color:#EFE9DC;
                margin-top:9px;">Parte de incidencia</div>
    <div style="font:600 15px/1 Arial,sans-serif;color:#F0A81C;margin-top:12px;">
      ${escapar(d.referencia)} &nbsp;·&nbsp; ${momento}</div>
  </td></tr>
  <tr><td><table role="presentation" width="100%" style="border-collapse:collapse;background:#F7F3EA;">
    ${filas.map(([k, v]) => fila(k, v)).join("")}
  </table></td></tr>
  <tr><td style="background:#EFE9DC;padding:14px;font:11px/1.5 Arial,sans-serif;color:#5A6468;">
    Parte generado desde una etiqueta NFC del almacén. Las fotos van adjuntas a este correo.
  </td></tr>
</table></body></html>`;
}

/* ── Handler ──────────────────────────────────────────────── */
export default async (req) => {
  const json = (obj, status = 200) =>
    new Response(JSON.stringify(obj), {
      status, headers: { "Content-Type": "application/json" },
    });

  if (req.method === "GET") {
    return json({
      ok: true,
      configurado: Boolean(SMTP_USER && SMTP_PASS && DESTINATARIOS.length),
      destinatarios: DESTINATARIOS.length,
      modo_prueba: MODO_PRUEBA,
    });
  }

  if (req.method !== "POST") return json({ error: "Método no admitido" }, 405);

  let d;
  try {
    d = await req.json();
  } catch {
    return json({ error: "El parte llegó ilegible" }, 400);
  }

  const faltan = OBLIGATORIOS.filter(c => !limpio(d[c]));
  if (faltan.length) return json({ error: `Faltan campos: ${faltan.join(", ")}` }, 400);

  const fotos = (d.fotos || []).slice(0, MAX_FOTOS).map(decodificarFoto).filter(Boolean);
  if (!fotos.length) return json({ error: "El parte necesita al menos una foto legible" }, 400);

  if (!SMTP_USER || !SMTP_PASS) {
    return json({ error: "El servidor no tiene configurado el correo (SMTP_USER / SMTP_PASS)" }, 500);
  }

  const transporte = nodemailer.createTransport({
    host: SMTP_HOST,
    port: SMTP_PORT,
    secure: SMTP_PORT === 465,
    auth: { user: SMTP_USER, pass: SMTP_PASS },
  });

  const prefijo = MODO_PRUEBA ? "[PRUEBA] " : "";
  const texto = [
    `PARTE DE INCIDENCIA ${d.referencia}`,
    `Operario:      ${d.operario}`,
    `Expedición:    ${d.expedicion}`,
    `Tipo:          ${d.tipo}`,
    `Ubicación:     ${d.ubicacion}`,
    `Posición:      ${d.detalle || "-"}`,
    `Reserva:       ${d.reserva}`,
    `Observaciones: ${d.observaciones || "-"}`,
    `Fotos:         ${fotos.length}`,
  ].join("\n");

  try {
    await transporte.sendMail({
      from: `"Incidencias Montornès" <${SMTP_USER}>`,
      to: DESTINATARIOS.join(", "),
      bcc: ARCHIVO_BCC || undefined,
      subject: `${prefijo}[INCIDENCIA ${d.codigo_tipo || ""}] Exp. ${limpio(d.expedicion, 40)} · ${limpio(d.ubicacion, 40)} · ${limpio(d.referencia, 40)}`,
      text: texto,
      html: cuerpoHtml(d, fotos.length),
      attachments: fotos.map((f, i) => ({
        filename: `${limpio(d.referencia, 40)}_foto_${String(i + 1).padStart(2, "0")}.${f.ext}`,
        content: f.contenido,
      })),
    });
  } catch (e) {
    const motivo = /invalid login|auth/i.test(String(e.message))
      ? "Gmail ha rechazado el usuario o la contraseña de aplicación"
      : String(e.message).slice(0, 200);
    return json({ error: `El correo no ha salido: ${motivo}` }, 502);
  }

  return json({ ok: true, referencia: d.referencia, fotos: fotos.length });
};

export const config = { path: ["/api/incidencias", "/api/salud"] };
