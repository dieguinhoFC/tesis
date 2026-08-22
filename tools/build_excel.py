import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# --- HOJA 1: PICOC & Preguntas ---
ws1 = wb.active
ws1.title = "PICOC & Preguntas"
ws1.views.sheetView[0].showGridLines = True

# Formatos
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
title_font = Font(name="Calibri", size=14, bold=True, color="1F4E78")
bold_font = Font(name="Calibri", size=11, bold=True)
regular_font = Font(name="Calibri", size=11)
thin_border = Border(
    left=Side(style="thin", color="D9D9D9"),
    right=Side(style="thin", color="D9D9D9"),
    top=Side(style="thin", color="D9D9D9"),
    bottom=Side(style="thin", color="D9D9D9")
)

ws1["A1"] = "METODOLOGÍA DE REVISIÓN SISTEMÁTICA — PROTOCOLO PICOC"
ws1["A1"].font = title_font
ws1["A2"] = "Tema: Clasificación de queratocono mediante Deep Learning aplicado a mapas de rigidez corneal (Ondas de Lamb / OCE)"
ws1["A2"].font = Font(name="Calibri", size=11, italic=True)

# Tabla PICOC
headers_picoc = ["Componente PICOC", "Definición", "Aplicación en la Tesis (Diego Silvestre)"]
for col_num, h in enumerate(headers_picoc, 1):
    cell = ws1.cell(row=4, column=col_num, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

picoc_data = [
    ("P (Population)", "Población / Datos de estudio", "Pacientes (70 ojos) categorizados en 3 grupos clínicos: 1) Normales / Control, 2) Queratocono Subclínico (Forme Fruste - FFKC), y 3) Queratocono Clínico (KC I, II, III), caracterizados con Elastografía por Coherencia Óptica (OCE) y ondas de Lamb."),
    ("I (Intervention)", "Intervención / Propuesta tecnológica", "Modelos de Aprendizaje Profundo (CNNs: ResNet, EfficientNet) entrenados sobre mapas 2D de rigidez / índice STI (Speed-Thickness Index) reconstruidos a partir de la velocidad de propagación de ondas de Lamb."),
    ("C (Comparison)", "Comparación / Métodos existentes", "1) Diagnóstico geométrico topográfico/tomográfico estándar (Pentacam, OCT) que no detecta cambios subclínicos. 2) Métodos de regresión lineal escalar básica sin análisis espacial profundo. 3) Modelos clásicos de ML (SVM, Random Forest)."),
    ("O (Outcome)", "Resultados y Métricas esperadas", "Desempeño multiclase: Matriz de confusión, Exactitud (Accuracy >= 90%), Macro F1-score, AUC-ROC (>= 0.92), con alta sensibilidad específica en la detección de Queratocono Subclínico."),
    ("C (Context)", "Contexto clínico de aplicación", "Sistemas CAD en oftalmología clínica para screening previo a cirugía refractiva (pre-LASIK) para prevenir ectasias iatrogénicas y detección temprana.")
]

for row_idx, row_data in enumerate(picoc_data, 5):
    for col_idx, val in enumerate(row_data, 1):
        cell = ws1.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx == 1 else regular_font
        cell.border = thin_border
        cell.alignment = Alignment(vertical="top", wrap_text=True)

# Tabla 3 PIs
ws1.cell(row=11, column=1, value="PREGUNTAS DE INVESTIGACIÓN (ESTADO DEL ARTE - ENTREGABLE E1)").font = Font(name="Calibri", size=12, bold=True, color="1F4E78")

headers_pi = ["Código", "Tipo de Pregunta", "Pregunta de Investigación Formulada"]
for col_num, h in enumerate(headers_pi, 1):
    cell = ws1.cell(row=12, column=col_num, value=h)
    cell.fill = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

pi_data = [
    ("PI1", "Modelos y Arquitecturas (Intervención)", "¿Qué arquitecturas de redes neuronales convolucionales (ej. ResNet, EfficientNet) y técnicas de transfer learning / data augmentation ofrecen mejor desempeño para la clasificación multiclase (Normal, Subclínico y Queratocono) a partir de mapas de calor 2D médicos?"),
    ("PI2", "Biomarcadores y Rigidez (Población/Intervención)", "¿De qué manera los biomarcadores biomecánicos basados en elastografía OCE (velocidad de ondas de Lamb, índice STI y anisotropía espacial SAWS) permiten identificar alteraciones tisulares en estadios subclínicos frente a parámetros topográficos convencionales?"),
    ("PI3", "Métricas y Limitaciones (Outcome/Comparación)", "¿Qué métricas de exactitud, F1 y AUC-ROC se alcanzan en la literatura para la detección temprana de ectasias corneales y qué estrategias se utilizan para mitigar el desbalance de clases en datasets clínicos reducidos?")
]

for row_idx, row_data in enumerate(pi_data, 13):
    for col_idx, val in enumerate(row_data, 1):
        cell = ws1.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx == 1 else regular_font
        cell.border = thin_border
        cell.alignment = Alignment(vertical="top", wrap_text=True)

# Tabla Cadenas
ws1.cell(row=17, column=1, value="CADENA BOOLEANA DE BÚSQUEDA (Scopus / IEEE Xplore)").font = Font(name="Calibri", size=12, bold=True, color="1F4E78")
cadena = '("keratoconus" OR "corneal ectasia" OR "forme fruste" OR "subclinical keratoconus") AND ("deep learning" OR "convolutional neural network" OR "CNN" OR "ResNet" OR "EfficientNet") AND ("optical coherence elastography" OR "OCE" OR "Lamb wave" OR "wave speed" OR "shear wave" OR "stiffness map" OR "corneal biomechanics") AND ("classification" OR "detection" OR "early diagnosis" OR "multiclass")'
ws1.merge_cells("A18:C18")
cell_cad = ws1["A18"]
cell_cad.value = cadena
cell_cad.font = Font(name="Consolas", size=10, color="1F4E78")
cell_cad.fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
cell_cad.alignment = Alignment(vertical="center", wrap_text=True)

ws1.column_dimensions["A"].width = 22
ws1.column_dimensions["B"].width = 30
ws1.column_dimensions["C"].width = 85

# --- HOJA 2: Formulario de Extraccion (Anexo A) ---
ws2 = wb.create_sheet(title="Formulario Extracción (Anexo A)")
ws2.views.sheetView[0].showGridLines = True

headers_ext = [
    "ID", "Referencia APA (Autor, Año)", "Título del Paper", "Enfoque de Clases (Binario / 3 Clases)",
    "Modalidad / Dispositivo (OCE, Pentacam, OCT, etc.)", "Biomarcador / Entrada (Ondas Lamb, STI, SAWS, etc.)",
    "Modelo IA / Arquitectura (CNN, ResNet, SVM, etc.)", "Tamaño Dataset (# Normal / # Subclínico / # KCN)",
    "Métricas Reportadas (Accuracy, F1, AUC-ROC)", "Brechas / Limitaciones Identificadas",
    "Aporte a PI1 (Modelos)", "Aporte a PI2 (Biomarcadores)", "Aporte a PI3 (Métricas / Brechas)", "Estado / Decisión (Incluido / Excluido)"
]

for col_num, h in enumerate(headers_ext, 1):
    cell = ws2.cell(row=1, column=col_num, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

for col_idx in range(1, len(headers_ext) + 1):
    col_letter = get_column_letter(col_idx)
    ws2.column_dimensions[col_letter].width = 26

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

wb.save("papers/Referencias.xlsx")
print("Referencias.xlsx generado exitosamente con 2 pestañas.")
