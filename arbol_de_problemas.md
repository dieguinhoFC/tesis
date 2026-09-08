.

# Árbol de Problemas: Detección de Queratocono con OCE

**Problema Central:** La extracción y el análisis analítico/manual de parámetros biomecánicos en los mapas espacio-tiempo de velocidad de onda (OCE) hacen que la clasificación del queratocono (normal, subclínico, avanzado) sea un proceso lento, complejo y dependiente de expertos.

```mermaid
graph BT
    %% Definición de nodos de Raíces (Causas)
    C1["<b>Complejidad para procesar y analizar de forma analítica múltiples mapas espacio-tiempo por cada ojo de manera escalable</b><br/> Para capturar cómo varía la rigidez en diferentes direcciones de la córnea, el sistema adquiere mapas de velocidad de onda en múltiples meridianos radiales por cada ojo. Procesar cada uno de estos mapas de forma tradicional requiere mucho tiempo, es propenso a errores y se vuelve inviable a medida que la cantidad de pacientes y datos de tu estudio sigue creciendo."]
  
    C2["<b>Complejidad del cálculo matemático para obtener la rigidez de la córnea:</b><br/>Calcular el módulo de rigidez a partir de las velocidades medidas exige resolver de forma repetida ecuaciones físicas complejas, como el modelo Rayleigh-Lamb, para ajustar las curvas de velocidad registradas. Este procesamiento analítico tradicional es muy lento, requiere un gran esfuerzo de cómputo y detiene el flujo de trabajo rápido que necesita una consulta médica."]
  
    C3["<b>Sutileza y solapamiento biomecánico entre el estado normal y el subclínico:</b><br/>Las variaciones físicas en la velocidad de propagación de las ondas y la rigidez de una córnea sana frente a una en etapa subclínica son mínimas y suelen solaparse estadísticamente. Esta estrecha diferencia hace que los estadios tempranos de la enfermedad sean muy difíciles de interpretar y clasificar visualmente o mediante umbrales matemáticos tradicionales directos."]

    %% Nodo del Problema Central
    PR((("<b>PROBLEMA RAÍZ:</b><br/>El cálculo matemático de la rigidez corneal a partir de las velocidades de onda medidas es lento y complejo, lo que posterga el diagnóstico del estado corneal del paciente, impidiendo identificar a tiempo si es una córnea normal, subclínica o con queratocono clínico.")))

    %% Definición de nodos de Ramas (Efectos)
    E1["<b> Inviabilidad del uso clínico de la tecnología </b><br/> A pesar de que la elastografía por coherencia óptica es una técnica sumamente precisa para medir la biomecánica, se mantiene limitada al ámbito de laboratorio. Los médicos no pueden adoptar un sistema que requiere demasiado tiempo de procesamiento para evaluar a un solo paciente."]
  
    E2["<b>Pérdida de la ventana de tratamiento y complicaciones visuales graves:</b><br/>Al no disponer de una clasificación inmediata, los pacientes en estadios iniciales (subclínicos) no reciben terapias oportunas como el crosslinking para frenar el avance de la enfermedad. Además, corren el riesgo de ser sometidos por error a cirugías refractivas con láser, lo que debilita aún más la córnea de forma irreversible."]
  
    E3["<b>Alta tasa de falsos negativos y subdiagnóstico de la enfermedad en fases tempranas.:</b><br/>Provoca que un alto porcentaje de pacientes con queratocono subclínico sean catalogados erróneamente como sanos, permitiendo que la deformación progrese de manera silenciosa hacia un daño visual irreversible
."]

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
