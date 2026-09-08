# 1.2 Objetivos

## 1.2.1 Objetivo general

Desarrollar un modelo de clasificación basado en aprendizaje profundo aplicado a mapas espacio-temporales de propagación de ondas de Lamb/OCE para la identificación del estado corneal.

## 1.2.2 Objetivos específicos

O 1. Preparar una base de datos a partir del preprocesamiento de los múltiples mapas espacio-temporales por ojo, eliminando la necesidad de analizar de forma analítica cada meridiano.
O 2. Implementar un modelo de red neuronal profunda que evite la complejidad del cálculo matemático para clasificar los estadios del queratocono.
O 3. Evaluar el desempeño del modelo para garantizar la diferenciación del estado normal y subclínico ante la sutileza y el solapamiento biomecánico existente.

## 1.2.3 Resultados esperados por objetivos

Para el objetivo específico 1:
R 1. Pipeline de preprocesamiento y aumento de datos de las imágenes de mapas espacio-temporales.
R 2. Base de datos de mapas espacio-temporales estructurada y dividida adecuadamente para los procesos de entrenamiento, validación y prueb.

Para el objetivo específico 2:
R 3. Revisión sistemática de arquitecturas de redes neuronales profundas que han sido usadas para el procesamiento y clasificación de imágenes médicas.
R 4. Implementación computacional de la arquitectura de red neuronal profunda empleando transferencia de aprendizaje.
R 5. Modelo de clasificación entrenado para identificar de forma automática los estadios del queratocono.

Para el objetivo específico 3:
R 6. Comparación del desempeño diagnóstico del modelo entrenado para la diferenciación de los estados corneale.
R 7. Análisis e interpretación de las características extraídas por la red neuronal mediante mapas visuales, revelando los patrones biomecánicos ocultos que diferencian el estado normal del subclínico.

## 1.2.4 Mapeo de objetivos, resultados y verificación

En las Tablas 1, 2 y 3 se listan los resultados esperados asociados a cada objetivo específico, así como sus indicadores objetivamente verificables y sus respectivos medios de verificación.

*Tabla 1: Resultados esperados, indicadores y medios de verificación del objetivo específico 1.*

**Objetivo 1:** Preparar una base de datos a partir del preprocesamiento de los múltiples mapas espacio-temporales por ojo, eliminando la necesidad de analizar de forma analítica cada meridiano.

| Resultado | Indicador objetivamente verificable | Medio de verificación |
|---|---|---|
| R1. Pipeline de preprocesamiento y aumento de datos de las imágenes de mapas espacio-temporales. | • Código y documentación del pipeline que especifique al menos 3 técnicas de aumento de datos (*data augmentation*) y los pasos de limpieza y normalización.<br>• Validación del pipeline por parte de un especialista o asesor. | • Reporte detallado del pipeline de preprocesamiento y aumento de datos. |
| R2. Base de datos de mapas espacio-temporales estructurada y dividida adecuadamente para los procesos de entrenamiento, validación y prueba. | • Base de datos consolidada a partir de los mapas de 70 pacientes, ampliada mediante aumento de datos.<br>• División clara en subconjuntos de entrenamiento, validación y prueba (p. ej., 70%, 15%, 15%). | • Repositorio (o enlace de almacenamiento seguro) de la base de datos anonimizada.<br>• Reporte de la distribución y cantidad final de imágenes por cada conjunto de datos. |

*Tabla 2: Resultados esperados, indicadores y medios de verificación del objetivo específico 2.*

**Objetivo 2:** Implementar un modelo de red neuronal profunda que evite la complejidad del cálculo matemático para clasificar los estadios del queratocono.

| Resultado | Indicador objetivamente verificable | Medio de verificación |
|---|---|---|
| R3. Revisión sistemática de arquitecturas de redes neuronales profundas que han sido usadas para el procesamiento y clasificación de imágenes médicas. | • Comparación técnica de al menos 3 arquitecturas de redes neuronales profundas extraídas mediante revisión bibliográfica. | • Formulario de extracción de datos de la revisión sistemática.<br>• Documento de revisión sistemática del estado del arte. |
| R4. Implementación computacional de la arquitectura de red neuronal profunda empleando transferencia de aprendizaje. | • Código fuente de la arquitectura base implementada y adaptada usando transferencia de aprendizaje (*transfer learning*).<br>• Pruebas de integración del código superadas sin errores sintácticos. | • Repositorio de control de versiones (ej. GitHub) conteniendo los *scripts* de la arquitectura implementada. |
| R5. Modelo de clasificación entrenado para identificar de forma automática los estadios del queratocono. | • Un modelo de red neuronal que haya completado sus épocas de entrenamiento demostrando convergencia en la función de pérdida. | • Archivo ejecutable o de pesos del modelo entrenado (ej. `.h5`, `.pt`).<br>• Reporte de las gráficas de convergencia (función de pérdida y exactitud) durante el entrenamiento. |

*Tabla 3: Resultados esperados, indicadores y medios de verificación del objetivo específico 3.*

**Objetivo 3:** Evaluar el desempeño del modelo para garantizar la diferenciación del estado normal y subclínico ante la sutileza y el solapamiento biomecánico existente.

| Resultado | Indicador objetivamente verificable | Medio de verificación |
|---|---|---|
| R6. Comparación del desempeño diagnóstico del modelo entrenado para la diferenciación de los estados corneales. | • Un modelo de red neuronal que alcanza un rendimiento mínimo definido (p. ej., > 80% de exactitud o AUC) en la clasificación de las clases (normal, subclínico y queratocono). | • Reporte de métricas de desempeño (matriz de confusión, sensibilidad, especificidad, curvas ROC-AUC) ejecutadas sobre el conjunto de prueba. |
| R7. Análisis e interpretación de las características extraídas por la red neuronal mediante mapas visuales, revelando los patrones biomecánicos ocultos que diferencian el estado normal del subclínico. | • Generación de al menos un mapa visual de activación (ej. Grad-CAM) por cada estado clínico clasificado, que demuestre en qué zonas de la imagen se enfoca el modelo. | • Reporte de análisis cualitativo que adjunte las imágenes de los mapas visuales y la interpretación clínica/física de las características extraídas. |
