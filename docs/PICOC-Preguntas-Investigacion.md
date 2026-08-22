# 🎯 Formulación Metodológica: PICOC y Preguntas de Investigación

**Tema:** Clasificación de queratocono mediante modelos de aprendizaje profundo aplicados a mapas de rigidez corneal reconstruidos a partir de biomarcadores de velocidad de onda  
**Estudiante:** Diego Silvestre  
**Asesor / Co-asesor:** Dr. José Fernando Zvietcovich Zegarra (Grupo de Biofotónica / OCE - ISER 2024)  
**Curso:** 1INF42 - Proyecto de Fin de Carrera 1 (2026-2)  

---

## 1. Contexto Clínico y Físico del Proyecto (OCE + Ondas de Lamb)

La investigación se basa en la adquisición de datos mediante **Elastografía por Coherencia Óptica (OCE - Optical Coherence Elastography)**:
1. **Excitación y Propagación:** Se induce una perturbación mecánica/óptica en la córnea y se captura la propagación de **ondas de Lamb (*Lamb waves*)** en múltiples meridianos angulares ($0^\circ, 22.5^\circ, 45^\circ, 67.5^\circ, 90^\circ$).
2. **Estimación de Velocidad:** Mediante mapas espacio-tiempo ($x$ vs $t$) y transformada 2D FFT, se extrae la velocidad de la onda de Lamb ($\approx 3500\text{ Hz}$).
3. **Biomarcadores Físicos de Entrada:**
   * **STI (*Speed-Thickness Index* / Índice Velocidad-Espesor):** Relación lineal entre el espesor corneal ($\mu m$) y la velocidad de onda ($m/s$). La pérdida de rigidez ("tejido blando/gelatinoso") genera desviaciones por debajo de la banda de regresión normal ($\text{STI} < 0$, valores negativos).
   * **SAWS (*Spatial Anisotropy of Wave Speed*):** Cuantifica la asimetría y anisotropía espacial (NFA) entre meridianos, significativamente elevada en córneas patológicas y subclínicas.
   * **Mapas 2D de Rigidez / STI:** Reconstrucción espacial en 2D (mapa de calor polar) de la rigidez y velocidad de onda de la córnea.

---

## 2. Esquema de Clasificación Multiclase (3 Categorías)

1. **Normal (Control):** Córneas con elasticidad homogénea y valores $\text{STI} \ge 0$ dentro de los intervalos de confianza del 95%.
2. **Queratocono Subclínico / Forme Fruste (*FFKC*):** Córneas asintomáticas y con topografía geométrica normal, pero con ablandamiento focal biomecánico ($\text{STI} \approx -0.38$, anisotropía aumentada). **Núcleo de innovación de la tesis.**
3. **Queratocono Clínico (*KC I, II, III*):** Córneas con daño biomecánico severo ($\text{STI} \le -1.22$), cono focalizado evidente y pérdida estructural.

---

## 3. Marco PICOC Formal

| Componente | Definición | Aplicación en la Tesis |
| :--- | :--- | :--- |
| **P** *(Population)* | Población / Muestra | Pacientes (70 ojos) categorizados en 3 grupos clínicos: **Normales**, **Queratocono Subclínico (*Forme Fruste*)** y **Queratocono Clínico**, caracterizados mediante elastografía OCE y ondas de Lamb. |
| **I** *(Intervention)* | Intervención / Propuesta | Modelos de **Aprendizaje Profundo (CNNs: ResNet, EfficientNet)** para clasificación multiclase automática a partir de **mapas 2D de rigidez / STI** derivados de la velocidad de ondas de Lamb. |
| **C** *(Comparison)* | Comparación | • Diagnóstico geométrico estándar (topografía Pentacam/OCT) ciego al ablandamiento subclínico.<br>• Modelos de regresión lineal simple o umbrales escalares de STI sin análisis espacial profundo.<br>• Modelos clásicos de ML (SVM, Random Forest). |
| **O** *(Outcome)* | Métricas y Resultados | • Métricas multiclase: Matriz de confusión, Exactitud (Accuracy $\ge 90\%$), Macro F1-score y AUC-ROC ($\ge 0.92$).<br>• Alta sensibilidad y especificidad en la detección de la clase **Queratocono Subclínico**.<br>• Reducción de la variabilidad inter-observador. |
| **C** *(Context)* | Contexto Clínico | Diagnóstico asistido por computadora (CAD) en centros oftalmológicos para evaluación preoperatoria de cirugía refractiva (pre-LASIK) para evitar ectasias iatrogénicas. |

---

## 4. Preguntas de Investigación (PI) para el Estado del Arte (E1)

* **PI1 (Modelos de Aprendizaje Profundo Multiclase):**  
  > *¿Qué arquitecturas de redes neuronales convolucionales (ej. ResNet, EfficientNet) y técnicas de transfer learning / data augmentation ofrecen mejor desempeño para la clasificación multiclase (Normal, Subclínico y Queratocono) a partir de mapas de calor 2D médicos?*

* **PI2 (Biomarcadores de OCE y Ondas de Lamb):**  
  > *¿De qué manera los biomarcadores biomecánicos basados en elastografía OCE (velocidad de ondas de Lamb, índice STI y anisotropía espacial SAWS) permiten identificar alteraciones tisulares en estadios subclínicos frente a parámetros topográficos convencionales?*

* **PI3 (Desempeño Diagnóstico, Desbalance y Limitaciones):**  
  > *¿Qué métricas de exactitud, F1 y AUC-ROC se alcanzan en la literatura para la detección temprana de ectasias corneales y qué estrategias se utilizan para mitigar el desbalance de clases en datasets clínicos reducidos?*

---

## 5. Cadenas de Búsqueda Booleanas (Scopus / IEEE Xplore)

```sql
( "keratoconus" OR "corneal ectasia" OR "forme fruste" OR "subclinical keratoconus" )
AND ( "deep learning" OR "convolutional neural network" OR "CNN" OR "ResNet" OR "EfficientNet" )
AND ( "optical coherence elastography" OR "OCE" OR "Lamb wave" OR "wave speed" OR "shear wave" OR "stiffness map" OR "corneal biomechanics" )
AND ( "classification" OR "detection" OR "early diagnosis" OR "multiclass" )
```
