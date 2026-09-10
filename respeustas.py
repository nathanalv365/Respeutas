from pathlib import Path
import html, json

items = [
    (1, "Formato de inventario de dotaciones", "Ledis"),
    (2, "N/A", ""),
    (3, "N/A", ""),
    (4, "N/A", ""),
    (5, "N/A", ""),
    (6, "N/A", ""),
    (7, "N/A", ""),
    (8, "Matriz de daño Anti-Juridico", "Leidy"),
    (9, "N/A", ""),
    (10, "N/A", ""),
    (11, "Licencia de funcionamiento", ""),
    (12, "N/A", ""),
    (13, "N/A", ""),
    (14, "Licencia de funcionamiento", ""),
    (15, "N/A", ""),
    (16, "N/A", ""),
    (17, "N/A", ""),
    (18, "N/A", ""),
    (19, "N/A", ""),
    (20, "N/A", ""),
    (21, "N/A", ""),
    (22, "N/A", ""),
    (23, "N/A", ""),
    (24, "Plan de capacitacion", ""),
    (25, "Certificaso de Fumigacion", ""),
    (26, "N/A", ""),
    (27, "Formato Ejecutado del control de Vectores (Por confirmar)", "Yeimi"),
    (28, "", "Yeimi"),
    (29, "Formato Ejecutado del Programa de Control de agua (Por confirmar)", "Yeimi"),
    (30, "Por confirmar", ""),
    (31, "N/A", ""),
    (32, "N/A", ""),
    (33, "N/A", ""),
    (34, "N/A", ""),
    (35, "N/A", ""),
    (36, "N/A", ""),
    (37, "N/A", ""),
    (38, "N/A", ""),
    (39, "N/A", ""),
    (40, "N/A", ""),
    (41, "N/A", ""),
    (42, "N/A", ""),
    (43, "N/A", ""),
    (44, "N/A", ""),
    (45, "N/A", ""),
    (46, "N/A", ""),
    (47, "N/A", ""),
    (48, "N/A", ""),
    (49, "N/A", ""),
    (50, "N/A", ""),
    (51, "N/A", ""),
    (52, "Certificacion De Reintegros de recursos no Ejecutados", "Daniela"),
    (53, "Consignaciones de rendimientos financieros generados por los aportes al ICBF", "Daniela"),
    (54, "N/A", ""),
    (55, "N/A", ""),
    (56, "N/A", ""),
    (57, "N/A", ""),
    (58, "N/A", ""),
    (59, "N/A", ""),
    (60, "N/A", ""),
    (61, "N/A", ""),
    (62, "N/A", ""),
    (63, "N/A", ""),
    (64, "N/A", ""),
    (65, "N/A", ""),
    (66, "N/A", ""),
    (67, "N/A", ""),
    (68, "N/A", ""),
    (69, "N/A", ""),
    (70, "N/A", ""),
    (71, "Declaracion de estados financieros", "Daniela"),
    (72, "N/A", ""),
    (73, "N/A", ""),
    (74, "N/A", ""),
    (75, "Anexar certificado de representante legal", ""),
    (76, "N/A", ""),
    (77, "N/A", ""),
    (78, "N/A", ""),
    (79, "N/A", ""),
    (80, "N/A", ""),
    (81, "N/A", ""),
    (82, "N/A", ""),
    (83, "N/A", ""),
    (84, "N/A", ""),
    (85, "Solicitud a la gobernacion sobre el traslado", "Gobernación"),
    (86, "N/A", ""),
    (87, "N/A", ""),
    (88, "N/A", ""),
    (89, "N/A", ""),
    (90, "N/A", ""),
]

records = [
    {"id": n, "evidence": evidence, "person": person, "done": False, "notes": ""}
    for n, evidence, person in items
]

people = sorted({x["person"] for x in records if x["person"]})
people_options = "\n".join(
    f'<option value="{html.escape(p)}">{html.escape(p)}</option>' for p in people
)

records_js = json.dumps(records, ensure_ascii=False)

doc = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Seguimiento · Respuesta Acción de Tutela</title>
<style>
:root {{
  --bg:#f5f7fb; --panel:#ffffff; --ink:#172033; --muted:#667085;
  --line:#e6eaf0; --accent:#315efb; --accent2:#173ea5; --ok:#16845b;
  --warn:#b66a00; --shadow:0 12px 35px rgba(20,31,52,.08); --radius:18px;
}}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;
       background:linear-gradient(180deg,#eef3ff 0,#f7f8fb 260px); color:var(--ink); }}
.container {{ max-width:1200px; margin:0 auto; padding:34px 22px 60px; }}
header {{ display:flex; justify-content:space-between; gap:20px; align-items:flex-start; margin-bottom:22px; }}
h1 {{ margin:0 0 7px; font-size:30px; letter-spacing:-.5px; }}
.subtitle {{ margin:0; color:var(--muted); max-width:730px; line-height:1.5; }}
.badge {{ padding:9px 13px; border:1px solid #dbe4ff; background:#fff; border-radius:999px; color:var(--accent2); font-weight:700; font-size:13px; }}
.grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin:20px 0; }}
.card {{ background:rgba(255,255,255,.92); border:1px solid var(--line); box-shadow:var(--shadow); border-radius:var(--radius); padding:18px; }}
.stat-label {{ color:var(--muted); font-size:13px; }}
.stat-value {{ font-size:28px; font-weight:800; margin-top:4px; }}
.progress-wrap {{ margin-top:9px; height:8px; background:#edf0f5; border-radius:999px; overflow:hidden; }}
.progress {{ height:100%; width:0; background:linear-gradient(90deg,var(--accent),#6a82ff); transition:width .25s ease; }}
.toolbar {{ display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-bottom:16px; }}
input,select,button,textarea {{ font:inherit; }}
.search {{ flex:1 1 300px; min-width:240px; border:1px solid var(--line); background:#fff; border-radius:12px; padding:12px 14px; outline:none; }}
select {{ border:1px solid var(--line); background:#fff; border-radius:12px; padding:12px 14px; }}
button {{ border:1px solid var(--line); background:#fff; border-radius:12px; padding:11px 14px; cursor:pointer; font-weight:650; }}
button:hover {{ border-color:#c6d1e5; background:#f9fbff; }}
button.primary {{ background:var(--accent); color:white; border-color:var(--accent); }}
button.danger {{ color:#b42318; }}
.table-card {{ padding:0; overflow:hidden; }}
.table-head {{ padding:18px 18px 0; color:var(--muted); font-size:13px; }}
table {{ width:100%; border-collapse:collapse; }}
th,td {{ padding:15px 18px; border-bottom:1px solid var(--line); vertical-align:top; text-align:left; }}
th {{ font-size:12px; text-transform:uppercase; letter-spacing:.06em; color:#7a8497; background:#fbfcfe; }}
tr.done {{ background:#f5fbf8; }}
.question {{ font-weight:800; }}
.evidence {{ margin-top:4px; line-height:1.42; }}
.n-a {{ color:#98a2b3; font-style:italic; }}
.person {{ display:inline-flex; padding:6px 9px; border-radius:999px; background:#edf2ff; color:var(--accent2); font-size:12px; font-weight:750; }}
.unassigned {{ background:#f2f4f7; color:#667085; }}
.status {{ display:inline-flex; align-items:center; gap:7px; font-weight:750; font-size:13px; color:var(--muted); }}
.status.done {{ color:var(--ok); }}
.status.pending {{ color:var(--warn); }}
.check {{ width:20px; height:20px; accent-color:var(--accent); cursor:pointer; }}
.notes {{ width:100%; min-width:180px; resize:vertical; min-height:48px; border:1px solid var(--line); border-radius:10px; padding:8px 10px; background:#fff; }}
.actions {{ display:flex; gap:8px; align-items:center; }}
.empty {{ padding:45px; text-align:center; color:var(--muted); }}
footer {{ margin-top:16px; color:#8a94a6; font-size:12px; text-align:center; }}
@media (max-width:850px) {{
  .grid {{ grid-template-columns:repeat(2,1fr); }}
  table, thead, tbody, tr, th, td {{ display:block; }}
  thead {{ display:none; }}
  tr {{ padding:14px 0; border-bottom:1px solid var(--line); }}
  td {{ border:0; padding:7px 16px; }}
  td::before {{ content:attr(data-label); display:block; color:#8a94a6; text-transform:uppercase; letter-spacing:.05em; font-size:10px; margin-bottom:4px; font-weight:750; }}
}}
@media (max-width:560px) {{
  .grid {{ grid-template-columns:1fr 1fr; }}
  h1 {{ font-size:24px; }}
  .container {{ padding:24px 13px 40px; }}
}}
</style>
</head>
<body>
<div class="container">
  <header>
    <div>
      <h1>Seguimiento · Respuesta de Acción de Tutela</h1>
      <p class="subtitle">Control de evidencias y solicitudes. Marca cada punto cuando esté gestionado y deja observaciones para hacer seguimiento.</p>
    </div>
    <div class="badge">90 preguntas</div>
  </header>

  <section class="grid">
    <div class="card"><div class="stat-label">Completadas</div><div class="stat-value" id="doneCount">0</div></div>
    <div class="card"><div class="stat-label">Pendientes</div><div class="stat-value" id="pendingCount">90</div></div>
    <div class="card"><div class="stat-label">Con responsable</div><div class="stat-value" id="assignedCount">0</div></div>
    <div class="card">
      <div class="stat-label">Progreso</div><div class="stat-value" id="progressText">0%</div>
      <div class="progress-wrap"><div class="progress" id="progressBar"></div></div>
    </div>
  </section>

  <section class="card">
    <div class="toolbar">
      <input id="search" class="search" placeholder="Buscar por número, evidencia o responsable…">
      <select id="personFilter">
        <option value="">Todos los responsables</option>
        {people_options}
        <option value="__none__">Sin responsable</option>
      </select>
      <select id="statusFilter">
        <option value="">Todos los estados</option>
        <option value="pending">Pendientes</option>
        <option value="done">Completadas</option>
      </select>
      <button id="pendingBtn">Ver pendientes</button>
      <button id="allBtn">Ver todas</button>
      <button id="clearBtn" class="danger">Restablecer</button>
    </div>
    <div class="table-head">Los cambios se guardan automáticamente en este navegador.</div>
  </section>

  <section class="card table-card" style="margin-top:16px">
    <table>
      <thead>
        <tr><th style="width:7%">N.º</th><th style="width:39%">Evidencia / solicitud</th><th style="width:16%">Responsable</th><th style="width:13%">Estado</th><th>Observaciones</th></tr>
      </thead>
      <tbody id="tbody"></tbody>
    </table>
  </section>

  <footer>Archivo independiente · los datos se almacenan localmente en el navegador (localStorage).</footer>
</div>

<script>
const STORAGE_KEY = "tutela_tracker_v1";
const initial = {records_js};
let records = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null") || initial;

function save() {{
  localStorage.setItem(STORAGE_KEY, JSON.stringify(records));
}}

function updateStats() {{
  const total = records.length;
  const done = records.filter(r => r.done).length;
  const assigned = records.filter(r => (r.person || "").trim()).length;
  const pct = total ? Math.round(done / total * 100) : 0;
  document.getElementById("doneCount").textContent = done;
  document.getElementById("pendingCount").textContent = total - done;
  document.getElementById("assignedCount").textContent = assigned;
  document.getElementById("progressText").textContent = pct + "%";
  document.getElementById("progressBar").style.width = pct + "%";
}}

function render() {{
  const q = document.getElementById("search").value.trim().toLowerCase();
  const pf = document.getElementById("personFilter").value;
  const sf = document.getElementById("statusFilter").value;
  const tbody = document.getElementById("tbody");

  const filtered = records.filter(r => {{
    const hay = `${{r.id}} ${{r.evidence}} ${{r.person}} ${{r.notes}}`.toLowerCase();
    const searchOk = !q || hay.includes(q);
    const personOk = !pf || (pf === "__none__" ? !(r.person || "").trim() : r.person === pf);
    const statusOk = !sf || (sf === "done" ? r.done : !r.done);
    return searchOk && personOk && statusOk;
  }});

  if (!filtered.length) {{
    tbody.innerHTML = '<tr><td colspan="5" class="empty">No hay elementos que coincidan con el filtro.</td></tr>';
    return;
  }}

  tbody.innerHTML = filtered.map(r => {{
    const evidence = r.evidence
      ? `<div class="evidence ${{r.evidence === "N/A" ? "n-a" : ""}}">${{escapeHtml(r.evidence)}}</div>`
      : '<div class="evidence n-a">Sin descripción registrada</div>';
    const person = r.person
      ? `<span class="person">${{escapeHtml(r.person)}}</span>`
      : '<span class="person unassigned">Sin responsable</span>';
    return `<tr class="${{r.done ? "done" : ""}}">
      <td data-label="N.º"><div class="question">${{r.id}}</div></td>
      <td data-label="Evidencia">${{evidence}}</td>
      <td data-label="Responsable">${{person}}</td>
      <td data-label="Estado">
        <label class="status ${{r.done ? "done" : "pending"}}">
          <input class="check" type="checkbox" data-id="${{r.id}}" ${{r.done ? "checked" : ""}}>
          ${{r.done ? "Completada" : "Pendiente"}}
        </label>
      </td>
      <td data-label="Observaciones">
        <textarea class="notes" data-note="${{r.id}}" placeholder="Añadir nota…">${{escapeHtml(r.notes || "")}}</textarea>
      </td>
    </tr>`;
  }}).join("");

  document.querySelectorAll(".check").forEach(el => {{
    el.addEventListener("change", e => {{
      const r = records.find(x => x.id == e.target.dataset.id);
      r.done = e.target.checked;
      save(); render(); updateStats();
    }});
  }});
  document.querySelectorAll(".notes").forEach(el => {{
    el.addEventListener("input", e => {{
      const r = records.find(x => x.id == e.target.dataset.note);
      r.notes = e.target.value;
      save(); updateStats();
    }});
  }});
}}

function escapeHtml(s) {{
  return String(s ?? "").replace(/[&<>"']/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}}[c]));
}}

["search","personFilter","statusFilter"].forEach(id => {{
  document.getElementById(id).addEventListener("input", render);
  document.getElementById(id).addEventListener("change", render);
}});

document.getElementById("pendingBtn").onclick = () => {{
  document.getElementById("statusFilter").value = "pending"; render();
}};
document.getElementById("allBtn").onclick = () => {{
  document.getElementById("statusFilter").value = ""; document.getElementById("personFilter").value = ""; render();
}};
document.getElementById("clearBtn").onclick = () => {{
  if (!confirm("¿Restablecer todas las tareas a pendientes y borrar observaciones?")) return;
  records = initial.map(r => ({{...r, done:false, notes:""}}));
  save(); render(); updateStats();
}};

updateStats();
render();
</script>
</body>
</html>"""

out = Path("/mnt/data/seguimiento_accion_tutela.html")
out.write_text(doc, encoding="utf-8")
print(f"Archivo creado: {out}")
print("Incluye 90 preguntas, responsables detectados, filtros, buscador, progreso, observaciones y guardado automático en el navegador.")
