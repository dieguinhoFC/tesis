# Borrador para Entregable 1 (E1) - Tesis 1

*Instrucción: Copia y pega el contenido de las siguientes secciones directamente en tu documento `Formato(2025).docx` en los apartados correspondientes.*

---

## 1. Problemática
**Problema Central:** La extracción manual y el análisis matemático analítico (como la FFT-2D y el ajuste a modelos como mRLFE) de parámetros biomecánicos en los mapas espacio-temporales de velocidad de onda (OCE) hacen que la clasificación del queratocono (normal, subclínico y avanzado) sea un proceso lento, complejo y altamente dependiente de expertos.

**Causas:**
1.  **Limitación de parámetros topográficos:** La topografía describe únicamente cambios morfológicos y geométricos, sin proporcionar información directa sobre la rigidez corneal temprana.
2.  **Cuello de botella en el procesamiento analítico:** Calcular la rigidez corneal a partir de los datos crudos de OCE requiere aplicar transformadas matemáticas complejas.
3.  **Complejidad de la clasificación biomecánica:** Las sutiles diferencias de rigidez entre estadios tempranos (subclínico vs normal) son difíciles de aislar y clasificar de forma masiva mediante métodos manuales.

**Efectos:**
1.  **Inviabilidad clínica:** Una técnica tan precisa como la OCE no alcanza una aplicabilidad clínica masiva debido a su lentitud.
2.  **Riesgo de errores humanos:** Al depender de observaciones manuales, existen sesgos en la clasificación de los casos limítrofes.
3.  **Retraso en el diagnóstico:** El retraso en el resultado impide la aplicación oportuna de tratamientos (como el Cross-linking) que detengan el avance de la ectasia.

**Situación Deseada (Solución):** Extraer automáticamente características latentes directamente de los mapas polares 2D de elastografía mediante modelos de Deep Learning, evitando la pérdida de información del procesamiento analítico y capturando relaciones no lineales complejas para automatizar y acelerar la clasificación clínica.

---

## 2. Objetivos de la Investigación

**Objetivo General:**
Desarrollar y validar un pipeline computacional basado en redes neuronales convolucionales para la clasificación automatizada de queratocono (normal, subclínico y clínico) a partir de mapas espaciales de velocidad de onda (OCE), optimizando el tiempo de procesamiento y la precisión diagnóstica.

**Objetivos Específicos:**
1. Preprocesar y consolidar el dataset de mapas OCE provenientes de 142 córneas (71 pacientes) para su compatibilidad con arquitecturas profundas.
2. Diseñar y entrenar modelos de Deep Learning (ej. ResNet, EfficientNet) empleando transferencia de aprendizaje para extraer características latentes de los mapas de rigidez.
3. Evaluar el rendimiento diagnóstico del modelo mediante métricas de clasificación multiclase (AUC-ROC, F1-Score) y métodos de interpretabilidad visual (Grad-CAM).

---

## 3. Resultados Esperados e IOVs

*   **Resultado 1 (vinculado al Objetivo Específico 1):** Dataset estructurado, balanceado y particionado mediante validación cruzada por grupos (Group K-Fold).
    *   **Indicador Objetivamente Verificable (IOV):** Repositorio de datos/metadatos documentado y versionado en formato CSV/HDF5.
*   **Resultado 2 (vinculado al Objetivo Específico 2):** Algoritmo de clasificación basado en aprendizaje profundo entrenado y optimizado.
    *   **Indicador Objetivamente Verificable (IOV):** Repositorio de código (GitHub) conteniendo los scripts de entrenamiento y los pesos del modelo final guardados (archivos `.pth` o `.h5`).
*   **Resultado 3 (vinculado al Objetivo Específico 3):** Reporte técnico de validación del modelo con su respectiva interpretabilidad clínica.
    *   **Indicador Objetivamente Verificable (IOV):** Documento de reporte técnico detallando matrices de confusión, curvas AUC-ROC y mapas de calor (activación Grad-CAM) con validación oftalmológica.

---

## 4. Revisión de la Literatura y Estado del Arte (Protocolo de Búsqueda)

**Preguntas de Investigación (PI):**
*   **PI 1:** ¿De qué manera las arquitecturas de Inteligencia Artificial permiten analizar directamente datos crudos espaciales o espacio-temporales (topografía o biomecánica), automatizando la extracción de características para la detección del queratocono?
*   **PI 2:** ¿Qué tan efectiva es la clasificación automatizada con Inteligencia Artificial para diferenciar el queratocono subclínico de una córnea normal, y qué rol juegan los diferentes tipos de biomarcadores de entrada en su desempeño?
*   **PI 3:** ¿De qué manera la integración de técnicas de explicabilidad visual (como mapas Grad-CAM) contribuye a la validación clínica de las predicciones de IA en el diagnóstico temprano del queratocono?

**Estrategia de Búsqueda:**
Se diseñó una estrategia sistemática basada en la metodología PRISMA, empleando cadenas de búsqueda booleanas que combinan términos referentes al problema (Queratocono), la intervención (Elastografía OCE / Biomecánica) y la tecnología (Inteligencia Artificial / Deep Learning). Las búsquedas se ejecutaron en las bases de datos Scopus e IEEE Xplore, obteniendo un total inicial de aproximadamente 100 documentos, los cuales fueron tamizados por título y resumen bajo estrictos criterios de inclusión (estudios cuantitativos que apliquen ML/DL en estadios tempranos/subclínicos de queratocono usando datos espaciales corneales, topográficos o biomecánicos) y exclusión (estudios sin enfoque computacional, sin métricas, u orientados a otras patologías).

*(Nota para el tesista: Después de este párrafo, debes redactar las respuestas a las 3 PI basándote en la evidencia de los artículos que leíste y resumiste en tu matriz de Excel).*
