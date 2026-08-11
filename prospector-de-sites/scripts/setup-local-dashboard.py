#!/usr/bin/env python3
"""Inicializa o dashboard local e importa o CSV de leads sem apagar dados."""
import csv, json, re, shutil, sqlite3
from datetime import datetime
from pathlib import Path

ROOT = Path.cwd()
PLUGIN = ROOT / "fork-kvm2" / "prospector-de-sites"
DB = ROOT / "prospector.db"
CSV_FILE = ROOT / "leads_prospector_SP.csv"
TEMPLATE = PLUGIN / "skills" / "dashboard-leads" / "references" / "dashboard-template.html"
COLUMNS = ["slug", "nome", "nicho", "cidade", "nota", "avaliacoes", "email", "telefone", "whatsapp", "siteAntigo", "motivo", "status", "urlNova", "dataProposta", "valor", "obs", "contratoStatus", "contratoEm", "manutencao", "pago", "docCliente", "endCliente"]

def clean(value):
    value = (value or "").strip()
    return "" if value in {"—", "-", "–"} else value

def slugify(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower().encode("ascii", "ignore").decode()).strip("-") or "lead"

def normalize_status(value):
    value = clean(value).lower()
    if "descart" in value: return "descartado"
    if "proposta" in value: return "proposta"
    if "redesign" in value: return "redesenhado"
    if "public" in value: return "publicado"
    return "novo"

def number(value, integer=False):
    value = clean(value).replace(".", "").replace(",", ".")
    if not value: return None
    try: return int(float(value)) if integer else float(value)
    except ValueError: return None

def row_from_csv(row):
    nome = clean(row.get("Nome")); raw_status = clean(row.get("Status")); date = ""
    match = re.search(r"(\d{2}/\d{2}/\d{4})", raw_status)
    if match: date = datetime.strptime(match.group(1), "%d/%m/%Y").date().isoformat()
    return {"slug": slugify(nome), "nome": nome, "nicho": clean(row.get("Nicho")), "cidade": clean(row.get("Cidade")), "nota": number(row.get("Nota")), "avaliacoes": number(row.get("Avaliações"), True), "email": clean(row.get("E-mail")), "telefone": clean(row.get("Telefone")), "whatsapp": "", "siteAntigo": clean(row.get("Site atual")), "motivo": clean(row.get("Motivo")), "status": normalize_status(raw_status), "urlNova": clean(row.get("URL nova")), "dataProposta": date, "valor": None, "obs": clean(row.get("Situação")), "contratoStatus": "pendente", "contratoEm": "", "manutencao": None, "pago": 0, "docCliente": "", "endCliente": ""}

def main():
    if DB.exists():
        backup = DB.with_suffix(f".db.bak-{datetime.now():%Y%m%d-%H%M%S}")
        shutil.copy2(DB, backup); print(f"Backup criado: {backup}")
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS leads (slug TEXT PRIMARY KEY, nome TEXT, nicho TEXT, cidade TEXT, nota REAL, avaliacoes INTEGER, email TEXT, telefone TEXT, whatsapp TEXT, siteAntigo TEXT, motivo TEXT, status TEXT DEFAULT 'novo', urlNova TEXT, dataProposta TEXT, valor REAL, obs TEXT, contratoStatus TEXT DEFAULT 'pendente', contratoEm TEXT, manutencao REAL, pago INTEGER DEFAULT 0, docCliente TEXT, endCliente TEXT, atualizado TEXT DEFAULT (datetime('now','localtime')))" )
    imported = 0
    if CSV_FILE.exists():
        with CSV_FILE.open(encoding="utf-8-sig", newline="") as handle:
            for source in csv.DictReader(handle):
                lead = row_from_csv(source)
                if not lead["nome"]: continue
                marks = ",".join("?" for _ in COLUMNS); updates = ",".join(f"{c}=excluded.{c}" for c in COLUMNS if c != "slug")
                conn.execute(f"INSERT INTO leads ({','.join(COLUMNS)}) VALUES ({marks}) ON CONFLICT(slug) DO UPDATE SET {updates}, atualizado=datetime('now','localtime')", [lead[c] for c in COLUMNS]); imported += 1
    conn.commit(); rows = [dict(zip(COLUMNS, row)) for row in conn.execute(f"SELECT {','.join(COLUMNS)} FROM leads ORDER BY nome")]; conn.close()
    payload = {"atualizado": datetime.now().isoformat(timespec="seconds"), "leads": rows}
    (ROOT / "dashboard.html").write_text(TEMPLATE.read_text(encoding="utf-8").replace("__DADOS__", json.dumps(payload, ensure_ascii=False)), encoding="utf-8")
    shutil.copy2(PLUGIN / "skills/dashboard-leads/references/dashboard-server.py", ROOT / "dashboard-server.py")
    shutil.copy2(PLUGIN / "skills/dashboard-leads/references/iniciar-dashboard.bat", ROOT / "iniciar-dashboard.bat")
    shutil.copy2(PLUGIN / "manual.html", ROOT / "manual.html")
    print(f"Dashboard pronto: {imported} registros importados em {DB}")

if __name__ == "__main__": main()
