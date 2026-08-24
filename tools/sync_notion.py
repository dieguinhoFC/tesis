#!/usr/bin/env python3
"""
sync_notion.py - Sincronizador de Cronograma de Tesis a Notion con soporte de Fechas Reales y Orden Secuencial.
"""

import os
import re
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

# Configurar salida UTF-8 para consola Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Cargar variables de entorno desde .env
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
if ENV_PATH.exists():
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ.setdefault(key.strip(), val.strip())

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")
NOTION_VERSION = "2022-06-28"

MONTH_MAP = {
    "ago": "08",
    "sep": "09",
    "set": "09",
    "oct": "10",
    "nov": "11",
    "dic": "12"
}

def parse_iso_date(dia_str: str, year: int = 2026):
    """Convierte texto como 'Vie 22-ago' o 'Sáb 23-ago noche' en '2026-08-22'."""
    m = re.search(r"(\d{1,2})-(\w{3})", dia_str.lower())
    if m:
        day = int(m.group(1))
        month_str = m.group(2)
        month = MONTH_MAP.get(month_str, "08")
        return f"{year}-{month}-{day:02d}"
    return None

def notion_request(endpoint: str, method: str = "GET", data: dict = None):
    url = f"https://api.notion.com/v1/{endpoint}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"[Error Notion API ({e.code})]: {e.read().decode('utf-8')}", file=sys.stderr)
        raise

def parse_cronograma_md(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    tasks = []
    week_pattern = re.compile(
        r"###\s+(SEMANA\s+\d+)\s+—\s+Sem\s+(\d+)\s+\((.*?)\)\n\*\*Objetivo\*\*:\s*(.*?)\n(.*?)(?=\n###|\n## Fechas|\Z)",
        re.DOTALL
    )
    
    order = 1
    for match in week_pattern.finditer(content):
        sem_title, sem_num, fechas, objetivo, body = match.groups()
        sem_label = f"Semana {int(sem_num):02d}"  # Formato Semana 01, Semana 02 para orden alfabético perfecto
        
        entregable = "Ninguno"
        if "ENTREGABLE E1" in body or sem_num in ["4", "5"]:
            entregable = "E1"
        elif "ENTREGABLE E2" in body or sem_num in ["8", "9"]:
            entregable = "E2"
        elif "ENTREGABLE E3" in body or sem_num in ["13", "14"]:
            entregable = "E3"
        elif sem_num in ["1", "2"]:
            entregable = "Cronograma"

        # Parsear líneas de checklist: - [ ] **Vie 22-ago (2h)**: Descripción
        checkbox_items = re.findall(r"-\s*\[([ xX])\]\s*\*\*(.*?)\s*\((\d+(?:-\d+)?h)\)\*\*:\s*(.*)", body)
        
        for check, dia_str, horas_str, actividad in checkbox_items:
            horas_match = re.search(r"(\d+)", horas_str)
            horas = int(horas_match.group(1)) if horas_match else 2
            iso_date = parse_iso_date(dia_str)
            
            tasks.append({
                "orden": order,
                "semana": sem_label,
                "dia": dia_str.strip(),
                "fecha_iso": iso_date,
                "actividad": actividad.strip(),
                "horas": horas,
                "estado": "Completado" if check.lower() == "x" else "Por hacer",
                "objetivo": objetivo.strip(),
                "entregable": entregable
            })
            order += 1
            
    return tasks

def create_notion_database(parent_page_id: str):
    page_id = parent_page_id.replace("-", "")
    
    db_schema = {
        "parent": {"type": "page_id", "page_id": page_id},
        "title": [
            {
                "type": "text",
                "text": {"content": "📊 Cronograma de Tesis 1 (1INF42-2026-2)"}
            }
        ],
        "properties": {
            "Tarea": {"title": {}},
            "Fecha": {"date": {}},
            "Semana": {
                "select": {
                    "options": [
                        {"name": f"Semana {i:02d}", "color": "blue"} for i in range(1, 15)
                    ]
                }
            },
            "Día": {"rich_text": {}},
            "Horas Estimadas": {"number": {"format": "number"}},
            "Estado": {
                "status": {
                    "options": [
                        {"name": "Por hacer", "color": "default"},
                        {"name": "En progreso", "color": "yellow"},
                        {"name": "Completado", "color": "green"}
                    ]
                }
            },
            "Entregable": {
                "select": {
                    "options": [
                        {"name": "Cronograma", "color": "gray"},
                        {"name": "E1", "color": "orange"},
                        {"name": "E2", "color": "purple"},
                        {"name": "E3", "color": "red"},
                        {"name": "Ninguno", "color": "default"}
                    ]
                }
            },
            "Orden": {"number": {"format": "number"}},
            "Objetivo Semanal": {"rich_text": {}}
        }
    }
    
    res = notion_request("databases", method="POST", data=db_schema)
    print(f"✅ Base de datos creada con ID: {res['id']}")
    return res["id"]

def populate_database(database_id: str, tasks: list):
    total = len(tasks)
    print(f"🚀 Insertando {total} tareas con fechas ISO y orden numérico en Notion...")
    
    for i, t in enumerate(tasks, start=1):
        props = {
            "Tarea": {
                "title": [{"text": {"content": t["actividad"]}}]
            },
            "Orden": {
                "number": t["orden"]
            },
            "Semana": {
                "select": {"name": t["semana"]}
            },
            "Día": {
                "rich_text": [{"text": {"content": t["dia"]}}]
            },
            "Horas Estimadas": {
                "number": t["horas"]
            },
            "Estado": {
                "status": {"name": t["estado"]}
            },
            "Entregable": {
                "select": {"name": t["entregable"]}
            },
            "Objetivo Semanal": {
                "rich_text": [{"text": {"content": t["objetivo"][:2000]}}]
            }
        }
        
        if t["fecha_iso"]:
            props["Fecha"] = {"date": {"start": t["fecha_iso"]}}
            
        page_payload = {
            "parent": {"database_id": database_id},
            "properties": props
        }
        notion_request("pages", method="POST", data=page_payload)
        print(f"  [{i}/{total}] ✅ {t['semana']} | {t['fecha_iso']} | {t['dia']}: {t['actividad'][:35]}...")

def clear_database_items(database_id: str):
    """Archiva elementos anteriores para evitar duplicados al re-sincronizar."""
    query_res = notion_request(f"databases/{database_id}/query", method="POST", data={"page_size": 100})
    results = query_res.get("results", [])
    if results:
        print(f"🧹 Limpiando {len(results)} tareas anteriores de la base de datos existente...")
        for page in results:
            notion_request(f"pages/{page['id']}", method="PATCH", data={"archived": True})

def update_env_db_id(new_db_id: str):
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if env_file.exists():
        content = env_file.read_text(encoding="utf-8")
        if "NOTION_DATABASE_ID=" in content:
            content = re.sub(r"NOTION_DATABASE_ID=.*", f"NOTION_DATABASE_ID={new_db_id}", content)
        else:
            content += f"\nNOTION_DATABASE_ID={new_db_id}\n"
        env_file.write_text(content, encoding="utf-8")

def main():
    if not NOTION_API_KEY or not NOTION_PAGE_ID:
        print("\n❌ Error: NOTION_API_KEY o NOTION_PAGE_ID no configurados en .env\n")
        sys.exit(1)
        
    cronograma_path = Path(__file__).resolve().parent.parent / "docs" / "cronogramas" / "Cronograma-diego-silvestre.md"
    if not cronograma_path.exists():
        print(f"❌ No se encontró {cronograma_path}")
        sys.exit(1)
        
    tasks = parse_cronograma_md(cronograma_path)
    print(f"📋 Se encontraron {len(tasks)} actividades en el cronograma.")
    
    db_id = os.getenv("NOTION_DATABASE_ID")
    db_ready = False
    
    if db_id:
        try:
            print(f"🔄 Verificando base de datos existente en Notion (ID: {db_id})...")
            clear_database_items(db_id)
            db_ready = True
        except Exception as e:
            print(f"⚠️ Base de datos anterior no accesible ({e}). Creando una nueva base de datos...")
            db_ready = False
            
    if not db_ready:
        db_id = create_notion_database(NOTION_PAGE_ID)
        update_env_db_id(db_id)
        print(f"💡 Guardado en tu .env: NOTION_DATABASE_ID={db_id}")
        
    populate_database(db_id, tasks)
    
    print("\n🎉 ¡Sincronización completada con éxito en Notion!")
    print("👉 En Notion ahora puedes ordenar por 'Fecha' (Ascendente) o 'Orden' (1, 2, 3...) y activar vista Calendario / Chart.")

if __name__ == "__main__":
    main()

