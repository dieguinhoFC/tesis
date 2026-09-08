satelitales del satélite PeruSat-1 en la determinación automática del nivel socioeconómico de áreas urbanas.

# 1.2 Objetivos

## 1.2.1 Objetivo general

Desarrollar un modelo de análisis de imágenes satelitales basado en redes neuronales profundas para la identificación automática del nivel socioeconómico de zonas urbanas.

## 1.2.2 Objetivos específicos

O1. Integrar datos visuales con datos censales

O2. Elaborar un criterio automático de los resultados de determinación del nivel socioeconómico

O3. Desarrollar una plataforma para el aprovechamiento oportuno de la información socioeconómica obtenida a través del criterio automático

## 1.2.3 Resultados esperados

O 1. **Integrar** datos visuales con datos censales

- R1. Conjunto de imágenes satelitales con regiones etiquetadas en base a los datos censales

O 2. **Elaborar** un criterio automático de los resultados de determinación del nivel socioeconómico

- R1. Protocolo de preprocesamiento de imágenes satelitales etiquetadas para su procesamiento por parte de los modelos de red neuronal
- R2. Modelo de arquitectura de red neuronal para la segmentación semántica de regiones urbanas en base a techos implementado
- R3. Modelo de arquitectura basado en red neuronal convolucionales para la extracción de variables socioeconómicas en imágenes satelitales implementado

O 3. **Desarrollar** una plataforma para el aprovechamiento oportuno de la información socioeconómica obtenida a través del criterio automático

- R1. Interfaz de Programación de Aplicaciones (API) para el uso automático del modelo de redes convolucionales
- R2. Interfaz Gráfica de Usuario (GUI) para la visualización de los resultados del modelo
- R3. Integración de los componentes del sistema (*back-end* y *front-end*)

## 1.2.4 Mapeo de objetivos, resultados y verificación

En las Tablas 1, 2 y 3 se listan los resultados esperados asociados a cada objetivo específico, así como sus indicadores y sus respectivos medios de verificación.

*Tabla 1: Resultados esperados, indicadores y medios de verificación del objetivo específico 1.*

**Objetivo:** Integrar datos visuales con datos censales

| Resultado | Indicador objetivamente verificable | Medio de verificación |
|---|---|---|
| R1. Conjunto de imágenes satelitales con regiones etiquetadas en base a los datos censales | • Al menos 5 distritos de la ciudad con información censal de nivel socioeconómico<br>• Un mapa de imagen satelital del mismo periodo censal<br>• Un mapa de niveles socioeconómicos etiquetados de acuerdo con información censal | • Repositorio de información censal de al menos 5 distritos de la ciudad<br>• Base de datos de imágenes satelitales correspondientes al mismo periodo censal<br>• Base de datos de imágenes etiquetadas de acuerdo con información censal |

*Tabla 2: Resultados esperados, indicadores y medios de verificación del objetivo específico 2 (Elaboración propia).*

**Objetivo:** elaborar un criterio automático de los resultados de determinación del nivel socioeconómico

| Resultado | Indicador objetivamente verificable | Medio de verificación |
|---|---|---|
| R1. Protocolo de preprocesamiento de imágenes satelitales etiquetadas para su procesamiento por parte de los modelos de red neuronal | • Protocolo de preprocesamiento de imágenes satelitales validado por un especialista | • Reporte de descripción del protocolo |
| R2. Modelo de arquitectura de red neuronal para la segmentación semántica de regiones urbanas en base a techos implementado | • Un modelo de red neuronal optimizado de al menos 70,0 % de precisión para la segmentación | • Diagrama de la arquitectura del modelo de red neuronal de segmentación implementado<br>• Repositorio de código, el cual contiene la implementación del modelo de segmentación<br>• Reporte de resultados de ejecución de pruebas de optimización al modelo |
| R3. Modelo de arquitectura basado en red neuronal convolucionales para la extracción de variables socioeconómicas en imágenes satelitales implementado | • Un modelo de red neuronal optimizado de al menos 70,0 % de precisión para la determinación del nivel socioeconómico | • Diagrama de la arquitectura del modelo de red neuronal de extracción de variables socioeconómicas implementado<br>• Repositorio de código del modelo de extracción de variables socioeconómicas<br>• Reporte de resultados de ejecución de pruebas de optimización al modelo |

*Tabla 3: Resultados esperados, indicadores y medios de verificación del objetivo específico 3 (Elaboración propia).*

**Objetivo:** desarrollar una plataforma para el aprovechamiento oportuno de la información socioeconómica obtenida a través del criterio automático

| Resultado | Indicador objetivamente verificable | Medio de verificación |
|---|---|---|
| R1. Interfaz de Programación de Aplicaciones (API) para el uso automático del modelo de redes convolucionales | • Pruebas unitarias aprobadas al 100%<br>• Pruebas funcionales aprobadas al 100 % | • Repositorio de código fuente del API<br>• Reporte de resultados de ejecución de pruebas unitarias y funcionales del API<br>• Documentación descriptiva de funcionalidades de la API |
| R2. Interfaz Gráfica de Usuario (GUI) para la visualización de los resultados del modelo | • Pruebas unitarias aprobadas al 100%<br>• Pruebas funcionales aprobadas al 100 % | • Repositorio de código fuente de la GUI<br>• Reporte de resultados de ejecución de pruebas unitarias y funcionales de la GUI<br>• Manual de usuario para la manipulación de la GUI |
| R3. Integración de los componentes del sistema (*back-end* y *front-end*) | • Pruebas funcionales aprobadas al 100 % | • Sistema desplegado en un servidor local<br>• Reporte de resultados de ejecución de pruebas funcionales |

# 1.3 Métodos y Procedimientos

En esta sección se mencionan y explican las herramientas, métodos y procedimientos a emplear para el desarrollo de este proyecto de fin de carrera.

## 1.3.1 Herramientas, métodos y procedimientos a usar

Se menciona, a continuación, las herramientas a emplear y procedimientos a seguir, asociados con cada resultado esperado de este proyecto (ver Tabla 4).

*Tabla 4: Resultados esperados, herramientas a usar y métodos a utilizar en el proyecto (Elaboración propia).*

| Resultado esperado | Herramienta a utilizar | Métodos a utilizar |
|---|---|---|
| Conjunto de imágenes satelitales con regiones etiquetadas en base a los datos censales | • QGIS<br>• Python<br>• Rasterio<br>• SQLite<br>• NumPy<br>• GitHub<br>• Bash | • Refinamiento pancromático |
| Modelo de segmentación semántica de regiones urbanas en base a techos<br><br>Modelo automático basado en redes neuronales convolucionales para la extracción de variables socioeconómicas en imágenes satelitales | • Python<br>• GitHub<br>• PyTorch<br>• Rasterio<br>• NumPy<br>• Matplotlib | • Algoritmos de aprendizaje supervisados<br>• Algoritmos de aprendizaje no supervisado<br>• Intersección sobre Unión (índice Jaccard) |
| Interfaz de Programación de Aplicaciones (API) para el uso automático del modelo de redes convolucionales | • Python<br>• GitHub<br>• PyTorch<br>• Flask<br>• Rasterio | • API REST<br>• Georreferenciación |
| Interfaz Gráfica de Usuario (GUI) para la visualización de los resultados del modelo | • JavaScript<br>• GitHub<br>• React.js | |

## 1.3.2 Descripción de las herramientas, métodos y procedimientos a usar

En esta sección, se describirá las herramientas y procedimientos a usar en el presente proyecto, que fueron mencionados en la sección anterior, y se explicará cómo se planea emplear en el mismo.

### Herramientas

**QGIS**

QGIS es un sistema de información de código abierto para la lectura y manipulación de información geográfica. Permite abrir y crear diferentes tipos de archivos georreferenciados, tales como imágenes satelitales o mapas de polígonos (Open Source Geospatial Foundation, s.f.).

En el presente proyecto, se empleará dicha herramienta para la conversión de las etiquetas georreferenciadas en un formato manejable por el resto de las herramientas.

**Rasterio**

Rasterio es una biblioteca de Python para la extracción y manipulación de imágenes ráster georreferenciadas, tanto los píxeles en sí como los metadatos asociados a la imagen (Mapbox, 2018).

En el presente proyecto, Rasterio cumple la función de transformar las imágenes desde el formato ráster hasta una forma matricial, de forma que sea manipulable durante el etiquetado y durante el procesamiento por los modelos. Asimismo, permitirá leer la ubicación de dicha imagen en la superficie terrestre, lo que ayuda a su visualización en un mapa virtual.

**SQLite**

SQLite es una biblioteca en lenguaje C que implementa un motor de base de datos SQL pequeño, rápido, autónomo, de alta confiabilidad y con todas las funciones. (Consorcio SQLite, s.f)

En el presente proyecto, se empleará esta herramienta para el almacenamiento y acceso a las etiquetas de nivel socioeconómico asociadas a las zonas urbanas del presente proyecto final de carrera.

**Python**

Python es un lenguaje de programación de alto nivel, interpretado y multiparadigma; es decir, permite la codificación mediante más de un paradigma de programación, sea programación orientada a objetos, programación funcional o programación imperativa; administrado por la Python Software Foundation (Python Software Foundation, s.f.).

Se ha elegido este lenguaje para la elaboración del modelo como de la interfaz de programación de aplicaciones, debido a diferentes motivos. En primer lugar, debido a la existencia de bibliotecas diseñadas para la implementación de modelos de aprendizaje automático, las cuales son compatibles con el tipo de modelos a desarrollar, así como de bibliotecas para la manipulación de imágenes satelitales y sus etiquetas asociadas. Por otro lado, debido a la presencia de los módulos necesarios para la implementación de las API.

**GitHub**

GitHub es una plataforma de colaborativo que permite mantener un control de versiones del código fuente de un proyecto mientras este se almacena de forma remota y accesible mediante la web (GitHub, s.f.).

El código fuente desarrollado en el marco del presente proyecto será almacenado y controlado empleando dicha herramienta, de forma que su acceso no dependa de algún equipo que se disponga y que pueda manejarse un control de cambios durante la duración del proyecto.

**Bash**

Bash es un lenguaje de órdenes y *shell* de Unix escrito por Brian Fox como un reemplazo de software libre para el shell Bourne en el proyecto GNU (Ramey en Hamilton, 2011).

En el presente proyecto, esta herramienta permitirá la manipulación y tratamiento previo de las imágenes satelitales de forma que estén aptas para su integración con los datos censales.

**PyTorch**

PyTorch es un marco de trabajo de código abierto orientado al desarrollo y despliegue de modelos de aprendizaje automático en Python. Este incluye, principalmente, métodos para el procesamiento de matrices, componentes para la construcción de redes neuronales y modelos preentrenados (Facebook, s.f. b).

En el proyecto, se emplea dicho marco de trabajo en la implementación de los modelos de redes neuronales convolucionales en el análisis de las imágenes satelitales para la extracción de variables socioeconómicas.

**NumPy**

NumPy es un proyecto de código abierto que permite la computación numérica en Python. El código fuente del módulo se encuentra disponible desde GitHub (Numpy, s.f.).

Los módulos mencionados anteriormente emplean estructuras definidas en NumPy para la representación de sus datos numéricos, por lo que, en el proyecto, esta biblioteca permitirá manipular y transformar dichas estructuras.

**Matplotlib**

Matplotlib es una biblioteca de Python para la visualización de datos estática, dinámica e interactiva (Hunter. 2007).

Se empleará esta biblioteca para el análisis gráfico del comportamiento de los datos y los resultados obtenidos tras el procesamiento de los mismos a través del modelo de redes neuronales propuesto.

**Flask**

Flask es un marco de trabajo para el desarrollo de aplicaciones web que cumple la función de interfaz de puerta de enlace de servicios web (WSGI). Se caracteriza por consistir en un mínimo de componentes para su funcionamiento y su capacidad de escalar a aplicaciones más complejas (Ronacher, s.f.).

En el proyecto, será empleado para la implementación de las interfaces de programación de aplicaciones (API), uno de los resultados esperados mencionados en la sección anterior, de forma que pueda comunicarse con la interfaz gráfica de usuario, otro resultado esperado de este proyecto de fin de carrera, para la ejecución automática del modelo de extracción del nivel socioeconómico.

**JavaScript**

JavaScript es un lenguaje de programación interpretado y multiparadigma (permite la programación imperativa, declarativa y orientada a objetos) empleado mayoritariamente como una herramienta de *scripting* para entornos web (Mozilla Foundation, s..f).

Este lenguaje de programación será empleado en el presente proyecto para la implementación de la interfaz gráfica de usuario planteada como resultado esperado para el objetivo 3, de forma que los resultados del modelo de extracción de variables socioeconómicas sean posibles de visualizar por sus usuarios finales sin necesitar conocer el funcionamiento del modelo en sí.

**React**

React es una biblioteca diseñada para la construcción de interfaces gráficas de usuario. Disponible para JavaScript, es una biblioteca declarativa y basada en componentes encapsulados (Facebook, s.f. a).

Para el presente proyecto, este será empleado en la construcción de la interfaz gráfica de usuario descrita anteriormente y que constituye un resultado esperado. Este marco de trabajo se comunicará con la interfaz de programación de aplicaciones descrita y consumirá los servicios que requiera durante su funcionamiento.

### Métodos y procedimientos

**Refinado pancromático**

Conocido también como *pansharpening*, es un tipo de fusión de datos que se refiere al proceso de de combinar píxeles de color de menor resolución con los píxeles pancromáticos de mayor resolución para producir una imagen de color de alta resolución (Padwick, Deskevich, Pacifici, Smallwood, 2010).

**Algoritmos de aprendizaje automático supervisados**

Los algoritmos de aprendizaje automático supervisado son modelos computacionales que para su entrenamiento requieren de datos etiquetados previamente, los cuales sirven como base para el ajuste de los parámetros del modelo (Bishop, 2006).

**Algoritmos de aprendizaje automático no supervisados**

Los algoritmos de aprendizaje automático no supervisado son algoritmos de aprendizaje automático cuya data de entrenamiento es generada de manera autónoma. Esto debido a ciertos factores, aunque por lo general se da cuando el proceso de etiquetado resulta particularmente tedioso, o si se necesita empezar a procesar un video al mismo instante en que está disponible (Bishop, 2006).

**Intersección sobre Unión (índice Jaccard)**

La intersección sobre unión, también conocida como índice Jaccard, es una métrica sobre la similitud de dos conjuntos (Raimundo & Vargas, 1996). Para dos conjuntos A y B, su cálculo se daría de la siguiente manera:

$$IoU = \frac{|A \cap B|}{|A \cup B|}$$

en la que A ∪ B representa la unión de los conjuntos A y B mientras que A ∩ B, su intersección.

Se empleará dicha métrica para este proyecto en la evaluación de la eficacia del modelo respecto de la tarea de segmentación de imágenes satelitales de PeruSAT-1. Para ello, los conjuntos a comparar son las etiquetas generadas por el modelo y las etiquetas reales de los datos empleados para el entrenamiento de dichos modelos.

**API REST**

Una interfaz de programación de aplicaciones de transferencia de estado representacional (API REST) es un conjunto de definiciones y protocolos que se usa para diseñar e integrar el software de aplicaciones, las cuales siguen un conjunto de principios, mencionados a continuación:

- Arquitectura cliente-servidor, cuyas partes se comunican mediante HTTP
- Cada comunicación entre el cliente y el servidor no presenta estado y es independiente de la otra.
- Los datos son almacenables en caché.
- Transferencia estandarizada de datos entre cliente y servidor
- Un sistema en capas que organiza en jerarquías invisibles (Red Hat, s.f.)

En el presente proyecto, se empleará REST para la implementación de las interfaces de programación de aplicaciones, debido a su simpleza en manejo y facilidad de entendimiento.

**Georreferenciación**

De acuerdo con ArcGIS Resources (s.f.):

La georreferenciación es el uso de coordenadas de mapa para asignar una ubicación espacial a entidades cartográficas. Todos los elementos de una capa de mapa tienen una ubicación geográfica y una extensión específicas que permiten situarlos en la superficie de la Tierra o cerca de ella. La capacidad de localizar de manera precisa las entidades geográficas es fundamental tanto en la representación cartográfica como en SIG.

En este proyecto de fin de carrera, se empleará la georreferenciación para ubicar las imágenes satelitales en el mapa, de acuerdo con sus metadatos.
