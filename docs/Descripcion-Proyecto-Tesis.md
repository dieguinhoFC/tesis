# 📘 Documento Maestro: Descripción del Proyecto, PICOC, Metodología y Estado del Arte

**Tema:** Clasificación de queratocono mediante modelos de aprendizaje profundo aplicados a mapas de rigidez corneal reconstruidos a partir de biomarcadores de velocidad de onda  
**Tesista:** Diego Alejandro Silvestre  
**Asesor:** Dr. César Beltrán Castañón (Inteligencia Artificial / Informática PUCP)  
**Co-asesor:** Dr. José Fernando Zvietcovich Zegarra (Grupo de Biofotónica / OCE / Datos)  
**Especialidad:** Ingeniería Informática — Pontificia Universidad Católica del Perú (PUCP)  
**Curso:** 1INF42 - Proyecto de Fin de Carrera 1 (2026-2)  

---

## 1. Fundamento del Problema (Alineado al Árbol de Problemas)

El proyecto aborda la dificultad de clasificar de forma precisa el estado de la córnea (normal, subclínico y avanzado), un proceso actualmente ineficiente debido a las siguientes causas fundamentales:

### A. Limitaciones Clínicas y Sutileza de la Enfermedad
* **El riesgo crítico (Pre-LASIK):** Operar con láser a un paciente con queratocono incipiente (**Queratocono Subclínico o *Forme Fruste - FFKC***) desencadena una complicación iatrogénica devastadora (*ectasia post-LASIK*).
* **Limitación de parámetros morfológicos (Topografía):** Los equipos clínicos estándar solo miden geometría. Al no medir directamente el debilitamiento biomecánico temprano de la córnea, fallan en la detección subclínica.
* **Sutileza de los cambios tempranos:** Las variaciones biomecánicas entre un ojo sano y uno con queratocono subclínico son extremadamente sutiles y se solapan estadísticamente, haciendo que los métodos de clasificación manual y los umbrales simples sean ineficientes.

### B. El Reto Biomecánico y la Pérdida de Información Analítica
* **Elastografía por Coherencia Óptica (OCE):** Para superar las limitaciones morfológicas, el laboratorio de biofotónica utiliza OCE para rastrear la propagación de **ondas de Lamb** y generar biomarcadores como el índice $\text{STI}$ (*Speed-Thickness Index*) y reconstrucciones en **Mapas Polares 2D**.
* **Complejidad física de los datos:** La propagación de estas ondas mecánicas exhibe un comportamiento no lineal altamente complejo, acoplado a variables como la anisotropía y el espesor.
* **Pérdida de información en el análisis tradicional:** Reducir esta rica información espacio-temporal (Mapas 2D polares) a simples promedios escalares o índices tabulares omite patrones implícitos y asimetrías cruciales para lograr una clasificación precisa.

**La Solución Propuesta (Informática):** Extraer automáticamente características profundas directamente de los **Mapas Polares 2D** mediante *Deep Learning*, evitando la pérdida de información del procesamiento analítico tabular y capturando las sutiles relaciones no lineales para diferenciar el queratocono subclínico.

---

## 2. Protocolo PICOC Formal y Blindado

| Componente | Definición | Aplicación en la Tesis |
| :--- | :--- | :--- |
| **P** *(Population)* | Población / Muestra | **142 córneas (71 pares binoculares OD/OS de pacientes)** evaluadas con elastografía OCE y distribuidas en 3 clases clínicas: **Normal (Control)**, **Queratocono Subclínico (*Forme Fruste*)** y **Queratocono Clínico**. |
| **I** *(Intervention)* | Intervención / Propuesta | Pipeline de **Deep Learning** (redes convolucionales preentrenadas: ResNet-18, EfficientNet-B0) con transfer learning, data augmentation y partición agrupada por paciente (*Group K-Fold*) sobre **mapas 2D polares de rigidez / STI**. |
| **C** *(Comparison)* | Comparación | 1. Diagnóstico geométrico estándar (*Pentacam / OCT topográfico*).<br>2. Modelos de Machine Learning clásico (SVM con kernel RBF, Random Forest, XGBoost) sobre features tabulares ($\text{STI}$ medio, $\text{SAWS}$).<br>3. Clasificación por corte escalar univariado de $\text{STI}$. |
| **O** *(Outcome)* | Métricas y Resultados | • Exactitud global balanceada ($\ge 90\%$), Macro F1-Score ($\ge 0.88$) y AUC-ROC multiclase ($\ge 0.92$).<br>• Alta sensibilidad/recall en la clase **Subclínico** ($\ge 85\%$).<br>• Mapas de explicabilidad visual (**Grad-CAM**) con validación de concordancia anatómica. |
| **C** *(Context)* | Contexto Clínico | Sistemas CAD (*Computer-Aided Diagnosis*) para **screening y evaluación preoperatoria de cirugía refractiva (pre-LASIK)** en clínicas oftalmológicas. |

---

## 3. Objetivos de la Tesis y Resultados (IOV)

*   **Objetivo General:** Desarrollar y validar un pipeline computacional basado en redes neuronales convolucionales para la clasificación automatizada de queratocono (normal, subclínico y clínico) a partir de mapas espaciales de velocidad de onda (OCE), optimizando el tiempo de procesamiento y la precisión diagnóstica.
*   **Objetivos Específicos & Resultados Esperados (IOV):**
    1.  **OE1:** Preprocesar y consolidar el dataset de mapas OCE provenientes de 142 córneas (71 pacientes) para su compatibilidad con arquitecturas profundas.
        *   *Resultado 1:* Dataset estructurado y particionado (Group K-Fold).
        *   *IOV:* Repositorio de datos/metadatos documentado en formato CSV/HDF5.
    2.  **OE2:** Diseñar y entrenar modelos de Deep Learning (ej. ResNet, EfficientNet) empleando transferencia de aprendizaje para extraer características latentes de los mapas de rigidez.
        *   *Resultado 2:* Algoritmo de clasificación entrenado.
        *   *IOV:* Repositorio de código (GitHub) con el script de entrenamiento y archivo de pesos (`.pth` o `.h5`).
    3.  **OE3:** Evaluar el rendimiento diagnóstico del modelo mediante métricas de clasificación multiclase (AUC-ROC, F1-Score) y métodos de interpretabilidad visual (Grad-CAM).
        *   *Resultado 3:* Reporte técnico de validación del modelo.
        *   *IOV:* Documento de reporte (o notebook de evaluación) detallando matrices de confusión y mapas de activación.

---

## 4. Preguntas de Investigación (PI) para el Estado del Arte (E1)

Las preguntas de investigación (PI) guiarán el desarrollo de la Revisión Sistemática (PRISMA):

* **PI 1 (Automatización del Cuello de Botella Matemático):**  
  > *¿De qué manera las arquitecturas de Deep Learning permiten analizar directamente los mapas espacio-temporales de elastografía (OCE), automatizando y reemplazando la compleja extracción matemática manual de parámetros biomecánicos?*

* **PI 2 (Efectividad en Diagnóstico Subclínico):**  
  > *¿Qué tan efectiva es esta clasificación automatizada con Inteligencia Artificial para diferenciar el queratocono subclínico de una córnea normal, superando las sutiles diferencias biomecánicas?*

* **PI 3 (Viabilidad y Confianza Clínica):**  
  > *¿Cómo el uso de técnicas de explicabilidad visual (como mapas Grad-CAM) ayuda a justificar clínicamente las predicciones del modelo de IA, reduciendo el riesgo de sesgo humano y facilitando su adopción médica?*

---

## 4. Estrategia de Búsqueda Sistemática (Protocolo PRISMA)

### A. Ecuaciones de Búsqueda Booleanas (Derivadas del PICOC)

#### 1. Scopus (Cadena principal de extracción — 84 resultados base en `papers/ris/SCOPUS_EXPORTADO_21-0802026.ris`):
```sql
TITLE-ABS-KEY (
  ( "keratoconus" OR "corneal ectasia" OR "forme fruste" OR "subclinical keratoconus" )
  AND ( "optical coherence elastography" OR "OCE" OR "Lamb wave*" OR "shear wave*" OR "corneal biomechanic*" OR "stiffness map*" )
  AND ( "deep learning" OR "machine learning" OR "convolutional neural network*" OR "CNN" )
  AND ( "classification" OR "detection" OR "early diagnosis" OR "screening" )
)
```

#### 2. IEEE Xplore (Cadena complementaria de ingeniería y procesamiento):
```sql
( ("Document Title":"keratoconus" OR "Abstract":"keratoconus" OR "Abstract":"corneal ectasia")
  AND ("Abstract":"elastography" OR "Abstract":"biomechanic*" OR "Abstract":"wave speed")
  AND ("Abstract":"deep learning" OR "Abstract":"neural network" OR "Abstract":"machine learning") )
```

### B. Criterios de Selección

* **Criterios de Inclusión (IC):**
  * **IC1:** Publicaciones en revistas o conferencias indexadas (Scopus / IEEE / PubMed) entre 2019 y 2026.
  * **IC2:** Aplicación de Machine Learning o Deep Learning para detección, estadificación o pronóstico de queratocono.
  * **IC3:** Empleo de datos biomecánicos, elastografía (OCE, Corvis ST) o mapas de rigidez.
  * **IC4:** Evaluación de estadios tempranos o queratocono subclínico (*Forme Fruste*).

* **Criterios de Exclusión (EC):**
  * **EC1:** Documentos sin acceso a texto completo.
  * **EC2:** Estudios puramente quirúrgicos o farmacológicos sin algoritmos de software/IA.
  * **EC3:** Patologías oculares ajenas a la córnea (retina, glaucoma).
  * **EC4:** Editoriales breves, cartas al editor o revisiones narrativas sin datos cuantitativos.

### C. Flujo de Selección de Artículos (Protocolo PRISMA Oficial)
```mermaid
flowchart TD
    A["1. Identificación (n = 101):<br>• Scopus (n = 84)<br>• IEEE Xplore (n = 17)"] --> B["2. Cribado Inicial (Screening):<br>Revisión por Título y Resumen (Zotero)"]
    B --> C["Excluidos por criterios EC (n = 68):<br>• Sin IA / puramente quirúrgicos (n = 38)<br>• Otras patologías no corneales (n = 18)<br>• Sin datos cuantitativos/revisiones narrativas (n = 12)"]
    B --> D["3. Elegibilidad:<br>33 artículos evaluados a texto completo"]
    D --> E["4. Matriz de Extracción Final (n = 16 a 18):<br>Llenados en papers/Referencias.xlsx (Anexo A)"]
```

---

## 5. Pipeline Técnico del Proyecto (Ingeniería de Software e IA)

```mermaid
flowchart LR
    A["142 Archivos Binarios<br>(71 Pacientes OD/OS)"] --> B["Módulo 1: Decodificación<br>Lectura NumPy y Cálculo STI"]
    B --> C["Módulo 2: Reconstrucción 2D<br>Mapas Polares (224x224 px)"]
    C --> D["Módulo 3: Partición Segura<br>Stratified Group 5-Fold (por Paciente)"]
    D --> E1["Módulo 4A: Baseline ML<br>SVM / Random Forest (STI tabular)"]
    D --> E2["Módulo 4B: Deep Learning<br>ResNet18 / EfficientNet (Transfer Learning)"]
    E1 & E2 --> F["Módulo 5: Evaluación<br>Matriz Confusión, ROC, F1"]
    E2 --> G["Módulo 6: Explicabilidad<br>Mapas Grad-CAM"]
```

### Detalle de Módulos de Software (`src/`):
1. **`src/data/` (Resultado 1):** Ingesta de archivos binarios crudos, extracción de la velocidad de fase de ondas de Lamb ($\sim 3500\text{ Hz}$), cálculo del índice $\text{STI}$ y generación de imágenes polarizadas $224 \times 224$ píxeles.
2. **`src/models/` (Resultado 2):** Pipeline de entrenamiento en PyTorch implementando validación cruzada estratificada por paciente (`GroupKFold`), modelos convolucionales preentrenados (`timm`/`torchvision`), y baselines en `scikit-learn`.
3. **`src/evaluation/` (Resultado 3):** Generación automática de matrices de confusión, curvas ROC multiclase, reportes de clasificación y mapas de calor explicables con **Grad-CAM**.

---

## 6. Mapeo de Entregables según Rúbrica PUCP (1INF42)

| Hito | Semana | Contenido Principal Requerido | Visto Bueno |
| :--- | :---: | :--- | :---: |
| **Cronograma** | Sem 1 (22-ago) | Cronograma formal del ciclo con avances semanales y reuniones de asesoría. | Asesor |
| **Entregable E1** | Sem 4 (12-sep) | Problemática (Árbol de problemas), Estado del arte (PRISMA + 3 PI), Objetivos con IOV, Cronograma y **Anexo A (`papers/Referencias.xlsx`)**. | Asesor $\rightarrow$ Profesor |
| **Entregable E2** | Sem 8 (09-oct) | Levantamiento de observaciones del E1, Marco conceptual/teórico/legal (Ley N° 29733 y FDA), Herramientas, métodos y procedimientos detallados. | Asesor $\rightarrow$ Profesor |
| **Entregable E3** | Sem 13 (14-nov) | Proyecto de fin de carrera completo: todas las correcciones, Anexo Plan de Proyecto (EDT, riesgos, presupuesto) y **Avance de un resultado (Resultado 1 y clasificador funcional)**. | Asesor $\rightarrow$ Jurado |
