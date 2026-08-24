# 📄 Entregable 1 (E1) — Borrador de Redacción y Estructura Formal

**Título del Proyecto:** Clasificación de queratocono mediante modelos de aprendizaje profundo aplicados a mapas de rigidez corneal reconstruidos a partir de biomarcadores de velocidad de onda  
**Estudiante:** Diego Alejandro Silvestre  
**Asesor:** Dr. César Beltrán Castañón (Informática / IA - PUCP)  
**Co-asesor:** Dr. José Fernando Zvietcovich Zegarra (Biofotónica / OCE - PUCP)  
**Curso:** 1INF42 - Proyecto de Fin de Carrera 1 (2026-2)  

---

## 1. Problemática

### 1.1 Contexto y Situación Actual
El queratocono es una ectasia corneal progresiva no inflamatoria que debilita la estructura biomecánica de la córnea, provocando su adelgazamiento y protusión cónica. Esta alteración genera astigmatismo irregular severo y disminución progresiva de la agudeza visual. En el contexto de la oftalmología moderna, uno de los mayores desafíos clínicos se presenta en la evaluación preoperatoria de cirugías refractivas con láser (pre-LASIK). Si un paciente con queratocono incipiente o asintomático (**Queratocono Subclínico / *Forme Fruste***) es sometido a un procedimiento LASIK, la ablación estromal debilita irreversiblemente el tejido restante, provocando una ectasia iatrogénica postquirúrgica de difícil tratamiento.

Los métodos diagnósticos convencionales utilizados en la práctica clínica (topografía y tomografía corneal, tales como Pentacam u OCT de segmento anterior) se basan exclusivamente en la caracterización morfológica y geométrica externa (curvatura anterior/posterior y paquimetría). No obstante, la pérdida de rigidez biomecánica precede temporalmente a la deformación geométrica visible. Por tanto, en fases subclínicas, los índices topográficos arrojan valores dentro de los rangos de normalidad, impidiendo una detección oportuna.

### 1.2 Modelado del Problema (Árbol de Problemas)

```text
[EFECTO 1] Ectasias iatrogénicas post-LASIK por cirugías en ojos con debilidad subclínica
[EFECTO 2] Diagnóstico tardío del queratocono cuando la deformación ya es irreversible
[EFECTO 3] Dependencia exclusiva del criterio subjetivo del especialista clínico
                               ▲
                      [PROBLEMA CENTRAL]
    Incapacidad de los sistemas actuales de diagnóstico clínico para detectar 
    el queratocono en estadios tempranos/subclínicos de forma temprana y automatizada
                               ▲
[CAUSA 1] Topógrafos estándar (Pentacam) miden geometría externa, ciega a la rigidez temprana
[CAUSA 2] Falta de modelos de IA adaptados a señales biomecánicas de ondas de Lamb
[CAUSA 3] Ausencia de herramientas CAD automáticas para screening preoperatorio basadas en OCE
```

### 1.3 Situación Deseada y Justificación Técnica
Se busca desarrollar una solución informática automatizada de diagnóstico asistido por computadora (CAD) basada en modelos de Aprendizaje Profundo (Deep Learning), capaz de procesar mapas 2D de rigidez corneal reconstruidos a partir de biomarcadores de velocidad de ondas de Lamb capturados mediante Elastografía por Coherencia Óptica (OCE). Esta propuesta permitirá discriminar de manera precisa y cuantitativa entre ojos sanos, subclínicos y patológicos, brindando una herramienta objetiva y temprana para el tamizaje clínico preoperatorio.

---

## 2. Revisión de la Literatura y Estado del Arte

### 2.1 Protocolo PICOC
* **Población (P):** 142 córneas (71 pares binoculares de pacientes) caracterizadas con elastografía OCE y clasificadas clínicamente en 3 grupos: Normales (Control), Queratocono Subclínico (*Forme Fruste*) y Queratocono Clínico.
* **Intervención (I):** Pipeline de Deep Learning (redes convolucionales preentrenadas: ResNet, EfficientNet) con partición agrupada por paciente (*Group K-Fold*) y data augmentation sobre mapas 2D de rigidez / STI.
* **Comparación (C):** Topografía Pentacam estándar, análisis estadístico de umbral univariado y modelos de Machine Learning clásico (SVM, Random Forest).
* **Resultados (O):** Exactitud global balanceada ($\ge 90\%$), Macro F1-score ($\ge 0.88$), AUC-ROC ($\ge 0.92$), alta sensibilidad en subclínicos ($\ge 85\%$) y mapas visuales explicables (Grad-CAM).
* **Contexto (C):** Tamizaje automatizado en evaluación preoperatoria de cirugía refractiva (pre-LASIK).

### 2.2 Preguntas de Investigación (PI)
1. **PI1 (Modelos en Datasets Reducidos):** *¿Qué arquitecturas de redes neuronales convolucionales (ej. ResNet, EfficientNet) y técnicas de transfer learning / data augmentation ofrecen mayor robustez y previenen el sobreajuste para la clasificación de mapas 2D médicos con muestras limitadas ($N < 300$)?*
2. **PI2 (Biomarcadores de OCE y Rigidez):** *¿De qué manera los biomarcadores biomecánicos basados en elastografía OCE (velocidad de ondas de Lamb, índice STI y anisotropía espacial SAWS) permiten discriminar estadios subclínicos frente a los índices topográficos convencionales?*
3. **PI3 (Desempeño y Brechas en Queratocono Subclínico):** *¿Qué niveles de exactitud y sensibilidad reportan los sistemas actuales de inteligencia artificial al clasificar queratocono subclínico frente a córneas sanas, y cuáles son las principales limitaciones metodológicas identificadas en la literatura?*

### 2.3 Estrategia de Búsqueda y Protocolo PRISMA
* **Bases de datos utilizadas:** Scopus e IEEE Xplore.
* **Cadenas booleanas:**
  * *Scopus:* `TITLE-ABS-KEY ( ( "keratoconus" OR "corneal ectasia" OR "forme fruste" OR "subclinical keratoconus" ) AND ( "optical coherence elastography" OR "OCE" OR "Lamb wave*" OR "shear wave*" OR "corneal biomechanic*" OR "stiffness map*" ) AND ( "deep learning" OR "machine learning" OR "convolutional neural network*" OR "CNN" ) AND ( "classification" OR "detection" OR "early diagnosis" OR "screening" ) )` $\rightarrow$ **84 resultados** (`papers/ris/SCOPUS_EXPORTADO_21-0802026.ris`).
  * *IEEE Xplore:* `( ("Document Title":"keratoconus" OR "Abstract":"keratoconus" OR "Abstract":"corneal ectasia") AND ("Abstract":"deep learning" OR "Abstract":"convolutional neural network" OR "Abstract":"ResNet" OR "Abstract":"EfficientNet" OR "Abstract":"transfer learning") AND ("Abstract":"classification" OR "Abstract":"detection") )` $\rightarrow$ **17 resultados** (`papers/ris/IEEE_Xplore_2026.ris`).
* **Total identificado:** **101 artículos científicos**.
* **Formulario de Extracción:** Adjunto como **Anexo A** (`papers/Referencias.xlsx`).

---

## 3. Objetivos y Resultados Esperados

### 3.1 Objetivo General
Desarrollar un sistema de clasificación multiclase de queratocono mediante modelos de aprendizaje profundo aplicados a mapas 2D de rigidez corneal reconstruidos a partir de biomarcadores de velocidad de ondas de Lamb obtenidos por elastografía OCE.

### 3.2 Objetivos Específicos (OE) e Indicadores Objetivamente Verificables (IOV)

| Objetivo Específico | Resultado Esperado | Indicador Objetivamente Verificable (IOV) |
| :--- | :--- | :--- |
| **OE1:** Decodificar y procesar las señales binarias de OCE de 142 córneas (71 pacientes) para reconstruir mapas polares 2D de rigidez y velocidad de onda. | **R1:** Dataset estructurado de 142 mapas 2D normalizados ($224 \times 224$ px) con matriz de metadatos clínicos asociados. | Archivo `.csv` con 142 registros y carpeta de imágenes 2D validadas en resolución y contraste con 0% de datos corruptos. |
| **OE2:** Implementar modelos basales de Machine Learning clásico sobre biomarcadores tabulares como punto de comparación. | **R2:** Módulo de clasificación tradicional entrenado (SVM RBF, Random Forest, XGBoost). | Reporte reproducible de métricas base (Accuracy, F1-Score) sobre los biomarcadores escalares ($\text{STI}$ medio, $\text{SAWS}$). |
| **OE3:** Diseñar, entrenar y optimizar una arquitectura de Deep Learning (CNN con Transfer Learning) con validación agrupada por paciente (*Group K-Fold*). | **R3:** Modelo de red neuronal convolucional multiclase optimizado y validado. | Código ejecutable en PyTorch que alcance $\text{Accuracy} \ge 90\%$, $\text{AUC-ROC} \ge 0.92$ y $\text{Sensibilidad Subclínica} \ge 85\%$. |
| **OE4:** Evaluar comparativamente el desempeño del modelo propuesto frente a las líneas base y generar mapas de explicabilidad visual. | **R4:** Informe de validación experimental con mapas de interpretabilidad Grad-CAM. | Matrices de confusión, curvas ROC comparativas y mapas Grad-CAM con concordancia anatómica en la zona de ablandamiento. |

---

## 4. Cronograma de Trabajo

*(Se adjunta el cronograma detallado del ciclo 2026-2 en el archivo oficial `docs/cronogramas/Cronograma-diego-silvestre.md`).*

---

## 5. Anexos
* **Anexo A:** Formulario de extracción de artículos científicos (`papers/Referencias.xlsx`).
