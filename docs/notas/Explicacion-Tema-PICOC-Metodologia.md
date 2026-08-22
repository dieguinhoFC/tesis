# 🧠 Bitácora de Entendimiento: Tema de Tesis, PICOC y Metodología

**Tema:** Clasificación de queratocono mediante modelos de aprendizaje profundo aplicados a mapas de rigidez corneal reconstruidos a partir de biomarcadores de velocidad de onda  
**Estudiante:** Diego Silvestre  
**Asesor:** Dr. José Fernando Zvietcovich Zegarra  
**Curso:** 1INF42 - Proyecto de Fin de Carrera 1 (2026-2)  

---

## 1. El Fundamento Clínico y Físico (¿Qué es todo esto?)

### A. Los 3 Grupos Clínicos de Clasificación
1. **Normal (Control):** Córnea sana, con elasticidad homogénea y grosor adecuado.
2. **Queratocono Subclínico / Forme Fruste (*FFKC*):** Córnea en etapa temprana. Por fuera (geometría/curvatura) se ve aparentemente normal, pero internamente ya perdió rigidez ("se ablandó"). **Es el núcleo de valor e innovación de la tesis**, ya que detectarlo previene errores en cirugías refractivas (pre-LASIK).
3. **Queratocono Clínico (*KC I, KC II, KC III*):** Córnea patológica avanzada con deformación cónica evidente.

### B. La Técnica Física (OCE + Ondas de Lamb)
* **Elastografía por Coherencia Óptica (OCE):** Mediante un pulso acústico/láser se genera una perturbación mecánica en la córnea.
* **Ondas de Lamb (*Lamb waves*):** Son las ondas que viajan a través del tejido corneal. 
  * En tejido duro y sano $\rightarrow$ La onda viaja **rápido**.
  * En tejido blando/gelatinoso (queratocono) $\rightarrow$ La onda viaja **lenta**.

### C. Los Biomarcadores de las Diapositivas
* **STI (*Speed-Thickness Index*):** En ojos sanos existe una **regresión lineal** entre el espesor ($\mu m$) y la velocidad de onda ($m/s$). Cuando el tejido está ablandado, los valores caen por debajo de la normalidad ($\text{STI} < 0$, ej. $-0.38$ en subclínico y $-1.22$ en queratocono).
* **Mapas 2D de Rigidez / STI:** Representación polar en 2D donde el **azul** indica rigidez sana y el **amarillo/rojo** indica la zona ablandada del cono (*cone*).
* **SAWS (*Spatial Anisotropy of Wave Speed*):** Mide la asimetría de propagación de la onda en diferentes ángulos/meridianos ($0^\circ, 22.5^\circ, 45^\circ, 67.5^\circ, 90^\circ$).

---

## 2. El Aporte de Informática (Tu Tesis)

* **Entrada:** Mapas 2D de calor de rigidez corneal / STI provenientes de los 70 pacientes del grupo de biofotónica.
* **Modelo:** Redes Neuronales Convolucionales (**CNNs: ResNet / EfficientNet**) con transfer learning y data augmentation.
* **Salida:** Clasificación multiclase automática en las 3 categorías (**Normal**, **Subclínico**, **Queratocono**).

---

## 3. Protocolo PICOC y Preguntas de Investigación (PI)

| Componente | Definición en tu Tesis |
| :--- | :--- |
| **P** *(Population)* | Córneas categorizadas en 3 clases: Normal, Queratocono Subclínico (*Forme Fruste*) y Queratocono Clínico (70 ojos con OCE). |
| **I** *(Intervention)* | Modelos de Deep Learning (ResNet, EfficientNet) sobre mapas 2D de rigidez / velocidad de ondas de Lamb. |
| **C** *(Comparison)* | Topografía geométrica clásica (Pentacam/OCT), regresión lineal escalar básica y ML clásico (SVM, Random Forest). |
| **O** *(Outcome)* | Exactitud ($\ge 90\%$), Macro F1, AUC-ROC ($\ge 0.92$) y alta sensibilidad en la detección de Queratocono Subclínico. |
| **C** *(Context)* | Sistemas CAD para screening preoperatorio en oftalmología (prevención de ectasias post-LASIK). |

### Las 3 Preguntas de Investigación para el E1:
* **PI1 (Modelos):** *¿Qué arquitecturas de Deep Learning (ResNet, EfficientNet) son más efectivas para la clasificación multiclase a partir de mapas 2D médicos?*
* **PI2 (Biomarcadores):** *¿De qué manera los biomarcadores de OCE (velocidad de Lamb, STI, SAWS) permiten discriminar estadios subclínicos frente a la topografía estándar?*
* **PI3 (Métricas y Limitaciones):** *¿Qué métricas diagnósticas se alcanzan y cómo se mitiga el desbalance de clases en datasets clínicos reducidos?*

---

## 4. Flujo de Trabajo con Zotero y Excel (PRISMA)

1. **Zotero:** Contiene los 84 resultados importados. Se hace un cribado rápido por Título y Resumen para filtrar de 84 a ~15-20 artículos elegibles.
2. **Excel (`papers/Referencias.xlsx`):** Contiene el protocolo PICOC y la matriz de extracción de 14 columnas que se adjunta como **Anexo A** en el Entregable E1.
