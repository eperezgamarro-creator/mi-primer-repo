# ------------------------------------------------------------------ versión escritorio + Archivador
s = rep(s, "grid-template-columns:repeat(4,1fr)}", "grid-template-columns:repeat(5,1fr)}")
s = rep(s, """Entrenar</button>
""", """Entrenar</button>
  <button data-tab="arch"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M3 10h18"/></svg>Archivador</button>
""")
s = rep(s, "({hoy,mat:materias,retos,logros})[t]()", "({hoy,mat:materias,retos,arch:archivador,logros})[t]()")
s = rep(s, "/* ---------- Logros ---------- */\nfunction logros(){", r"""/* ---------- Archivador: todas las herramientas por materia (como la versión de escritorio) ---------- */
const ARCH=[
  {id:'org',n:'Plan y simulacros',short:'Plan y examen',c:'--s-org',when:'Organización del curso y modo examen'},
  {id:'mat',n:'Matemàtiques',c:'--s-mat',when:'Lunes y jueves, presencial'},
  {id:'ang',n:'Anglès',c:'--s-ang',when:'Lunes y miércoles, presencial · English File Pre-int.'},
  {id:'cas',n:'Castellà',c:'--s-cas',when:'Martes, presencial'},
  {id:'cat',n:'Català',c:'--s-cat',when:'Martes y miércoles, presencial'},
  {id:'geo',n:'Geografia',c:'--s-geo',when:'Online IOC · sesión del sábado'},
  {id:'psi',n:'Psicologia i Sociologia',short:'Psicologia',c:'--s-psi',when:'Online IOC · sesión del sábado'},
  {id:'esc',n:'Letra y velocidad',c:'--s-esc',when:'10–15 min al día · para el examen escrito'}];
function archivador(){
  const f=st.archF&&ARCH.some(a=>a.id===st.archF)?st.archF:'all';
  const list=f==='all'?ARCH:ARCH.filter(a=>a.id===f);
  const row=(t,a)=>{const others=t.subj.filter(x=>x!==a.id).map(x=>(ARCH.find(y=>y.id===x)||{}).short||(ARCH.find(y=>y.id===x)||{}).n).filter(Boolean);
    return `<button class="ar-tool" data-tool="${t.id}"><span class="lbl">${esc(t.kind)}</span><b>${esc(t.name)}</b><span class="ar-d">${esc(t.desc)}</span>${others.length&&f!=='all'?`<span class="ar-s">También en ${esc(others.join(', '))}</span>`:''}<span class="ar-go">${t.pdf?'Ver cuaderno':'Abrir'} →</span></button>`;};
  app.innerHTML=`<div class="view"><div class="hello"><div><p class="lbl">${TOOLS.length} herramientas · juegos, mapas, ejercicios y cuadernos</p><h1>Archivador</h1></div></div>
   <div class="ar-f"><button data-af="all" aria-pressed="${f==='all'}" style="--c:var(--ink)">Todo <span>${TOOLS.length}</span></button>${ARCH.map(a=>`<button data-af="${a.id}" aria-pressed="${f===a.id}" style="--c:var(${a.c})"><i></i>${esc(a.short||a.n)} <span>${toolsOf(a.id).length}</span></button>`).join('')}</div>
   ${list.map(a=>{const ts=f==='all'&&a.id!=='org'?toolsOf(a.id).filter(t=>!t.subj.includes('org')):toolsOf(a.id);if(!ts.length)return '';
     return `<section class="panel ar-sec" style="--c:var(${a.c})"><div class="ar-h"><h2>${esc(a.n)}</h2><span class="muted">${esc(a.when)}</span></div>
     ${ts.map(t=>row(t,a)).join('')}${EXAMS2.includes(a.id)?`<button class="ar-sim" data-sim="${a.id}">Simulacro cronometrado de ${esc(a.short||a.n)} →</button>`:''}</section>`;}).join('')}</div>`;
  app.querySelectorAll('[data-af]').forEach(b=>b.onclick=()=>{st.archF=b.dataset.af;save();archivador();});
  app.querySelectorAll('[data-tool]').forEach(b=>b.onclick=()=>openTool(b.dataset.tool));
  app.querySelectorAll('[data-sim]').forEach(b=>b.onclick=()=>openTool('examen',b.dataset.sim));
  window.scrollTo(0,0);
}
/* ---------- Logros ---------- */
function logros(){""")
s = rep(s, "</style>", """:root{--s-org:#9A5B12;--s-esc:#6B5E4A}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--s-org:#E3A85A;--s-esc:#C2B49A}}
:root[data-theme="dark"]{--s-org:#E3A85A;--s-esc:#C2B49A}
.ar-f{display:flex;flex-wrap:wrap;gap:6px}
.ar-f button{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--rule);background:var(--sheet);border-radius:6px;padding:6px 10px;font-size:14px;font-weight:700}
.ar-f button i{width:9px;height:9px;border-radius:2px;background:var(--c)}
.ar-f button span{font-family:var(--f-mono);font-size:12px;color:var(--ink-2)}
.ar-f button[aria-pressed="true"]{border-color:var(--c);box-shadow:inset 0 -3px 0 var(--c)}
.ar-sec{border-top:4px solid var(--c)}
.ar-h{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;padding-bottom:6px}
.ar-h h2{font-size:1.5rem}.ar-h span{font-size:13.5px}
.ar-tool{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 20px;align-items:center;width:100%;text-align:left;padding:14px 0;border-top:1px solid var(--rule-soft)}
.ar-tool>*{grid-column:1}
.ar-tool b{font-family:var(--f-display);font-size:1.2rem}
.ar-d{color:var(--ink-2);font-size:15px;max-width:62ch}
.ar-s{color:var(--ink-2);font-size:13px}
.ar-go{grid-column:2;grid-row:1 / span 4;font-weight:700;font-size:14px;border:1.5px solid var(--ink);border-radius:4px;padding:8px 12px;white-space:nowrap}
.ar-tool:hover .ar-go{background:var(--ink);color:var(--sheet)}
.ar-sim{display:block;width:100%;text-align:left;margin-top:8px;border:1px dashed var(--c);border-radius:4px;padding:9px 12px;font-weight:700;font-size:14px}
.ar-sim:hover{border-style:solid}
@media (max-width:520px){.ar-tool{grid-template-columns:1fr}.ar-go{grid-column:1;grid-row:auto;justify-self:start;margin-top:8px}}
/* escritorio: las pestañas pasan a una barra lateral */
@media (min-width:900px){
  .tabs{top:0;right:auto;width:212px;border-top:0;border-right:1px solid var(--rule);padding:28px 12px}
  .tabs .in{display:flex;flex-direction:column;gap:4px;max-width:none}
  .tabs .in::before{content:"Estudi PACFGS";font-family:var(--f-display);font-weight:800;font-size:1.35rem;letter-spacing:-.02em;padding:0 12px 18px}
  .tabs button{flex-direction:row;justify-content:flex-start;gap:12px;font-size:15.5px;padding:11px 12px;border-radius:8px}
  .tabs button:hover{background:var(--bg)}
  .tabs button[aria-current="page"]{background:var(--bg)}
  body:has(#tabs:not([hidden])){padding-left:212px}
  .view{padding-block:28px 56px}
}
</style>""")
