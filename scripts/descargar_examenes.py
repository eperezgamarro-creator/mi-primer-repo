"""
Descarga los exámenes de la prueba de acceso a grado superior de Cataluña
desde cursosdeacceso.com y los ordena por materia en una carpeta del escritorio.

Uso:  python descargar_examenes.py
Solo usa la biblioteca estándar de Python (no hace falta instalar nada).
"""
import re
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

PAGINA_INICIAL = "https://www.cursosdeacceso.com/examenes-prueba-acceso-grado-superior-catalunya"
NOMBRE_CARPETA = "Examens Accés Grau Superior Catalunya"

CARPETAS = {
    "angles": "01 Anglès",
    "ingles": "01 Anglès",
    "english": "01 Anglès",
    "matematiques": "02 Matemàtiques",
    "matematicas": "02 Matemàtiques",
    "matematica": "02 Matemàtiques",
    "mates": "02 Matemàtiques",
    "catala": "03 Llengua catalana",
    "catalan": "03 Llengua catalana",
    "castella": "04 Llengua castellana",
    "castellano": "04 Llengua castellana",
    "geografia": "05 Geografia",
    "psicologia": "06 Psicologia i sociologia",
    "sociologia": "06 Psicologia i sociologia",
}

CABECERAS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def carpeta_escritorio():
    # El escritorio puede llamarse distinto según el sistema y si usas OneDrive
    casa = Path.home()
    for opcion in [casa / "OneDrive" / "Escritorio", casa / "OneDrive" / "Desktop",
                   casa / "Escritorio", casa / "Desktop"]:
        if opcion.is_dir():
            return opcion
    return casa / "Desktop"


def normalizar(texto):
    texto = texto.lower()
    reemplazos = {
        "á": "a", "à": "a", "é": "e", "è": "e", "í": "i",
        "ó": "o", "ò": "o", "ú": "u", "ü": "u", "ç": "c", "ñ": "n"
    }
    for original, nuevo in reemplazos.items():
        texto = texto.replace(original, nuevo)
    return texto


def materia_de(*textos):
    # Busca palabras completas en la URL y en el texto del enlace
    palabras = set()
    for texto in textos:
        palabras |= set(re.split(r"[^a-z0-9]+", normalizar(unquote(texto))))

    if palabras & {"psicologia", "sociologia"}:
        return CARPETAS["psicologia"]

    for clave, carpeta in CARPETAS.items():
        if clave in palabras:
            return carpeta
    return None


class Enlaces(HTMLParser):
    def __init__(self):
        super().__init__()
        self.enlaces = []  # (href, texto)
        self._href = None
        self._texto = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._texto = []

    def handle_data(self, data):
        if self._href:
            self._texto.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href:
            self.enlaces.append((self._href, " ".join(self._texto).strip()))
            self._href = None


def descargar(url):
    peticion = urllib.request.Request(url, headers=CABECERAS)
    with urllib.request.urlopen(peticion, timeout=60) as respuesta:
        return respuesta.read(), respuesta.headers.get_content_type()


def enlaces_de(url):
    contenido, _ = descargar(url)
    lector = Enlaces()
    lector.feed(contenido.decode("utf-8", errors="replace"))
    return [(urljoin(url, href), texto) for href, texto in lector.enlaces]


def es_pdf(url):
    return urlparse(url).path.lower().endswith(".pdf")


def buscar_pdfs():
    """Devuelve {url_pdf: (materia, texto)} de la página inicial y sus subpáginas de exámenes."""
    dominio = urlparse(PAGINA_INICIAL).netloc
    pdfs = {}
    visitadas = set()
    pendientes = [(PAGINA_INICIAL, "")]

    while pendientes:
        pagina, contexto = pendientes.pop(0)
        if pagina in visitadas:
            continue
        visitadas.add(pagina)
        try:
            enlaces = enlaces_de(pagina)
        except Exception as error:
            print(f"No se ha podido leer {pagina}: {error}")
            continue

        for url, texto in enlaces:
            url = url.split("#")[0]
            if es_pdf(url):
                materia = materia_de(url, texto, contexto)
                if materia and url not in pdfs:
                    pdfs[url] = (materia, texto)
            elif (pagina == PAGINA_INICIAL
                  and urlparse(url).netloc == dominio
                  and "catalu" in normalizar(url)
                  and url not in visitadas):
                # Subpáginas de Cataluña (p. ej. una por materia o por año): un nivel de profundidad
                pendientes.append((url, texto + " " + url))
    return pdfs


def main():
    destino_base = carpeta_escritorio() / NOMBRE_CARPETA
    print(f"Buscando exámenes en {PAGINA_INICIAL} ...")
    pdfs = buscar_pdfs()

    if not pdfs:
        print("No se ha encontrado ningún PDF de tus materias. "
              "Puede que la web haya cambiado o que los exámenes no sean PDFs directos.")
        return

    print(f"Encontrados {len(pdfs)} PDFs. Descargando en: {destino_base}\n")
    descargados, fallidos = 0, []

    for url, (materia, _) in sorted(pdfs.items(), key=lambda x: x[1][0]):
        carpeta = destino_base / materia
        carpeta.mkdir(parents=True, exist_ok=True)
        nombre = unquote(Path(urlparse(url).path).name)
        ruta = carpeta / nombre
        if ruta.exists():
            print(f"Ya existe: {materia}/{nombre}")
            continue
        try:
            contenido, _ = descargar(url)
            ruta.write_bytes(contenido)
            descargados += 1
            print(f"Descargado: {materia}/{nombre}")
        except Exception as error:
            fallidos.append(f"{url} ({error})")
        time.sleep(0.5)  # para no saturar la web

    print(f"\nTotal descargados: {descargados}")
    if fallidos:
        print("\nNo se han podido descargar:")
        for f in fallidos:
            print(f"- {f}")


if __name__ == "__main__":
    main()
