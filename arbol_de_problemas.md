. 

# Árbol de Problemas: Detección de Queratocono con OCE

**Problema Central:** La extracción y el análisis analítico/manual de parámetros biomecánicos en los mapas espacio-tiempo de velocidad de onda (OCE) hacen que la clasificación del queratocono (normal, subclínico, avanzado) sea un proceso lento, complejo y dependiente de expertos.

```mermaid
graph BT
    %% Definición de nodos de Raíces (Causas)
    C1["<b>Limitación de parámetros topográficos:</b><br/>La topografía describe únicamente cambios morfológicos<br/>y geométricos, sin proporcionar información directa<br/>sobre la rigidez corneal temprana."]
  
    C2["<b>Cuello de botella en el procesamiento analítico:</b><br/>Calcular la rigidez corneal a partir de los datos brutos<br/>de OCE requiere aplicar transformadas matemáticas (FFT-2D)<br/>y ajustes a modelos físicos complejos (mRLFE)."]
  
    C3["<b>Complejidad de la clasificación biomecánica:</b><br/>Las sutiles diferencias de rigidez entre estadios<br/>(subclínico vs normal) son difíciles de aislar y<br/>clasificar de forma masiva mediante métodos manuales."]

    %% Nodo del Problema Central
    PR((("<b>PROBLEMA RAÍZ:</b><br/>La extracción manual y el análisis matemático de<br/>características en los mapas espacio-tiempo de<br/>velocidad de onda (OCE) hacen que la clasificación<br/>del queratocono sea un proceso lento y complejo.")))

    %% Definición de nodos de Ramas (Efectos)
    E1["<b>Inviabilidad clínica:</b><br/>Una técnica tan precisa como la OCE se queda atrapada<br/>en el laboratorio porque no es lo suficientemente rápida<br/>o automática para usarse en las clínicas oftalmológicas."]
  
    E2["<b>Riesgo de errores humanos:</b><br/>Al depender de la observación manual de la gráfica<br/>espacio-tiempo, puede haber sesgos o errores en la<br/>clasificación de los casos limítrofes (subclínicos)."]
  
    E3["<b>Retraso en el diagnóstico:</b><br/>Si el médico no tiene el resultado rápido, se pierde<br/>la oportunidad de aplicar un tratamiento oportuno<br/>para detener el avance de la enfermedad."]

    %% Conexiones Raíces -> Problema Central
    C1 --> PR
    C2 --> PR
    C3 --> PR

    %% Conexiones Problema Central -> Efectos
    PR --> E1
    PR --> E2
    PR --> E3

    %% Estilos de los nodos
    style PR fill:#f9d0c4,stroke:#e06666,stroke-width:3px,color:#000
    style C1 fill:#d9ead3,stroke:#93c47d,stroke-width:2px,color:#000
    style C2 fill:#d9ead3,stroke:#93c47d,stroke-width:2px,color:#000
    style C3 fill:#d9ead3,stroke:#93c47d,stroke-width:2px,color:#000
    style E1 fill:#cfe2f3,stroke:#6fa8dc,stroke-width:2px,color:#000
    style E2 fill:#cfe2f3,stroke:#6fa8dc,stroke-width:2px,color:#000
    style E3 fill:#cfe2f3,stroke:#6fa8dc,stroke-width:2px,color:#000
```
