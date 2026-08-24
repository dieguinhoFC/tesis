# 📋 Guía y Banco de Preguntas para el Asesor (Con Traducción Sencilla)

**Tema:** Clasificación de queratocono mediante modelos de aprendizaje profundo aplicados a mapas de rigidez corneal reconstruidos a partir de biomarcadores de velocidad de onda  
**Tesista:** Diego Silvestre  
**Asesor:** Dr. César Beltrán Castañón (IA / Metodología de Informática)  
**Co-asesor:** Dr. José Fernando Zvietcovich Zegarra (Grupo de Biofotónica / OCE / Datos)  
**Curso:** 1INF42 - Proyecto de Fin de Carrera 1 (2026-2)  

---

## 💡 El "Traductor Humano" (¿Qué significa cada cosa en lenguaje sencillo?)

| Concepto Técnico | ¿Qué significa en cristiano? | ¿Por qué me importa como tesista de informática? | ¿Cómo se lo digo al asesor? |
| :--- | :--- | :--- | :--- |
| **Archivos Binarios y Dimensiones** | Una foto normal (JPG) ya viene ordenada. Un archivo binario es una bolsa cerrada con millones de números sueltos. | Necesitamos saber cómo ordenar esos números en Python: cuántas filas, cuántas columnas y si tienen decimales (`float32`). | *"Dr., ¿cuántas filas y columnas tiene la matriz dentro del archivo binario?"* |
| **Scripts del Laboratorio** | El código que el equipo del doctor ya usó para hacer los dibujos de su presentación. | **Es tu mayor atajo:** si te pasan ese código, no inventamos nada de física, solo lo pasamos a Python. | *"Dr., ¿nos comparte el script (MATLAB o Python) con el que graficaron los ojos?"* |
| **Metadatos y Etiquetas** | El Excel que dice: Archivo 1 = Paciente Juan, Ojo Derecho, Sano. Archivo 2 = Paciente María, Ojo Izquierdo, Queratocono. | Sin esta lista de respuestas correctas, no podemos enseñarle nada a la IA. | *"Dr., ¿tienen el Excel con la lista de pacientes, ojo (OD/OS) y su diagnóstico?"* |
| **Data Leakage / Partición por Paciente** | Juan tiene ojo derecho e izquierdo. Como ambos ojos se parecen mucho, no podemos poner el derecho en la clase y el izquierdo en el examen porque la IA haría trampa. | Evita que el modelo memorice al paciente. Es lo que el jurado de la PUCP revisa para ponerte buena nota. | *"Dr., separaremos las pruebas por paciente completo para que la validación sea rigurosa."* |
| **Grad-CAM (Explicabilidad)** | Que la IA dibuje un círculo rojo sobre la imagen diciendo: *"Digo que está enfermo porque vi esta mancha aquí"*. | A los médicos no les gustan las "cajas negras"; necesitan ver en qué zona de la córnea se fijó la IA. | *"Dr., mostraremos mapas visuales para ver qué parte de la córnea detectó la red."* |

---

## 🟢 Fase 1: Lo Único Urgente para tus Primeras Semanas (E1 / Semanas 1 a 4)

> **Objetivo:** Conseguir los archivos y el código base para poder abrirlos en Python.

### 📌 Mensaje Directo para el Asesor (Copiar y pegar)
```text
Estimado Dr. Zvietcovich, buenas tardes:

Para ir preparando la estructura del proyecto y la lectura de los datos en Python:

1. ¿Nos podría compartir el código (en MATLAB o Python) que ustedes usaron para abrir los archivos binarios y generar las gráficas de velocidad/rigidez?
2. ¿Disponen de un archivo Excel con la lista de pacientes que indique a qué ojo pertenece cada archivo (derecho/izquierdo) y cuál es su diagnóstico clínico (Sano, Subclínico, Queratocono)?
3. ¿Cuáles son las dimensiones (filas x columnas) de los datos crudos?

Con estos insumos dejaremos listo el módulo de lectura de datos en Python. Muchas gracias.
```

---

## 🟡 Fase 2: Para el Entregable 2 (E2 / Semanas 5 a 8)

> **Objetivo:** Describir en el informe de Tesis cómo se procesan las señales y se crean las imágenes 2D.

1. **La fórmula del STI (Speed-Thickness Index):**
   * *Pregunta simple:* *"Dr., ¿cuál es la fórmula o recta de calibración que usan para calcular el STI a partir del espesor y la velocidad?"*
2. **Los ángulos de medición:**
   * *Pregunta simple:* *"¿En qué ángulos se tomaron las medidas (ej. 0°, 45°, 90°) para armar el círculo completo del ojo?"*
3. **El tamaño de la imagen final:**
   * *Pregunta simple:* *"¿Qué resolución en píxeles le parece adecuada para los mapas finales (ej. 224 x 224 píxeles)?"*

---

## 🟠 Fase 3: Para el Avance Práctico (E3 / Semanas 9 a 12)

> **Objetivo:** Mostrar los resultados de los modelos de Inteligencia Artificial funcionando.

1. **Comparación con métodos clásicos:**
   * *Pregunta simple:* *"Dr., además de la Red Neuronal (Deep Learning), ¿con qué métodos tradicionales comparamos los resultados? (ej. SVM o árboles de decisión sobre el promedio de rigidez)"*
2. **Validación visual con el médico:**
   * *Pregunta simple:* *"Dr., generamos estos mapas de atención (Grad-CAM) donde la IA marca la zona afectada; ¿coincide con la zona que ustedes identificaron clínicamente?"*
