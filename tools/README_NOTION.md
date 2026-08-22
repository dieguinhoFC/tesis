# 🚀 Integración del Cronograma de Tesis con Notion + CLI + IA

Este proyecto te permite llevar el control de tu cronograma de tesis tanto desde tu **celular/navegador (Notion)** como desde tu **terminal (CLI)** o **chat del IDE (con IA / Groq)**.

---

## 🛠️ Configuración Inicial (Solo 2 minutos)

### Paso 1: Obtener tu Token Gratuito de Notion
1. Ingresa a [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) con tu cuenta de Notion.
2. Haz clic en **"+ New integration"**.
3. Nómbrala por ejemplo: `Tesis Assistant` y dale a **Save**.
4. Copia el **Internal Integration Secret** (empieza con `ntn_...`).

### Paso 2: Crear la página en Notion y darle acceso
1. En Notion, crea una nueva página en blanco llamada: `🎓 Tesis 1 - Clasificación Queratocono`.
2. Haz clic en los **tres puntos `...`** (arriba a la derecha de la página) ➔ **Connect to / Conectar a** ➔ Selecciona `Tesis Assistant`.
3. Copia el **Page ID** de la URL de tu página:
   * Ejemplo de URL: `https://www.notion.so/mi-espacio/Tesis-1-Clasificacion-Queratocono-1a2b3c4d5e6f7g8h9i0j...`
   * El Page ID son los últimos 32 caracteres (`1a2b3c4d5e6f7g8h9i0j...`).

### Paso 3: Configurar tu archivo `.env`
Copia el archivo [.env.example](file:///F:/Proyectos/ProyectoTesis/.env.example) a `.env`:
```env
NOTION_API_KEY=ntn_tu_token_aqui
NOTION_PAGE_ID=tu_page_id_aqui
GROQ_API_KEY=gsk_tu_clave_groq_aqui (Opcional, gratis en https://console.groq.com)
```

---

## 📥 1. Sincronizar Cronograma inicial a Notion

Ejecuta el script para importar automáticamente todas las tareas, semanas y objetivos de [Cronograma-diego-silvestre.md](file:///F:/Proyectos/ProyectoTesis/Cronograma-diego-silvestre.md) a Notion:

```bash
python scripts/sync_notion.py
```

*Esto creará en tu página de Notion una base de datos interactiva con propiedades de Estado (`Por hacer`, `En progreso`, `Completado`), Entregables (`E1`, `E2`, `E3`), Horas estimadas y vista de Calendario/Kanban.*

---

## 💻 2. Uso del CLI (`tesis_cli.py`)

No necesitas instalar librerías pesadas (utiliza la librería estándar de Python).

### Ver estado general en tiempo real (desde la nube de Notion):
```bash
python tools/tesis_cli.py status
```

### Descargar cambios de Notion a tu Markdown local (para hacer Git commit):
```bash
python tools/tesis_cli.py pull
```

### Subir cambios marcados en el Markdown local hacia Notion:
```bash
python tools/tesis_cli.py push
```

### Ver tareas de una semana específica:
```bash
python tools/tesis_cli.py list --week 1
```

### Marcar una tarea como completada desde la terminal:
```bash
python tools/tesis_cli.py done --week 1 --item 1
```

### Preguntarle a la IA (Groq / Llama 3.3):
```bash
python tools/tesis_cli.py ask "¿Qué entregables tengo que enviar en octubre y a quién?"
```

---

## 📱 3. Uso desde el Celular / Tablet

Simplemente abre la app de **Notion** en tu móvil:
* Verás la base de datos sincronizada.
* Puedes cambiar la vista a **Board (Tablero Kanban)** para arrastrar tareas o vista **Calendar** para ver fechas clave.
* Cualquier cambio que hagas en el celular se reflejará inmediatamente en el CLI y en el IDE.
