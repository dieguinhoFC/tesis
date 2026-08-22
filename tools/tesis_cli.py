#!/usr/bin/env python3
"""
tesis_cli.py - Interfaz de línea de comandos para consultar y actualizar el avance de tesis en Notion.
Soporta consultas directas y preguntas en lenguaje natural usando Groq (Llama 3.3).
"""

import os
import re
import sys
import json
import argparse
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

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
if ENV_PATH.exists():
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ.setdefault(key.strip(), val.strip())

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NOTION_VERSION = "2022-06-28"

def notion_api(endpoint: str, method: str = "GET", data: dict = None):
    if not NOTION_API_KEY:
        print("❌ Error: NOTION_API_KEY no encontrada en .env", file=sys.stderr)
        sys.exit(1)
        
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
        print(f"[Error Notion API]: {e.read().decode('utf-8')}", file=sys.stderr)
        sys.exit(1)

def query_groq(prompt: str, context: str):
    """Consulta al modelo gratuito Llama 3.3 de Groq."""
    if not GROQ_API_KEY:
        return "⚠️ GROQ_API_KEY no configurada en .env. Agrega tu clave gratuita de https://console.groq.com para respuestas con IA."
        
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    system_prompt = (
        "Eres el asistente de gestión de tesis de Diego. Ayudas a dar seguimiento al cronograma, entregables (E1, E2, E3), "
        "tiempos estimados y estado de tareas. Sé conciso, claro y directo."
    )
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": f"{system_prompt}\n\nContexto actual de la base de datos de tareas:\n{context}"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 600
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            return res["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error al consultar Groq: {e}"

def find_thesis_database():
    """Busca la base de datos de tesis si NOTION_DATABASE_ID no está explícitamente en .env."""
    global NOTION_DATABASE_ID
    if NOTION_DATABASE_ID:
        return NOTION_DATABASE_ID
        
    search_res = notion_api("search", method="POST", data={"filter": {"value": "database", "property": "object"}})
    for result in search_res.get("results", []):
        title_objs = result.get("title", [])
        title = "".join(t.get("plain_text", "") for t in title_objs)
        if "Cronograma de Tesis" in title or "Tesis" in title:
            NOTION_DATABASE_ID = result["id"]
            return NOTION_DATABASE_ID
            
    print("❌ No se encontró la base de datos de la Tesis en Notion. Ejecuta primero 'python scripts/sync_notion.py'.")
    sys.exit(1)

def get_all_tasks():
    db_id = find_thesis_database()
    results = []
    has_more = True
    cursor = None
    
    while has_more:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        resp = notion_api(f"databases/{db_id}/query", method="POST", data=body)
        results.extend(resp.get("results", []))
        has_more = resp.get("has_more", False)
        cursor = resp.get("next_cursor")
        
    parsed = []
    for r in results:
        props = r.get("properties", {})
        
        # Tarea
        title_objs = props.get("Tarea", {}).get("title", [])
        tarea = "".join(t.get("plain_text", "") for t in title_objs)
        
        # Semana
        semana_obj = props.get("Semana", {}).get("select") or {}
        semana = semana_obj.get("name", "Semana ?")
        
        # Día
        dia_objs = props.get("Día", {}).get("rich_text", [])
        dia = "".join(t.get("plain_text", "") for t in dia_objs)
        
        # Horas
        horas = props.get("Horas Estimadas", {}).get("number", 0)
        
        # Estado
        estado_obj = props.get("Estado", {}).get("status") or {}
        estado = estado_obj.get("name", "Por hacer")
        
        # Entregable
        ent_obj = props.get("Entregable", {}).get("select") or {}
        entregable = ent_obj.get("name", "Ninguno")

        parsed.append({
            "id": r["id"],
            "tarea": tarea,
            "semana": semana,
            "dia": dia,
            "horas": horas,
            "estado": estado,
            "entregable": entregable
        })
        
    # Ordenar por semana y día
    def sort_key(x):
        import re
        m = re.search(r"\d+", x["semana"])
        return int(m.group(0)) if m else 99
        
    parsed.sort(key=sort_key)
    return parsed

def show_status():
    tasks = get_all_tasks()
    total = len(tasks)
    completadas = [t for t in tasks if t["estado"] == "Completado"]
    en_progreso = [t for t in tasks if t["estado"] == "En progreso"]
    pendientes = [t for t in tasks if t["estado"] == "Por hacer"]
    
    pct = (len(completadas) / total * 100) if total > 0 else 0
    bar_len = 25
    filled = int(bar_len * pct / 100)
    bar = "█" * filled + "░" * (bar_len - filled)
    
    print("\n" + "=" * 55)
    print(" 🎓 ESTADO DEL CRONOGRAMA DE TESIS (1INF42)")
    print("=" * 55)
    print(f" Progreso general: [{bar}] {pct:.1f}% ({len(completadas)}/{total} tareas)")
    print(f" • Completadas: {len(completadas)} | En progreso: {len(en_progreso)} | Pendientes: {len(pendientes)}")
    print("-" * 55)
    
    # Mostrar resumen por semanas
    semanas = sorted(list(set(t["semana"] for t in tasks)), key=lambda s: int(s.replace("Semana ", "") if "Semana " in s else 99))
    
    for s in semanas:
        s_tasks = [t for t in tasks if t["semana"] == s]
        s_comp = len([t for t in s_tasks if t["estado"] == "Completado"])
        s_tot = len(s_tasks)
        check = "✅" if s_comp == s_tot and s_tot > 0 else ("⏳" if s_comp > 0 else "⬜")
        
        ent = next((t["entregable"] for t in s_tasks if t["entregable"] not in ["Ninguno", "None"]), None)
        ent_str = f" [📦 Hito: {ent}]" if ent else ""
        print(f" {check} {s:<10} ({s_comp}/{s_tot} tareas){ent_str}")
        
    print("=" * 55)
    print("💡 Usa 'python tesis_cli.py list --week <num>' para ver detalle.")
    print("💡 Usa 'python tesis_cli.py ask \"<pregunta>\"' para consultar con IA.\n")

def list_week(week_num: int):
    tasks = get_all_tasks()
    target_sem = f"Semana {week_num}"
    week_tasks = [t for t in tasks if t["semana"] == target_sem]
    
    if not week_tasks:
        print(f"❌ No se encontraron tareas para {target_sem}.")
        return
        
    print(f"\n📋 TAREAS DE {target_sem.upper()}:")
    print("-" * 65)
    for idx, t in enumerate(week_tasks, start=1):
        icon = "✅" if t["estado"] == "Completado" else ("🔄" if t["estado"] == "En progreso" else "⬜")
        print(f" [{idx}] {icon} {t['dia']:<16} ({t['horas']}h) - {t['tarea']}")
    print("-" * 65)
    print("💡 Para marcar como hecha: 'python tesis_cli.py done --week <num> --item <index>'\n")

def mark_done(week_num: int, item_idx: int):
    tasks = get_all_tasks()
    target_sem = f"Semana {week_num}"
    week_tasks = [t for t in tasks if t["semana"] == target_sem]
    
    if item_idx < 1 or item_idx > len(week_tasks):
        print(f"❌ Índice inválido. Debe estar entre 1 y {len(week_tasks)}.")
        return
        
    target_task = week_tasks[item_idx - 1]
    page_id = target_task["id"]
    
    notion_api(f"pages/{page_id}", method="PATCH", data={
        "properties": {
            "Estado": {"status": {"name": "Completado"}}
        }
    })
    print(f"✅ ¡Tarea actualizada a Completado en Notion!: {target_task['tarea']}")

def pull_from_notion():
    """Descarga el estado de Notion y actualiza los checkboxes en Cronograma-diego-silvestre.md."""
    md_path = Path(__file__).resolve().parent.parent / "docs" / "cronogramas" / "Cronograma-diego-silvestre.md"
    if not md_path.exists():
        print(f"❌ No se encontró el archivo {md_path}")
        return
        
    print("📥 Descargando estado de tareas desde Notion...")
    tasks = get_all_tasks()
    completed_tasks = {t["tarea"].strip().lower() for t in tasks if t["estado"] == "Completado"}
    
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    updated_lines = []
    changes = 0
    
    for line in lines:
        match = re.match(r"^(\s*-\s*\[)([\sxX])(\]\s*\*\*.*?\*\*:\s*)(.*)$", line)
        if match:
            prefix, current_check, middle, task_desc = match.groups()
            task_desc_clean = task_desc.strip().lower()
            
            # Buscar si coincide con alguna tarea completada
            is_done = any(t in task_desc_clean or task_desc_clean in t for t in completed_tasks)
            new_check = "x" if is_done else " "
            
            if new_check != current_check:
                changes += 1
                line = f"{prefix}{new_check}{middle}{task_desc}\n"
                
        updated_lines.append(line)
        
    with open(md_path, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)
        
    print(f"✅ Markdown local actualizado ({changes} cambios sincronizados). Listo para git commit.")

def push_to_notion():
    """Lee los checkboxes [x] del Markdown local y los actualiza en Notion."""
    md_path = Path(__file__).resolve().parent.parent / "docs" / "cronogramas" / "Cronograma-diego-silvestre.md"
    if not md_path.exists():
        print(f"❌ No se encontró el archivo {md_path}")
        return
        
    print("📤 Leyendo checkboxes locales de Cronograma-diego-silvestre.md...")
    tasks = get_all_tasks()
    
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    checked_tasks = []
    for match in re.finditer(r"-\s*\[([xX])\]\s*\*\*.*?\*\*:\s*(.*)", content):
        checked_tasks.append(match.group(2).strip().lower())
        
    updated = 0
    for t in tasks:
        t_clean = t["tarea"].strip().lower()
        should_be_done = any(c in t_clean or t_clean in c for c in checked_tasks)
        
        if should_be_done and t["estado"] != "Completado":
            notion_api(f"pages/{t['id']}", method="PATCH", data={
                "properties": {"Estado": {"status": {"name": "Completado"}}}
            })
            print(f"  ✅ Marcado en Notion: {t['tarea'][:40]}...")
            updated += 1
            
    print(f"✅ Sincronización a Notion completada ({updated} tareas actualizadas).")

def ask_assistant(question: str):
    print(f"🤖 Consultando a Groq (Llama 3.3) sobre tu tesis...\n")
    tasks = get_all_tasks()
    
    # Resumen estructurado para contexto del LLM
    context_lines = []
    for t in tasks:
        context_lines.append(f"- [{t['estado']}] {t['semana']} | {t['dia']} ({t['horas']}h) | Hito: {t['entregable']} | Tarea: {t['tarea']}")
    context = "\n".join(context_lines)
    
    response = query_groq(question, context)
    print(response)

def main():
    parser = argparse.ArgumentParser(description="CLI de Control y Seguimiento de Tesis")
    subparsers = parser.add_subparsers(dest="command")
    
    # status
    subparsers.add_parser("status", help="Muestra el resumen visual del progreso de la tesis en tiempo real")
    
    # list
    list_p = subparsers.add_parser("list", help="Lista tareas de una semana")
    list_p.add_argument("--week", type=int, required=True, help="Número de semana (1-14)")
    
    # done
    done_p = subparsers.add_parser("done", help="Marca una tarea como completada")
    done_p.add_argument("--week", type=int, required=True, help="Número de semana")
    done_p.add_argument("--item", type=int, required=True, help="Número de ítem de la lista")
    
    # pull
    subparsers.add_parser("pull", help="Descarga el estado desde Notion y marca las casillas [x] en el Markdown local")
    
    # push
    subparsers.add_parser("push", help="Lee las casillas [x] del Markdown local y las sincroniza hacia Notion")
    
    # ask
    ask_p = subparsers.add_parser("ask", help="Pregunta cualquier duda sobre tu cronograma con IA")
    ask_p.add_argument("question", type=str, help="Tu consulta en lenguaje natural")
    
    args = parser.parse_args()
    
    if args.command == "status" or not args.command:
        show_status()
    elif args.command == "list":
        list_week(args.week)
    elif args.command == "done":
        mark_done(args.week, args.item)
    elif args.command == "pull":
        pull_from_notion()
    elif args.command == "push":
        push_to_notion()
    elif args.command == "ask":
        ask_assistant(args.question)

if __name__ == "__main__":
    main()

