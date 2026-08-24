import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

def parse_all_ris():
    papers = []
    for filepath, src in [('papers/ris/SCOPUS_EXPORTADO_21-0802026.ris', 'Scopus'), ('papers/ris/IEEE_Xplore_2026.ris', 'IEEE')]:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        entries = [e for e in content.split('ER  -') if e.strip()]
        for e in entries:
            t_m = re.search(r'(?:TI|T1)\s+-\s+(.+)', e)
            y_m = re.search(r'(?:PY|Y1|DA)\s+-\s+(\d{4})', e)
            a_m = re.findall(r'(?:AU|A1)\s+-\s+(.+)', e)
            ab_m = re.search(r'(?:AB|N2)\s+-\s+(.+)', e, re.DOTALL)
            title = t_m.group(1).strip() if t_m else 'Sin título'
            year = y_m.group(1).strip() if y_m else 'N/A'
            ab = ab_m.group(1).strip() if ab_m else ''
            auth = a_m[0].strip() if a_m else 'Anon'
            papers.append({'title': title, 'year': year, 'first_author': auth, 'abstract': ab, 'source': src})
    return papers

papers = parse_all_ris()

included_screening = []
excluded_no_ia = []
excluded_editorial_narrative = []

for p in papers:
    txt = (p['title'] + ' ' + p['abstract']).lower()
    has_ia = any(k in txt for k in ['machine learning', 'deep learning', 'cnn', 'neural network', 'artificial intelligence', 'svm', 'random forest', 'xgboost', 'resnet', 'transformer', 'classifier', 'classification'])
    is_editorial_narrative = any(k in txt for k in ['narrative review', 'letter to editor', 'retracted', 'bibliometric analysis'])
    is_pure_surgery_drug = any(k in txt for k in ['cross-linking outcomes', 'swimming goggle', 'turner syndrome', 'cytokine profile', 'transcriptomic', 'intracorneal ring segments', 'corneal ring implantation']) and not any(k in txt for k in ['deep learning', 'cnn', 'machine learning'])

    if is_editorial_narrative or 'retracted:' in txt:
        excluded_editorial_narrative.append(p)
    elif not has_ia or is_pure_surgery_drug:
        excluded_no_ia.append(p)
    else:
        included_screening.append(p)

print(f"Total identificados en RIS: {len(papers)}")
print(f"1. Excluidos por falta de IA / quirúrgicos puros / genética: {len(excluded_no_ia)}")
print(f"2. Excluidos por editoriales / retractados / revisiones narrativas: {len(excluded_editorial_narrative)}")
print(f"3. Elegibles para evaluación detallada (Fase 3): {len(included_screening)}")

print("\n--- Lista de Candidatos Preseleccionados (Candidatos para los 16-20 finales) ---")
for i, p in enumerate(included_screening[:25]):
    print(f"{i+1}. [{p['year']}] {p['title']} ({p['first_author']} et al.) - {p['source']}")
