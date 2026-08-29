# Plantilla para Redacción del Estado del Arte (E1)

Esta plantilla te ayudará a responder las Preguntas de Investigación (PI) basándote en la evidencia de los artículos seleccionados en tu PRISMA. 

**Instrucción:** Usa esta estructura para redactar la sección de revisión de la literatura en tu documento `Formato(2025).docx`. Rellena los espacios entre corchetes `[...]` con la información de tu matriz de extracción (Excel).

---

## Revisión de la Literatura y Estado del Arte

A continuación, se presentan los hallazgos de la revisión sistemática estructurados en torno a las tres preguntas de investigación planteadas.

### 1. Arquitecturas de Deep Learning en Elastografía y Biomecánica (PI 1)
*¿Qué arquitecturas de Deep Learning han demostrado mayor eficacia para la extracción automática de características espaciales en elastografía (OCE) o biomecánica corneal frente a modelos de Machine Learning clásico?*

La revisión de la literatura revela una clara tendencia hacia el uso de arquitecturas basadas en [CNNs / Transformadores / etc.] para el procesamiento de mapas de rigidez corneal. Autores como [Apellido del Autor 1, Año] demostraron que el uso de [Ej. ResNet-50] directamente sobre representaciones 2D de [ondas de Lamb / mapas OCE] evita la pérdida de información que sufren los enfoques tabulares tradicionales. Asimismo, estudios comparativos como el de [Apellido del Autor 2, Año] concluyen que el Deep Learning supera a algoritmos clásicos como [SVM / Random Forest] en un [X]% en términos de exactitud cuando se analizan mapas espaciales, debido a su capacidad para aprender asimetrías latentes.

*(Añade 1 o 2 párrafos más citando otros artículos que hablen sobre qué modelos son los más usados y por qué superan al ML tradicional).*

### 2. Impacto Diagnóstico en el Queratocono Subclínico (PI 2)
*¿En qué medida el uso de biomarcadores biomecánicos procesados por IA incrementa la sensibilidad y especificidad en la detección del queratocono subclínico, en comparación con las métricas de topografía corneal estándar?*

El diagnóstico temprano del queratocono subclínico (*Forme Fruste*) sigue siendo el principal desafío clínico. Sin embargo, la integración de la IA con parámetros de elastografía ha mostrado resultados prometedores. Investigaciones como las de [Autor 3, Año] evidencian que los biomarcadores biomecánicos detectan el debilitamiento corneal antes de que ocurran cambios morfológicos detectables por topografía (Pentacam). Al aplicar Deep Learning, el estudio de [Autor 4, Año] reportó una sensibilidad de [XX]% para casos subclínicos, superando ampliamente el [YY]% obtenido mediante índices topográficos estándar.

*(Añade más evidencia detallando cómo la biomecánica + IA logran aislar esos cambios sutiles que la topografía no ve).*

### 3. Limitaciones, Brechas y Explicabilidad Clínica (PI 3)
*¿Cuáles son las principales limitaciones, métricas de rendimiento esperadas y técnicas de explicabilidad reportadas para facilitar la adopción clínica de estos modelos?*

A pesar de los altos rendimientos (AUC-ROC promedios de [XX.X] reportados por [Autor 5, Año]), la literatura identifica barreras críticas para su traslación clínica. La principal limitación reportada en múltiples estudios ([Autor 6, Año]; [Autor 7, Año]) es el tamaño reducido de los datasets de OCE disponibles y el riesgo de sobreajuste. Para mitigar la falta de confianza de los oftalmólogos ("caja negra"), enfoques recientes han adoptado técnicas de explicabilidad visual. Por ejemplo, [Autor 8, Año] utilizó mapas de activación de clases (e.g., Grad-CAM) para confirmar que las redes neuronales se centran anatómicamente en la región del ápex del cono corneal, alineando así las predicciones computacionales con la fisiopatología esperada.

*(Termina con un párrafo conclusivo sobre cómo tu tesis abordará alguna de estas brechas).*
