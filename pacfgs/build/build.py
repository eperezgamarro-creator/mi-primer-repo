import sys, re, json, base64
sys.path.insert(0, sys.argv[3])
import mates_data as M
NB = lambda t: t.replace(' %', '\u00a0%')  # que «30 %» no se parta entre líneas
M.EXTRA_HTML = {k: NB(v) for k, v in M.EXTRA_HTML.items()}
M.NEW_TOPIC['html'] = NB(M.NEW_TOPIC['html'])
M.MC = [(t, NB(q), [NB(x) for x in o], NB(e)) for t, q, o, e in M.MC]

SRC, OUT = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()

def rep(text, old, new, count=1, where=''):
    n = text.count(old)
    assert n == count, f'{where}: expected {count} of {old[:80]!r}, found {n}'
    return text.replace(old, new)

# ------------------------------------------------------------------ tools
m = re.search(r'const PAY=', s)
PAY, _ = json.JSONDecoder().raw_decode(s, m.end())
tools = {k: base64.b64decode(v).decode('utf-8') for k, v in PAY['html'].items()}

PAC_JS = r"""<script>/* Registro común de fallos (lo lee el repaso inteligente de la app 2.x) */
window.PAC=window.PAC||(()=>{const K='pac-miss';const clean=s=>String(s==null?'':s).replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
 function miss(o){try{if(!o||!o.q)return;const L=JSON.parse(localStorage.getItem(K)||'[]');const id=o.id||((o.s||'x')+'|'+clean(o.q).slice(0,160));const now=Date.now();const ex=L.find(x=>x.id===id);
  if(ex){if(now-(ex.t||0)>60000)ex.n=(ex.n||1)+1;ex.box=0;ex.due=now;ex.t=now;ex.done=false;if(o.a)ex.a=o.a;if(o.e)ex.e=o.e;}
  else L.push(Object.assign({},o,{id,n:1,box:0,due:now,t:now,t0:now}));
  localStorage.setItem(K,JSON.stringify(L.slice(-800)));}catch(e){}}
 function unmiss(id){try{const L=JSON.parse(localStorage.getItem(K)||'[]');const i=L.findIndex(x=>x.id===id);if(i<0)return;if((L[i].n||1)<=1)L.splice(i,1);else L[i].n--;localStorage.setItem(K,JSON.stringify(L));}catch(e){}}
 return {miss,unmiss,clean};})();</script>
"""

def add_pac(h, name):
    assert not re.search(r'\bPAC\b', h), name
    if '</head>' in h:
        return rep(h, '</head>', PAC_JS + '</head>', where=name)
    i = h.index('<script>')
    return h[:i] + PAC_JS + h[i:]

# Inglés de cada día
h = add_pac(tools['ingles-dia'], 'ingles-dia')
h = rep(h, "S.done=true;S.res[S.i]=ok;prog[ex.id]=ok?1:0;save();",
        "S.done=true;S.res[S.i]=ok;prog[ex.id]=ok?1:0;save();\n    if(!ok)PAC.miss({id:'icd|'+ex.id,s:'ang',src:'Inglés de cada día',q:'<span class=\"muted\">'+ins+'</span><br>'+(ex.t==='o'?ex.es:ex.q),a:fullText(ex),e:ex.n||'',o:ex.t==='c'?ex.o:undefined,ai:ex.t==='c'?ex.a:undefined});",
        where='ingles-dia')
tools['ingles-dia'] = h

# Inglés de bolsillo
h = add_pac(tools['ingles-bolsillo'], 'ingles-bolsillo')
h = rep(h, "phase='result'; before=snap(cur.id); grade(cur.id,ok);",
        "phase='result'; before=snap(cur.id); grade(cur.id,ok);\n  if(!ok)PAC.miss({id:'bol|'+cur.id,s:'ang',src:'Inglés de bolsillo',q:'<span class=\"muted\">'+esc(cur.hint)+'</span><br><b>'+esc(cur.front)+'</b>',a:cur.back});",
        where='bolsillo')
h = rep(h, "restore(cur.id,before); grade(cur.id,true); before=snap(cur.id);",
        "restore(cur.id,before); grade(cur.id,true); before=snap(cur.id); PAC.unmiss('bol|'+cur.id);",
        where='bolsillo')
tools['ingles-bolsillo'] = h

# Geo en Joc / Ment en Joc
for name, subj, label in [('geo-joc', 'geo', 'Geo en Joc'), ('ment-joc', 'psi', 'Ment en Joc')]:
    h = add_pac(tools[name], name)
    h = rep(h, "var isCorrect = q._order[i].correct;",
            "var isCorrect = q._order[i].correct;\n  if(!isCorrect)PAC.miss({s:'%s',src:'%s · '+((TOPIC_BY_ID[q.t]||{}).title||''),q:q.q,o:q.o,ai:q.c,e:q.e});" % (subj, label),
            where=name)
    tools[name] = h

# Fracciones
h = add_pac(tools['fracciones'], 'fracciones')
h = rep(h, "  const ok = status === 'ok';\n",
        "  const ok = status === 'ok';\n  if (!ok) { const fx = t => String(t == null ? '' : t).replace(/class=\"fr\"/g, 'class=\"frac\"'); PAC.miss({ s: 'mat', src: 'Fracciones', q: fx((q.hint ? '<span class=\"muted\">' + q.hint + '</span><br>' : '') + q.prompt), a: fx(q.answerHtml), e: fx((q.steps || []).join('<br>')) }); }\n",
        where='fracciones')
tools['fracciones'] = h

# Family Tree
h = add_pac(tools['family-tree'], 'family-tree')
for flag, arr, idx in [('detAnswered', 'detectiveQuestions', 'detIndex'), ('genAnswered', 'genitiveQuestions', 'genIndex'), ('graAnswered', 'grammarQuestions', 'graIndex')]:
    pat = re.compile(r'(%s = true;\s*const q = %s\[%s\];)' % (flag, arr, idx))
    assert len(pat.findall(h)) == 1, arr
    h = pat.sub(lambda mm: mm.group(1) + "\n      if (selectedIndex !== q.correct) PAC.miss({ s: 'ang', src: 'Family Tree', q: q.q + (q.hint ? '<br><span class=\"muted\">' + q.hint + '</span>' : ''), o: q.options, ai: q.correct, e: q.explanation });", h)
tools['family-tree'] = h

# Plan de Lenguas: cuaderno de errores -> cola común; simulacros -> nota estimada
h = add_pac(tools['lenguas'], 'lenguas')
h = rep(h, "function addRow(coll,obj){\n",
        "function addRow(coll,obj){\n  try{const sj=obj.lengua==='ca'?'cat':'cas';\n    if(coll==='errores')PAC.miss({s:sj,src:'Plan de Lenguas',q:(obj.regla?'<span class=\"muted\">'+esc(obj.regla)+'</span><br>':'')+'<b>'+esc(obj.mal)+'</b>',a:esc(obj.bien)});\n    if(coll==='simulacros'&&typeof obj.nota==='number'){const L=JSON.parse(localStorage.getItem('pac-sims')||'[]');L.push({s:sj,v:obj.nota,t:Date.now(),src:'Plan de Lenguas'});localStorage.setItem('pac-sims',JSON.stringify(L.slice(-200)));}}catch(e){}\n",
        where='lenguas')
tools['lenguas'] = h

# Sala d'examen: fecha exacta en el historial para ordenar los simulacros
tools['examen'] = rep(tools['examen'], 'st.hist.push({', 'st.hist.push({t:Date.now(),', count=3, where='examen')

for k in ['ingles-dia', 'ingles-bolsillo', 'geo-joc', 'ment-joc', 'fracciones', 'family-tree', 'lenguas', 'examen']:
    old = PAY['html'][k]
    new = base64.b64encode(tools[k].encode('utf-8')).decode('ascii')
    s = rep(s, '"%s"' % old, '"%s"' % new, where='PAY ' + k)

# ------------------------------------------------------------------ DECK (Mates)
m = re.search(r'const DECK=', s)
DECK, end = json.JSONDecoder().raw_decode(s, m.end())
for t in DECK['topics']:
    if t['id'] in M.EXTRA_HTML:
        t['html'] = t['html'].rstrip() + '\n' + M.EXTRA_HTML[t['id']]
last_mat = max(i for i, t in enumerate(DECK['topics']) if t['s'] == 'mat')
DECK['topics'].insert(last_mat + 1, M.NEW_TOPIC)
new_cards = M.cards()
ids = {c['id'] for c in DECK['cards']}
assert not ids & {c['id'] for c in new_cards}
DECK['cards'].extend(new_cards)
deck_js = json.dumps(DECK, ensure_ascii=False, separators=(',', ':'))
assert '</script' not in deck_js.lower()
s = s[:m.end()] + deck_js + s[end:]

# ------------------------------------------------------------------ app JS
s = rep(s, "<title>Estudi PACFGS 2.0</title>", "<title>Estudi PACFGS 2.1</title>")
s = rep(s, '<p class="lbl">Estudi PACFGS 2.0</p>', '<p class="lbl">Estudi PACFGS 2.1</p>')

s = rep(s, "'mat-est':'T12'}", "'mat-est':['T10','T12'],'mat-prob':['T1','T2','T4','T5','T10','T12']}")
s = rep(s, "const genCard=(tid,s='mat')=>{const ex=MG.make(tid);",
        "const genCard=(tid,s='mat')=>{if(Array.isArray(tid))tid=tid[Math.floor(Math.random()*tid.length)];const ex=MG.make(tid);")

# --- repaso espaciado: intervalos largos, dominado tras 14 días
s = rep(s, "const INT=[0,1,1,3,7,16];", "const INT=[0,1,3,7,14,30,60]; // días hasta el siguiente repaso según la caja")
s = rep(s, "const isDom=c=>{const x=st.c[c.id];return !!x&&x.b>=4;};",
        "const isDom=c=>{const x=st.c[c.id];return !!x&&x.b>=5;}; // acertada tras un repaso de 14 días")
s = rep(s, "const save=()=>{try{localStorage.setItem(LS,JSON.stringify(st));}catch(e){}if(typeof syncTick==='function')syncTick();};",
        "/* 2.1: las cajas antiguas (intervalos 1,1,3,7,16) pasan a la escala nueva (1,3,7,14,30,60) */\n"
        "function migrate(){if(st.srs2)return false;for(const id in st.c){const x=st.c[id];x.b=[0,1,1,2,3,4][Math.min(5,x.b||0)];}st.srs2=1;return true;}\n"
        "if(migrate()){try{localStorage.setItem(LS,JSON.stringify(st));}catch(e){}}\n"
        "const save=()=>{try{localStorage.setItem(LS,JSON.stringify(st));}catch(e){}if(typeof syncTick==='function')syncTick();};")
s = rep(s, "function reloadState(){try{const s2=JSON.parse(localStorage.getItem(LS)||'null');if(s2)st=Object.assign(blank(),s2);}catch(e){}}",
        "function reloadState(){try{const s2=JSON.parse(localStorage.getItem(LS)||'null');if(s2)st=Object.assign(blank(),s2);}catch(e){}if(migrate())save();}")

OLD_AWARD = """  if(c.id&&!S.o.crono){const x=st.c[c.id]||{b:0};
    if(score===0){x.b=1;x.due=TODAY;if(S.o.srs&&!S.again.has(c.id)){S.again.add(c.id);S.q.push(c);}}
    else if(score===1){x.b=Math.max(1,x.b);x.due=addDays(1);}
    else{x.b=Math.min(5,x.b+1);x.due=addDays(INT[x.b]);}
    st.c[c.id]=x;}"""
NEW_AWARD = """  if(c.id&&!S.o.crono){const had=st.c[c.id],x=had||{b:0},dueNow=!had||x.due<=TODAY;
    if(score===0){x.b=0;x.due=TODAY;if(S.o.srs&&!S.again.has(c.id)){S.again.add(c.id);S.q.push(c);}}
    else if(score===1){x.b=Math.max(1,x.b);const d1=addDays(Math.max(1,Math.round(INT[x.b]/2)));if(dueNow||d1<x.due)x.due=d1;} // dudé: no sube de caja, vuelve a mitad de plazo
    else if(dueNow){x.b=Math.min(INT.length-1,x.b+1);x.due=addDays(INT[x.b]);} // solo sube de caja si tocaba repasarla
    x.due=capDue(x.due);x.l=TODAY;st.c[c.id]=x;}"""
s = rep(s, OLD_AWARD, NEW_AWARD)

# --- nota estimada, prioridad por puntos y recta final (después de daysLeft)
ANCHOR = "const planMark=k=>{"
s = rep(s, ANCHOR, r"""/* ---------- recta final: todo lo visto vuelve antes del examen ---------- */
const FINAL_DAYS=28;
const inFinal=()=>{const n=daysLeft();return n>0&&n<=FINAL_DAYS;};
function capDue(d){ // ningún repaso queda para después del examen: se reparte en sus últimas 3 semanas
  const ex=examDate(),lim=new Date(ex);lim.setDate(lim.getDate()-2);const L=iso(lim);
  if(d<=L||TODAY>=L)return d;
  const t0=new Date();t0.setHours(0,0,0,0);t0.setDate(t0.getDate()+1);
  const from=new Date(Math.max(t0.getTime(),ex.getTime()-21*DAY));
  const span=Math.max(0,Math.round((lim-from)/DAY));const r=new Date(from);r.setDate(r.getDate()+Math.floor(Math.random()*(span+1)));
  const ri=iso(r);return ri<d?ri:d;}
function startFinal(sel,len,back){
  const P=cardsOf(c=>st.c[c.id]&&(!sel||sel.includes(c.s)));
  if(!P.length){toast('Aún no has visto tarjetas: empieza por el repaso inteligente');return;}
  const wk=addDays(-7),rec=c=>(st.c[c.id].l||'')>wk?1:0;
  const q=shuffle(P).sort((a,b)=>rec(a)-rec(b)||((st.c[a.id].l||'')<(st.c[b.id].l||'')?-1:(st.c[a.id].l||'')>(st.c[b.id].l||'')?1:0)).slice(0,len||st.goal);
  run(shuffle(q),{title:'Recta final',srs:true,back:back||(()=>setTab(TAB))});
}
/* ---------- nota estimada ----------
   Reglas de la prueba de acceso a grado superior en Catalunya: parte común (lenguas y mates) y parte
   específica (dos materias); cada parte es la media de sus ejercicios, hace falta un 4 en cada parte
   para hacer media y un 5 de nota final. Compruébalo en la convocatoria de cada año. */
const RULES={common:['cat','cas','ang','mat'],spec:['geo','psi'],minPart:4,pass:5,course:0.2};
const CRED=[0,.2,.4,.6,.8,1,1]; // valor de una tarjeta según su caja
function cardEst(k){const cs=cardsOf(c=>c.s===k);if(!cs.length)return 0;let v=0;cs.forEach(c=>{const x=st.c[c.id];if(x)v+=CRED[Math.min(6,x.b||0)];});return 10*v/cs.length;}
function simsOf(k){const out=[];
  try{const e=JSON.parse(localStorage.getItem('sala-examen-v1')||'{}');(e.hist||[]).forEach((h,i)=>{if(h&&h.s===k&&typeof h.score==='number')out.push({v:h.score,t:h.t||i});});}catch(e){}
  try{(JSON.parse(localStorage.getItem('pac-sims')||'[]')||[]).forEach(h=>{if(h&&h.s===k&&typeof h.v==='number')out.push({v:h.v,t:h.t||0});});}catch(e){}
  return out.sort((a,b)=>a.t-b.t);}
function estSubj(k){const c=cardEst(k),sm=simsOf(k).slice(-3);
  if(!sm.length)return {v:c,c,sim:null,n:0};
  const w=[1,2,3].slice(3-sm.length);let a=0,ws=0;sm.forEach((x,i)=>{a+=x.v*w[i];ws+=w[i];});const sim=a/ws;
  return {v:0.7*sim+0.3*c,c,sim,n:sm.length};}
const mean=a=>a.reduce((x,y)=>x+y,0)/a.length;
const WGT=k=>RULES.common.includes(k)?0.5/RULES.common.length:0.5/RULES.spec.length; // peso en la nota final
function estimate(){const by={};Object.keys(SUBJ).forEach(k=>by[k]=estSubj(k));
  const com=mean(RULES.common.map(k=>by[k].v)),spe=mean(RULES.spec.map(k=>by[k].v));
  const ok=com>=RULES.minPart&&spe>=RULES.minPart,raw=(com+spe)/2;
  const bonus=typeof st.course==='number'&&st.course>=5?st.course*RULES.course:0;
  return {by,com,spe,ok,raw,bonus,fin:ok?Math.min(10,raw+bonus):null};}
function pointsOrder(){const E=estimate(),mo=missOpen();
  return Object.keys(SUBJ).map(k=>{const part=RULES.common.includes(k)?E.com:E.spe;let g=WGT(k)*(10-E.by[k].v);if(part<RULES.minPart+0.5)g*=2;g+=mo.filter(m=>m.s===k).length*0.002;return [k,g];})
    .sort((a,b)=>b[1]-a[1]).map(x=>x[0]);}
const f1=n=>n==null?'—':n.toFixed(1).replace('.',',');
function notaPanel(full){const E=estimate(),top=pointsOrder().slice(0,2);
  const cl=v=>v>=RULES.pass?'n-ok':v>=RULES.minPart?'n-mid':'n-bad';
  const head=E.ok?(E.fin>=RULES.pass?'aprobarías':'no llegas al 5'):'no hace media: una parte está por debajo de 4';
  return `<div class="panel nota"><div class="note"><span class="lbl">Si el examen fuera hoy</span><span class="lbl">estimación</span></div>
   <div class="nbig ${E.ok?cl(E.fin):'n-bad'}"><b>${f1(E.ok?E.fin:E.raw)}</b><span>${head}</span></div>
   <div class="nparts"><div><span class="lbl">Parte común</span><b class="${cl(E.com)}">${f1(E.com)}</b></div><div><span class="lbl">Parte específica</span><b class="${cl(E.spe)}">${f1(E.spe)}</b></div></div>
   ${full?`<div>${Object.keys(SUBJ).map(k=>{const x=E.by[k];return `<div class="mrow"><span style="font-weight:700">${SUBJ[k].n}</span><span class="xpbar"><i style="width:${x.v*10}%;background:var(${SUBJ[k].c})"></i></span><span class="mono" style="font-size:13px">${f1(x.v)}</span></div>
     <p class="muted" style="font-size:12.5px;margin:-2px 0 8px">${x.n?`${x.n} simulacro${x.n>1?'s':''}: ${f1(x.sim)} · tarjetas: ${f1(x.c)}`:`Sin simulacros: solo cuentan las tarjetas (${f1(x.c)})`} · 1 punto aquí = ${String(WGT(k)).replace('.',',')} en la final</p>`;}).join('')}</div>`:''}
   <p style="font-size:14px">Donde más nota ganas ahora: <b>${top.map(k=>SUBJ[k].n).join('</b> y <b>')}</b>.${E.ok&&E.bonus?` Incluye +${f1(E.bonus)} del curso de preparación.`:''}</p>
   <p class="muted" style="font-size:12.5px">Cuenta tus 3 últimos simulacros de cada materia (70 %) y las tarjetas dominadas (30 %). Sin simulacros sale baja a propósito: haz uno de cada materia para afinarla.</p></div>`;}
const planMark=k=>{""")
s = rep(s, "function weakOrder(){return Object.keys(SUBJ).map(k=>{const due=missOpen().filter(m=>m.s===k).length;return [k,mastery(c=>c.s===k)-due*0.01];}).sort((a,b)=>a[1]-b[1]).map(x=>x[0]);}",
        "function weakOrder(){return pointsOrder();} // primero la materia donde más nota final se gana")
s = rep(s, "' · tu materia más floja'", "' · donde más nota ganas'")
s = rep(s, "  const pt=TOOLS.find(t=>t.id===PRACT[subj]);\n",
        "  if(inFinal())items.push({k:'fin',c:'--gold',t:'Recta final',d:`Repasa lo que ya sabías · faltan ${daysLeft()} días`,done:!!p.fin,act:()=>{planMark('fin');startFinal(null,Math.max(20,st.goal));}});\n  const pt=TOOLS.find(t=>t.id===PRACT[subj]);\n")

# Hoy: panel de nota
s = rep(s, """     <div class="panel" style="display:flex;flex-direction:column;gap:8px"><p class="lbl">Tus fallos</p>""",
        """     ${notaPanel(false)}
     <div class="panel" style="display:flex;flex-direction:column;gap:8px"><p class="lbl">Tus fallos</p>""")
# Progreso: panel completo + nota del curso
s = rep(s, """   <div class="cols"><div>
   <div class="panel"><p class="lbl" style="margin-bottom:6px">Por materia</p>""",
        """   <div class="cols"><div>
   ${notaPanel(true)}
   <div class="panel"><p class="lbl" style="margin-bottom:6px">Por materia</p>""")
s = rep(s, """   <div class="panel" style="display:flex;flex-direction:column;gap:10px"><p class="lbl">Guardado</p>""",
        """   <div class="panel" style="display:flex;flex-direction:column;gap:10px"><p class="lbl">Nota del curso de preparación (opcional)</p><div class="btnrow"><input type="number" class="field" id="crs" min="0" max="10" step="0.1" placeholder="Ej. 7,5" value="${typeof st.course==='number'?st.course:''}"><button class="btn2" id="crss">Guardar</button></div><p class="muted" style="font-size:13px">Si está aprobado, se suma × ${String(RULES.course).replace('.',',')} a la nota de la prueba. Déjalo vacío si no haces el curso.</p></div>
   <div class="panel" style="display:flex;flex-direction:column;gap:10px"><p class="lbl">Guardado</p>""")
s = rep(s, "  document.getElementById('exp').onclick=exportData;\n",
        "  document.getElementById('crss').onclick=()=>{const v=String(document.getElementById('crs').value).replace(',','.').trim();if(v===''){delete st.course;save();logros();toast('Nota del curso quitada');return;}const n=parseFloat(v);if(!isNaN(n)&&n>=0&&n<=10){st.course=Math.round(n*10)/10;save();logros();toast('Nota del curso guardada');}};\n  document.getElementById('exp').onclick=exportData;\n")
# Retos: recta final
s = rep(s, "   <div class=\"grid\">${Object.keys(SUBJ).map(k=>`<button class=\"cover\" data-cr=",
        "   <button class=\"cta col\" id=\"fin\" style=\"--c:var(--s-psi)\"><span class=\"lbl\" style=\"color:inherit;opacity:.75\">Recta final${inFinal()?` · faltan ${daysLeft()} días`:''}</span><b>Repasa lo que ya sabías</b><span>Primero lo que hace más tiempo que no ves, para que nada se olvide antes del examen</span><span class=\"go\">Empezar</span></button>\n   <div class=\"grid\">${Object.keys(SUBJ).map(k=>`<button class=\"cover\" data-cr=")
s = rep(s, "  document.getElementById('jocs').onclick=()=>openTool('jocs');\n",
        "  document.getElementById('jocs').onclick=()=>openTool('jocs');\n  document.getElementById('fin').onclick=()=>startFinal(null,20,back);\n")

# CSS
s = rep(s, "</style>", """.nota{display:flex;flex-direction:column;gap:10px}
.nbig{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.nbig b{font-family:var(--f-display);font-size:2.6rem;line-height:1}
.nbig span{font-size:14px;color:var(--ink-2)}
.nparts{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.nparts b{display:block;font-family:var(--f-display);font-size:1.5rem}
.n-ok{color:var(--ok)}.n-mid{color:var(--gold)}.n-bad{color:var(--bad)}
</style>""")

open(OUT, 'w', encoding='utf-8').write(s)
print('ok', len(s), 'new cards', len(new_cards), 'topics', len(DECK['topics']), 'cards', len(DECK['cards']))
