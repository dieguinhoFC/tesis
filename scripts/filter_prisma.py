import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('papers/ris/SCOPUS_EXPORTADO_21-0802026.ris', 'r', encoding='utf-8', errors='ignore') as f:
    scopus_txt = f.read()
with open('papers/ris/IEEE_Xplore_2026.ris', 'r', encoding='utf-8', errors='ignore') as f:
    ieee_txt = f.read()

entries = [('Scopus', e) for e in scopus_txt.split('ER  -') if e.strip()] + [('IEEE', e) for e in ieee_txt.split('ER  -') if e.strip()]

selected_papers = []

for src, e in entries:
    t_m = re.search(r'(?:TI|T1)\s+-\s+(.+)', e)
    y_m = re.search(r'(?:PY|Y1|DA)\s+-\s+(\d{4})', e)
    a_m = re.findall(r'(?:AU|A1)\s+-\s+(.+)', e)
    ab_m = re.search(r'(?:AB|N2)\s+-\s+(.+)', e, re.DOTALL)
    doi_m = re.search(r'(?:DO)\s+-\s+(.+)', e)
    j_m = re.search(r'(?:JO|JF|T2|JA)\s+-\s+(.+)', e)
    
    title = t_m.group(1).strip() if t_m else 'No title'
    year = y_m.group(1).strip() if y_m else 'N/A'
    authors = [a.strip() for a in a_m]
    ab = ab_m.group(1).strip() if ab_m else ''
    doi = doi_m.group(1).strip() if doi_m else ''
    journal = j_m.group(1).strip() if j_m else 'N/A'
    
    txt = (title + ' ' + ab).lower()
    
    # Exclusiones automáticas (EC)
    if any(k in txt for k in ['cross-linking surgery outcomes', 'predicting outcome of treatment', 'swimming goggle', 'turner syndrome', 'cytokine profile', 'transcriptomic', 'intracorneal ring', 'retracted:', 'bibliometric analysis', 'parental corneal', 'corneoscleral morphology in keratoconus and its association']):
        continue
    
    # Diagnóstico / clasificación con IA
    is_diag_ai = any(k in txt for k in ['classification', 'detect', 'diagnosis', 'screening', 'grading']) and any(k in txt for k in ['deep learning', 'cnn', 'machine learning', 'neural network', 'svm', 'random forest', 'xgboost', 'resnet', 'efficientnet', 'transfer learning', 'transformer', 'artificial intelligence'])
    
    if not is_diag_ai:
        continue
        
    has_subclinical = any(k in txt for k in ['subclinical', 'forme fruste', 'early', 'suspect', 'incipient', 'pre-clinical'])
    has_biomech_map = any(k in txt for k in ['biomechanic', 'corvis', 'elastography', 'oce', 'stiffness', 'shear wave', 'lamb wave', 'topograph', 'tomograph', 'map', 'raw data'])
    
    score = 0
    if has_subclinical: score += 5
    if has_biomech_map: score += 5
    if any(k in txt for k in ['deep learning', 'cnn', 'resnet', 'transformer']): score += 3
    if 'group' in txt or 'cross-validation' in txt or 'k-fold' in txt: score += 2
    
    selected_papers.append({
        'title': title,
        'year': year,
        'first_author': authors[0] if authors else 'Anon',
        'journal': journal,
        'source': src,
        'score': score,
        'abstract': ab,
        'doi': doi
    })

selected_papers.sort(key=lambda x: x['score'], reverse=True)
print(f"Total tras filtrado sistemático PRISMA: {len(selected_papers)} artículos relevantes")
print("\n=== TOP 20 PAPERS SELECCIONADOS PARA LA MATRIZ DE EXTRACCIÓN (ANEXO A) ===")
for i, p in enumerate(selected_papers[:20]):
    print(f"{i+1:2d}. [{p['year']}] {p['title']} ({p['first_author']} et al.) [{p['source']}]")
