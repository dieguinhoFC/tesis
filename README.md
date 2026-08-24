# 🎓 Proyecto de Fin de Carrera (Tesis) — 1INF42-2026-2

**Tema**: Clasificación de queratocono mediante modelos de aprendizaje profundo aplicados a mapas de rigidez corneal reconstruidos a partir de biomarcadores de velocidad de onda  
**Estudiante**: Diego Silvestre  
**Asesor**: Dr. César Beltrán Castañón  
**Co-asesor**: Dr. José Fernando Zvietcovich Zegarra (Grupo de Biofotónica / OCE)  

---

## 📁 Estructura del Proyecto

```text
ProyectoTesis/
│
├── docs/                             # Documentación de la tesis
│   ├── Descripcion-Proyecto-Tesis.md # Documento Maestro: PICOC, Estado del Arte y Metodología
│   ├── E1-Borrador-Entregable1.md    # Borrador Formal del Entregable 1 (E1)
│   ├── cronogramas/                  # Cronogramas y planificaciones
│   │   ├── Cronograma-diego-silvestre.md
│   │   ├── Cronograma-diego-silvestre.html
│   │   └── Cronograma-Curso.md
│   ├── normativa_pucp/               # Guías, rúbricas y plantillas oficiales
│   │   ├── 1INF42-2026-2-Cronograma.pdf
│   │   ├── ProyectoFinCarrera_v3.0.docx
│   │   ├── Tesis1.md
│   │   └── Checklist-Rubrica-PUCP.md
│   ├── notas/                        # Guías y notas técnicas de soporte
│   │   └── Guia-Preguntas-Asesor-Biofotonica.md
│   └── referencias/                  # Capturas y diapositivas de referencia del laboratorio
│
├── papers/                           # Estado del arte y literatura científica
│   ├── Referencias.xlsx              # Formulario de extracción de artículos (Anexo A)
│   ├── ris/                          # Exportaciones bibliográficas brutas (PRISMA)
│   │   ├── SCOPUS_EXPORTADO_21-0802026.ris  # 84 artículos de Scopus
│   │   └── IEEE_Xplore_2026.ris             # 17 artículos de IEEE Xplore
│   └── pdfs/                         # Artículos científicos descargados
│
├── tools/                            # Herramientas de seguimiento y automatización
│   ├── sync_notion.py                # Sincronizador Markdown -> Notion
│   ├── tesis_cli.py                  # CLI interactivo con IA (Groq / Llama 3.3)
│   └── README_NOTION.md              # Guía de configuración Notion / CLI
│
├── src/                              # Código fuente del modelo (Deep Learning)
│   ├── data/                         # Preprocesamiento y mapas de rigidez corneal
│   └── models/                       # Arquitecturas CNN (ResNet, EfficientNet) y evaluación
│
├── .env.example                      # Plantilla de variables de entorno
└── .gitignore                        # Archivos ignorados por Git
```

---

## ⚡ Comandos Rápidos del CLI

Para gestionar y consultar el cronograma de tareas en Notion:

```bash
# Ver estado general y porcentaje de avance
python tools/tesis_cli.py status

# Ver tareas de la semana actual
python tools/tesis_cli.py list --week 1

# Marcar una tarea como completada
python tools/tesis_cli.py done --week 1 --item 1

# Consultar con IA gratuita (Groq / Llama 3.3)
python tools/tesis_cli.py ask "¿Qué entregable tengo la próxima semana?"
```

*(Consulta [`tools/README_NOTION.md`](file:///F:/Proyectos/ProyectoTesis/tools/README_NOTION.md) para más detalles sobre la sincronización).*
