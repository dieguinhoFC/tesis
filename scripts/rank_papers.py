import re

def analyze_ris(path, src_name):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    entries = [e for e in content.split('ER  -') if e.strip()]
    results = []
    for e in entries:
        t_m = re.search(r'(?:TI|T1)\s+-\s+(.+)', e)
        y_m = re.search(r'(?:PY|Y1|DA)\s+-\s+(\d{4})', e)
        a_m = re.findall(r'(?:AU|A1)\s+-\s+(.+)', e)
        ab_m = re.search(r'(?:AB|N2)\s+-\s+(.+)', e, re.DOTALL)
        doi_m = re.search(r'(?:DO)\s+-\s+(.+)', e)
        title = t_m.group(1).strip() if t_m else 'No title'
        year = y_m.group(1).strip() if y_m else 'N/A'
        authors = [a.strip() for a in a_m]
        ab = ab_m.group(1).strip() if ab_m else ''
        doi = doi_m.group(1).strip() if doi_m else ''
        
        # Scoring keywords
        score = 0
        txt = (title + ' ' + ab).lower()
        if any(k in txt for k in ['subclinical', 'forme fruste', 'early', 'suspect']): score += 3
        if any(k in txt for k in ['elastography', 'oce', 'lamb wave', 'shear wave', 'stiffness', 'elasticity']): score += 4
        if any(k in txt for k in ['deep learning', 'cnn', 'resnet', 'convolutional', 'transfer learning']): score += 4
        if any(k in txt for k in ['machine learning', 'random forest', 'svm', 'xgboost', 'artificial intelligence']): score += 2
        if any(k in txt for k in ['corvis', 'biomechanic', 'tbi', 'cbi']): score += 2
        
        results.append({'title': title, 'year': year, 'authors': authors, 'abstract': ab, 'score': score, 'source': src_name, 'doi': doi})
    return results

all_p = analyze_ris('papers/ris/SCOPUS_EXPORTADO_21-0802026.ris', 'Scopus') + analyze_ris('papers/ris/IEEE_Xplore_2026.ris', 'IEEE')
all_p.sort(key=lambda x: x['score'], reverse=True)

import sys
sys.stdout.reconfigure(encoding='utf-8')

print(f"Total analizados: {len(all_p)}")
print("=== TOP 18 PAPERS PARA ANEXO A / MATRIZ DE EXTRACCIÓN ===")
for i, p in enumerate(all_p[:20]):
    first_auth = p['authors'][0] if p['authors'] else 'Anon'
    print(f"{i+1}. [{p['year']}] {p['title']} ({first_auth} et al.) | Score: {p['score']} | {p['source']}")
