#!/usr/bin/env python3
"""
enhance_notion_page.py - Convierte la página principal de Notion en un Dashboard completo de Tesis.
Agrega encabezados, banner de reglas del curso, fechas críticas y enlaces.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

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
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")
NOTION_VERSION = "2022-06-28"

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
        print(f"[Error Notion API]: {e.read().decode('utf-8')}", file=sys.stderr)
        raise

def add_dashboard_blocks(page_id: str):
    clean_page_id = page_id.replace("-", "")
    
    blocks = [
        # Callout resumen
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "🎯 Tema: Clasificación de queratocono mediante Deep Learning en mapas de rigidez corneal reconstruidos por biomarcadores de velocidad de onda.\n"
                                       "⏱️ Disponibilidad: 6-8 h/semana (Viernes ~2h | Sábado noche ~2h | Domingo ~3-4h)"
                        }
                    }
                ],
                "icon": {"emoji": "🎓"},
                "color": "blue_background"
            }
        },
        # Encabezado Fechas Críticas
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🚨 Fechas Críticas de Entrega (1INF42)"}}]
            }
        },
        # Callout Fechas E1, E2, E3
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "• Vie 22-ago: Enviar Cronograma al Asesor\n"
                                       "• Vie 12-sep (mediodía): Entrega E1 (Problemática, Estado del arte, Objetivos, IOV)\n"
                                       "• Jue 09-oct (mediodía): Entrega E2 (Marcos teórico/legal, Herramientas, Métodos)\n"
                                       "• Vie 14-nov (mediodía): Entrega E3 (Documento completo + Plan + Avance de Resultado)\n"
                                       "• 30-nov al 13-dic: Exposiciones Finales ante el Jurado"
                        }
                    }
                ],
                "icon": {"emoji": "📅"},
                "color": "yellow_background"
            }
        },
        # Encabezado Reglas Clave
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "⚠️ Reglas de Oro del Curso"}}]
            }
        },
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"type": "text", "text": {"content": "Todo entregable debe tener visto bueno del asesor antes de enviarse al profesor o jurado (Sin VB = Nota 00)."}}]
            }
        },
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"type": "text", "text": {"content": "Cada nuevo entregable debe incluir las correcciones del anterior levantadas."}}]
            }
        },
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"type": "text", "text": {"content": "El Formulario de extracción de artículos siempre se adjunta como Anexo A a partir del E1."}}]
            }
        },
        # Divisor
        {"object": "block", "type": "divider", "divider": {}},
        # Encabezado Tareas
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "📋 Tablero y Gestión de Avances"}}]
            }
        }
    ]
    
    print(f"Agregando bloques de resumen a la página principal {clean_page_id}...")
    notion_request(f"blocks/{clean_page_id}/children", method="PATCH", data={"children": blocks})
    print("✅ Dashboard decorado con éxito.")

if __name__ == "__main__":
    if not NOTION_API_KEY or not NOTION_PAGE_ID:
        print("❌ Faltan credenciales en .env")
        sys.exit(1)
    add_dashboard_blocks(NOTION_PAGE_ID)
