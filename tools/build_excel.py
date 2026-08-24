import os
import re
import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

def parse_and_rank_ris(filepath, source_label, id_prefix):
    papers = []
    if not os.path.exists(filepath):
        print(f"Advertencia: No se encontró {filepath}")
        return papers
        
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    entries = [e for e in content.split('ER  -') if e.strip()]
    
    for idx, e in enumerate(entries, 1):
        t_m = re.search(r'(?:TI|T1)\s+-\s+(.+)', e)
        y_m = re.search(r'(?:PY|Y1|DA)\s+-\s+(\d{4})', e)
        a_m = re.findall(r'(?:AU|A1)\s+-\s+(.+)', e)
        ab_m = re.search(r'(?:AB|N2)\s+-\s+(.+)', e, re.DOTALL)
        doi_m = re.search(r'(?:DO)\s+-\s+(.+)', e)
        j_m = re.search(r'(?:JO|JF|T2|JA)\s+-\s+(.+)', e)
        
        title = t_m.group(1).strip() if t_m else 'Sin título'
        title = re.sub(r'\s+', ' ', title)
        year = y_m.group(1).strip() if y_m else 'N/A'
        authors = [a.strip() for a in a_m]
        first_author = authors[0] if authors else 'Anon'
        ab = ab_m.group(1).strip() if ab_m else 'Sin resumen disponible'
        ab = re.sub(r'\s+', ' ', ab)
        doi = doi_m.group(1).strip() if doi_m else ''
        journal = j_m.group(1).strip() if j_m else 'N/A'
        journal = re.sub(r'\s+', ' ', journal)
        
        txt = (title + ' ' + ab).lower()
        
        # 1. Detección de Exclusiones Claras (EC)
        is_retracted = 'retracted:' in txt
        is_editorial_narrative = any(k in txt for k in ['narrative review', 'letter to editor', 'bibliometric analysis'])
        is_pure_surgery = any(k in txt for k in [
            'cross-linking surgery outcomes', 'predicting outcome of treatment',
            'swimming goggle', 'turner syndrome', 'cytokine profile',
            'transcriptomic', 'intracorneal ring', 'corneoscleral morphology',
            'deep anterior lamellar keratoplasty', 'penetrating keratoplasty outcome'
        ])
        has_ai = any(k in txt for k in ['machine learning', 'deep learning', 'cnn', 'neural network', 'artificial intelligence', 'svm', 'random forest', 'xgboost', 'resnet', 'efficientnet', 'transformer', 'classifier', 'classification', 'detection', 'screening', 'diagnos'])
        
        # 2. Scoring de Relevancia
        score = 0
        has_subclinical = any(k in txt for k in ['subclinical', 'forme fruste', 'early', 'suspect', 'incipient', 'pre-clinical'])
        has_biomech = any(k in txt for k in ['elastography', 'oce', 'lamb wave', 'shear wave', 'stiffness', 'biomechanic', 'elasticity', 'corvis', 'tbi', 'cbi', 'raw data'])
        has_deep_learning = any(k in txt for k in ['deep learning', 'cnn', 'resnet', 'efficientnet', 'convolutional', 'transfer learning', 'vgg', 'densenet'])
        has_validation = any(k in txt for k in ['cross-validation', 'k-fold', 'group', 'patient', 'leakage', 'auc', 'f1-score', 'sensitivity', 'specificity'])
        
        if has_subclinical: score += 4
        if has_biomech: score += 5
        if has_deep_learning: score += 4
        if has_validation: score += 2
        
        # 3. Clasificación Automática y Asignación de PI
        if is_retracted or is_editorial_narrative:
            priority = "BAJA (Descartar)"
            status = "Excluido en Cribado"
            ec = "EC4 (Editorial/Narrativa)"
            pi_tag = "Ninguno"
        elif is_pure_surgery or not has_ai:
            priority = "BAJA (Descartar)"
            status = "Excluido en Cribado"
            ec = "EC2 (Sin IA / Quirúrgico puro)"
            pi_tag = "Ninguno"
        elif score >= 8:
            priority = "ALTA (Candidato Principal)"
            status = "Pasa a Elegibilidad"
            ec = "-"
            if has_biomech and has_subclinical:
                pi_tag = "PI2 + PI3 (Rigidez y Detección Subclínica)"
            elif has_deep_learning:
                pi_tag = "PI1 + PI3 (Deep Learning y Diagnóstico)"
            else:
                pi_tag = "PI2 (Biomarcadores de Rigidez)"
        elif score >= 4:
            priority = "MEDIA (Complementario)"
            status = "Pasa a Elegibilidad"
            ec = "-"
            pi_tag = "PI1 (Modelos de IA)" if has_deep_learning else "PI3 (Desempeño / Métricas)"
        else:
            priority = "BAJA (Descartar)"
            status = "Excluido en Cribado"
            ec = "EC2 (Topografía estándar sin biomecánica ni IA avanzada)"
            pi_tag = "Ninguno"
            
        papers.append({
            'raw_id': idx,
            'source': source_label,
            'id_prefix': id_prefix,
            'year': year,
            'first_author': first_author,
            'title': title,
            'journal': journal,
            'doi': doi,
            'abstract': ab,
            'score': score,
            'priority': priority,
            'status': status,
            'ec': ec,
            'pi_tag': pi_tag
        })
    return papers

def build_thesis_excel():
    scopus_papers = parse_and_rank_ris('papers/ris/SCOPUS_EXPORTADO_21-0802026.ris', 'Scopus', 'SCO')
    ieee_papers = parse_and_rank_ris('papers/ris/IEEE_Xplore_2026.ris', 'IEEE Xplore', 'IEE')
    all_papers = scopus_papers + ieee_papers
    
    # Ordenar: primero ALTA, luego MEDIA, luego BAJA (por score descendente)
    all_papers.sort(key=lambda x: (0 if "ALTA" in x['priority'] else 1 if "MEDIA" in x['priority'] else 2, -x['score']))
    
    # Asignar IDs ordenados
    for idx, p in enumerate(all_papers, 1):
        p['id'] = f"{p['id_prefix']}-{p['raw_id']:02d}"
        
    print(f"Total de papers procesados: {len(all_papers)}")
    alta_count = sum(1 for p in all_papers if "ALTA" in p['priority'])
    media_count = sum(1 for p in all_papers if "MEDIA" in p['priority'])
    baja_count = sum(1 for p in all_papers if "BAJA" in p['priority'])
    print(f"-> Prioridad ALTA (Candidatos top a texto completo): {alta_count}")
    print(f"-> Prioridad MEDIA (Complementarios): {media_count}")
    print(f"-> Prioridad BAJA (Excluidos automáticos en cribado): {baja_count}")
    
    wb = openpyxl.Workbook()
    
    # Estilos
    header_navy = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_blue = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
    header_green = PatternFill(start_color="375623", end_color="375623", fill_type="solid")
    
    fill_alta = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid") # Verde suave
    fill_media = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid") # Amarillo suave
    fill_baja = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid") # Naranja suave
    
    font_header = Font(name="Calibri", size=10.5, bold=True, color="FFFFFF")
    font_title = Font(name="Calibri", size=13, bold=True, color="1F4E78")
    font_bold = Font(name="Calibri", size=10, bold=True)
    font_regular = Font(name="Calibri", size=10)
    font_abstract = Font(name="Calibri", size=9.5, color="333333")
    font_code = Font(name="Consolas", size=9, color="1F4E78")
    fill_code = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
    
    thin_border = Border(
        left=Side(style="thin", color="D9D9D9"),
        right=Side(style="thin", color="D9D9D9"),
        top=Side(style="thin", color="D9D9D9"),
        bottom=Side(style="thin", color="D9D9D9")
    )
    
    # ==========================================
    # HOJA 1: Protocolo & PICOC
    # ==========================================
    ws1 = wb.active
    ws1.title = "1. Protocolo & PICOC"
    ws1.views.sheetView[0].showGridLines = True
    
    ws1["A1"] = "MÉTODO DE REVISIÓN SISTEMÁTICA Y PROTOCOLO PICOC (PUCP 1INF42)"
    ws1["A1"].font = font_title
    ws1["A2"] = "Tema: Clasificación de queratocono mediante Deep Learning aplicado a mapas de rigidez corneal (Ondas de Lamb / OCE)"
    ws1["A2"].font = Font(name="Calibri", size=10, italic=True)
    ws1["A3"] = "Tesista: Diego Silvestre | Asesor: Dr. César Beltrán Castañón | Co-asesor: Dr. José Fernando Zvietcovich Zegarra"
    ws1["A3"].font = Font(name="Calibri", size=9.5, bold=True, color="595959")
    
    headers_p = ["Componente PICOC", "Definición Metodológica", "Aplicación Específica en la Tesis"]
    for c_idx, h in enumerate(headers_p, 1):
        cell = ws1.cell(row=5, column=c_idx, value=h)
        cell.fill = header_navy
        cell.font = font_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    picoc_data = [
        ("P (Population)", "Población y Muestra de estudio", "142 córneas (71 pares binoculares OD/OS de pacientes) distribuidas en 3 clases clínicas: 1) Normal (Control), 2) Queratocono Subclínico (Forme Fruste), y 3) Queratocono Clínico, caracterizadas con Elastografía OCE y ondas de Lamb."),
        ("I (Intervention)", "Intervención y Propuesta técnica", "Pipeline de Aprendizaje Profundo (CNNs preentrenadas: ResNet-18, EfficientNet-B0) con Transfer Learning, Data Augmentation física y partición por paciente (Stratified Group K-Fold) aplicado a mapas 2D de rigidez / STI."),
        ("C (Comparison)", "Comparación con Métodos existentes", "1) Diagnóstico geométrico estándar (Pentacam / OCT topográfico) ciego a estadios subclínicos. 2) Machine Learning tradicional (SVM RBF, Random Forest, XGBoost) sobre features tabulares (STI medio, SAWS). 3) Umbral escalar univariado de STI."),
        ("O (Outcome)", "Métricas y Resultados esperados", "Exactitud balanceada (>= 90%), Macro F1-Score (>= 0.88), AUC-ROC multiclase (>= 0.92), alta sensibilidad en la clase Subclínico (>= 85%) y mapas de explicabilidad visual (Grad-CAM) concordantes anatómicamente."),
        ("C (Context)", "Contexto Clínico de aplicación", "Sistemas CAD para tamizaje preoperatorio de cirugía refractiva con láser (pre-LASIK) en clínicas oftalmológicas para evitar ectasias iatrogénicas.")
    ]
    
    for r_idx, r_data in enumerate(picoc_data, 6):
        for c_idx, val in enumerate(r_data, 1):
            cell = ws1.cell(row=r_idx, column=c_idx, value=val)
            cell.font = font_bold if c_idx == 1 else font_regular
            cell.border = thin_border
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            
    ws1.cell(row=12, column=1, value="PREGUNTAS DE INVESTIGACIÓN (ESTADO DEL ARTE — ENTREGABLE E1)").font = font_title
    headers_pi = ["Código", "Dimensión de Revisión", "Pregunta de Investigación Formulada"]
    for c_idx, h in enumerate(headers_pi, 1):
        cell = ws1.cell(row=13, column=c_idx, value=h)
        cell.fill = header_blue
        cell.font = font_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    pi_data = [
        ("PI1", "Modelos de IA en Pocos Datos (Intervención)", "¿Qué arquitecturas de redes neuronales convolucionales (ej. ResNet, EfficientNet) y técnicas de transfer learning / data augmentation se utilizan en la literatura médica para clasificar patologías corneales en conjuntos de datos reducidos (N < 300)?"),
        ("PI2", "Biomarcadores y Rigidez (Física / Población)", "¿De qué manera los biomarcadores biomecánicos basados en elastografía y ondas de propagación (velocidad de onda, relación velocidad/grosor STI y rigidez) permiten discriminar estadios tempranos frente a los índices topográficos convencionales?"),
        ("PI3", "Desempeño y Brechas en Subclínico (Métricas / Brechas)", "¿Qué niveles de exactitud y sensibilidad reportan los sistemas actuales de inteligencia artificial al clasificar queratocono subclínico frente a córneas sanas, y cuáles son las principales limitaciones metodológicas identificadas en la literatura?")
    ]
    
    for r_idx, r_data in enumerate(pi_data, 14):
        for c_idx, val in enumerate(r_data, 1):
            cell = ws1.cell(row=r_idx, column=c_idx, value=val)
            cell.font = font_bold if c_idx == 1 else font_regular
            cell.border = thin_border
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            
    ws1.cell(row=18, column=1, value="ESTRATEGIA DE BÚSQUEDA BOOLEANA (2 BASES DE DATOS — RÚBRICA PUCP)").font = font_title
    headers_cad = ["Base de Datos", "Enfoque de Búsqueda", "Cadena Booleana Exacta y Resultados"]
    for c_idx, h in enumerate(headers_cad, 1):
        cell = ws1.cell(row=19, column=c_idx, value=h)
        cell.fill = header_blue
        cell.font = font_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    cad_data = [
        (
            "Scopus (Base 1)",
            "Dominio Clínico, Biomecánica y Machine Learning (84 resultados en papers/ris/SCOPUS_EXPORTADO_21-0802026.ris)",
            'TITLE-ABS-KEY ( ( "keratoconus" OR "corneal ectasia" OR "forme fruste" OR "subclinical keratoconus" ) AND ( "optical coherence elastography" OR "OCE" OR "Lamb wave*" OR "shear wave*" OR "corneal biomechanic*" OR "stiffness map*" ) AND ( "deep learning" OR "machine learning" OR "convolutional neural network*" OR "CNN" ) AND ( "classification" OR "detection" OR "early diagnosis" OR "screening" ) )'
        ),
        (
            "IEEE Xplore (Base 2)",
            "Dominio de Ciencias de la Computación, Deep Learning e Imágenes Corneales (17 resultados en papers/ris/IEEE_Xplore_2026.ris)",
            '( ("Document Title":"keratoconus" OR "Abstract":"keratoconus" OR "Abstract":"corneal ectasia") AND ("Abstract":"deep learning" OR "Abstract":"convolutional neural network" OR "Abstract":"ResNet" OR "Abstract":"EfficientNet" OR "Abstract":"transfer learning") AND ("Abstract":"classification" OR "Abstract":"detection") )'
        )
    ]
    
    for r_idx, r_data in enumerate(cad_data, 20):
        for c_idx, val in enumerate(r_data, 1):
            cell = ws1.cell(row=r_idx, column=c_idx, value=val)
            if c_idx == 3:
                cell.font = font_code
                cell.fill = fill_code
            elif c_idx == 1:
                cell.font = font_bold
            else:
                cell.font = font_regular
            cell.border = thin_border
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            
    ws1.column_dimensions["A"].width = 22
    ws1.column_dimensions["B"].width = 34
    ws1.column_dimensions["C"].width = 95
    
    # ==========================================
    # HOJA 2: PRISMA - Cribado Total (101 Papers)
    # ==========================================
    ws2 = wb.create_sheet(title="2. PRISMA - Cribado Total (101)")
    ws2.views.sheetView[0].showGridLines = True
    
    headers_crib = [
        "ID", "Base", "Año", "Primer Autor", "Título del Artículo Científico",
        "Prioridad Sugerida", "Aporte Principal (PI)", "Decisión Cribado (Fase 2)",
        "Criterio de Exclusión (si aplica)", "Revista / Conferencia", "DOI", "Resumen (Abstract)"
    ]
    
    for c_idx, h in enumerate(headers_crib, 1):
        cell = ws2.cell(row=1, column=c_idx, value=h)
        cell.fill = header_navy
        cell.font = font_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    # Validaciones de datos (Dropdowns)
    dv_decision = DataValidation(type="list", formula1='"Pasa a Elegibilidad,Excluido en Cribado,Incluido Final en Anexo A"', allow_blank=True)
    dv_prioridad = DataValidation(type="list", formula1='"ALTA (Candidato Principal),MEDIA (Complementario),BAJA (Descartar)"', allow_blank=True)
    dv_ec = DataValidation(type="list", formula1='"- ,EC1: Sin acceso a texto completo,EC2 (Sin IA / Quirúrgico puro),EC2 (Topografía estándar sin biomecánica),EC3: Otra patología no corneal,EC4 (Editorial/Narrativa)"', allow_blank=True)
    
    ws2.add_data_validation(dv_decision)
    ws2.add_data_validation(dv_prioridad)
    ws2.add_data_validation(dv_ec)
    
    dv_prioridad.add(f"F2:F{len(all_papers)+1}")
    dv_decision.add(f"H2:H{len(all_papers)+1}")
    dv_ec.add(f"I2:I{len(all_papers)+1}")
    
    for r_idx, p in enumerate(all_papers, 2):
        row_vals = [
            p['id'], p['source'], p['year'], p['first_author'], p['title'],
            p['priority'], p['pi_tag'], p['status'], p['ec'],
            p['journal'], p['doi'], p['abstract']
        ]
        for c_idx, val in enumerate(row_vals, 1):
            cell = ws2.cell(row=r_idx, column=c_idx, value=val)
            cell.border = thin_border
            if c_idx in [1, 2, 3]:
                cell.font = font_bold
                cell.alignment = Alignment(horizontal="center", vertical="top")
            elif c_idx == 4:
                cell.font = font_regular
                cell.alignment = Alignment(vertical="top")
            elif c_idx == 5:
                cell.font = font_bold
                cell.alignment = Alignment(vertical="top", wrap_text=True)
            elif c_idx == 6: # Prioridad
                cell.font = font_bold
                cell.alignment = Alignment(horizontal="center", vertical="top")
                if "ALTA" in val: cell.fill = fill_alta
                elif "MEDIA" in val: cell.fill = fill_media
                else: cell.fill = fill_baja
            elif c_idx == 7: # Aporte PI
                cell.font = font_regular
                cell.alignment = Alignment(vertical="top")
            elif c_idx == 8: # Decisión Cribado
                cell.font = font_bold
                cell.alignment = Alignment(horizontal="center", vertical="top")
                if val == "Pasa a Elegibilidad": cell.fill = fill_alta
                else: cell.fill = fill_baja
            elif c_idx == 9: # EC
                cell.font = font_regular
                cell.alignment = Alignment(vertical="top")
            elif c_idx in [10, 11]:
                cell.font = font_regular
                cell.alignment = Alignment(vertical="top")
            elif c_idx == 12: # Abstract
                cell.font = font_abstract
                cell.alignment = Alignment(vertical="top", wrap_text=True)
                
    ws2.column_dimensions["A"].width = 12
    ws2.column_dimensions["B"].width = 14
    ws2.column_dimensions["C"].width = 8
    ws2.column_dimensions["D"].width = 18
    ws2.column_dimensions["E"].width = 38
    ws2.column_dimensions["F"].width = 24
    ws2.column_dimensions["G"].width = 32
    ws2.column_dimensions["H"].width = 24
    ws2.column_dimensions["I"].width = 30
    ws2.column_dimensions["J"].width = 22
    ws2.column_dimensions["K"].width = 18
    ws2.column_dimensions["L"].width = 65
    
    # ==========================================
    # HOJA 3: Anexo A - Matriz de Extracción (20-25)
    # ==========================================
    ws3 = wb.create_sheet(title="3. Anexo A - Matriz Extracción")
    ws3.views.sheetView[0].showGridLines = True
    
    headers_anexo = [
        "ID Ref", "Referencia APA 7ma (Autor, Año)", "Título del Paper",
        "Enfoque de Clases (Binario / 3 Clases)", "Dispositivo / Modalidad (OCE, Pentacam, OCT, Corvis)",
        "Biomarcador / Entrada (Ondas Lamb, STI, Rigidez, Curvatura)", "Modelo IA / Arquitectura (ResNet, SVM, CNN, RF)",
        "Tamaño Dataset (# Ojos / # Pacientes)", "Métricas Reportadas (Accuracy, Sensibilidad Subclínico, AUC-ROC)",
        "Limitaciones / Brechas Reportadas",
        "Aporte a PI1 (Modelos en Pocos Datos)", "Aporte a PI2 (Biomarcadores vs Topografía)", "Aporte a PI3 (Desempeño y Brechas Subclínico)",
        "Estado de Lectura"
    ]
    
    for c_idx, h in enumerate(headers_anexo, 1):
        cell = ws3.cell(row=1, column=c_idx, value=h)
        cell.fill = header_green
        cell.font = font_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    for c_idx in range(1, len(headers_anexo) + 1):
        ws3.column_dimensions[get_column_letter(c_idx)].width = 24
    ws3.column_dimensions["B"].width = 28
    ws3.column_dimensions["C"].width = 38
    ws3.column_dimensions["H"].width = 30
    ws3.column_dimensions["I"].width = 30
    ws3.column_dimensions["J"].width = 32
    
    # Poblar preliminarmente los Top 20 de prioridad ALTA en el Anexo A
    top_papers = [p for p in all_papers if "ALTA" in p['priority']][:20]
    for r_idx, p in enumerate(top_papers, 2):
        row_vals = [
            p['id'], f"{p['first_author']} et al. ({p['year']})", p['title'],
            "3 Clases (Normal / Subclínico / KC)" if "subclinical" in p['title'].lower() else "Binario / Multiclase",
            "OCE / Elastografía / Corvis" if "elastography" in p['abstract'].lower() else "Pentacam / Topógrafo / OCT",
            "Rigidez / Ondas / Desplazamiento" if "stiffness" in p['abstract'].lower() else "Mapas de elevación / Curvatura",
            "CNN / ResNet / Deep Learning" if "deep learning" in p['abstract'].lower() else "Machine Learning (SVM / RF)",
            "Por extraer del PDF", "Por extraer del PDF", "Por extraer del PDF",
            "Aporte directo a PI1" if "deep learning" in p['abstract'].lower() else "-",
            "Aporte directo a PI2" if "stiffness" in p['abstract'].lower() or "wave" in p['abstract'].lower() else "-",
            "Aporte directo a PI3 (Sensibilidad subclínico)",
            "Pendiente de Lectura Completa"
        ]
        for c_idx, val in enumerate(row_vals, 1):
            cell = ws3.cell(row=r_idx, column=c_idx, value=val)
            cell.border = thin_border
            cell.font = font_bold if c_idx in [1, 2] else font_regular
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            
    # ==========================================
    # HOJA 4: Resumen Cuantitativo PRISMA
    # ==========================================
    ws4 = wb.create_sheet(title="4. Resumen Flujo PRISMA")
    ws4.views.sheetView[0].showGridLines = True
    
    ws4["A1"] = "DIAGRAMA DE FLUJO PRISMA 2020 — CONTEO FORMAL"
    ws4["A1"].font = font_title
    
    headers_res = ["Fase del Protocolo PRISMA", "Descripción de la Etapa", "Cantidad (n)"]
    for c_idx, h in enumerate(headers_res, 1):
        cell = ws4.cell(row=3, column=c_idx, value=h)
        cell.fill = header_navy
        cell.font = font_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    res_data = [
        ("1. Identificación", "Registros identificados en Scopus (84) + IEEE Xplore (17)", f"{len(all_papers)}"),
        ("1.1 Duplicados", "Registros duplicados eliminados", "0"),
        ("2. Cribado (Screening)", "Registros evaluados por título y resumen", f"{len(all_papers)}"),
        ("2.1 Excluidos en Cribado", f"Excluidos por criterios EC (sin IA, quirúrgicos puros, topografía estándar)", f"{baja_count}"),
        ("3. Elegibilidad", "Artículos candidatos evaluados a texto completo (Prioridad Alta + Media)", f"{alta_count + media_count}"),
        ("3.1 Excluidos a Texto Completo", "Excluidos tras revisión metodológica detallada", f"{alta_count + media_count - 20}"),
        ("4. Inclusión (Anexo A)", "Artículos finales incluidos en la matriz de extracción cualitativa/cuantitativa", "20")
    ]
    
    for r_idx, r_data in enumerate(res_data, 4):
        for c_idx, val in enumerate(r_data, 1):
            cell = ws4.cell(row=r_idx, column=c_idx, value=val)
            cell.font = font_bold if c_idx in [1, 3] else font_regular
            cell.border = thin_border
            if c_idx == 3:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(vertical="center")
                
    ws4.column_dimensions["A"].width = 28
    ws4.column_dimensions["B"].width = 65
    ws4.column_dimensions["C"].width = 16
    
    out_path = "papers/Referencias.xlsx"
    wb.save(out_path)
    print(f"Archivo Excel enriquecido generado con éxito en: {out_path}")

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    build_thesis_excel()


