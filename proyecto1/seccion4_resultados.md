# Descripción general de resultados

## Regresión logística

Se utilizó un modelo de **Regresión Logística** con un umbral de **0.6** para clasificar noticias en **falsas (0) y verdaderas (1)**. Los resultados finales muestran un **rendimiento sólido con un balance adecuado entre precisión y recall** .

| **Métrica**                         | **Valor** |
| ------------------------------------------ | --------------- |
| Exactitud                                  | 89.1%           |
| Precisión (Clase 0 - Noticias Falsas)     | 89%             |
| Precisión (Clase 1 - Noticias Verdaderas) | 89%             |
| Recall (Clase 0 - Noticias Falsas)         | 84%             |
| Recall (Clase 1 - Noticias Verdaderas)     | 93%             |
| F1-Score (Clase 0 - Noticias Falsas)       | 87%             |
| F1-Score (Clase 1 - Noticias Verdaderas)   | 91%             |

### **Resumen**

* Alta exactitud (89.1%) lo que indica que el modelo clasifica correctamente la mayoría de las noticias.
* Balance entre precisión y recall en ambas clases (89% de precisión en ambas clases).
* Recall alto en la detección de noticias verdaderas (93%), lo que significa que la mayoría de las noticias legítimas son correctamente identificadas.
* Recall razonablemente alto en la detección de noticias falsas (84%), evitando que muchas noticias falsas pasen como verdaderas.

### **Análisis de la matriz de confusión**

#### **Valores clave de la matriz de confusión**

![1740156786465](image/seccion4_resultados/1740156786465.png)

#### Interpretación

- **4,026** noticias **falsas** fueron **correctamente identificadas** como **falsas** (Verdaderos Negativos - TN).
- **6,144** noticias **verdaderas** fueron **correctamente clasificadas** como **verdaderas** (Verdaderos Positivos - TP).
- **755** noticias falsas fueron **clasificadas erróneamente** como **verdaderas** (Falsos Negativos - FN).
- **488** noticias **verdaderas** fueron **clasificadas erróneamente** como falsas (Falsos Positivos - FP).

#### Conclusiones

Por un lado, la tasa de error es baja , ya que el modelo tiene más verdaderos positivos y negativos que errores. Por otro lado, hay más falsos negativos (noticias falsas clasificadas como verdaderas) que falsos positivos (noticias verdaderas clasificadas como falsas). Esto sugiere que el modelo prioriza la detección de noticias verdaderas, pero sigue siendo confiable para detectar noticias falsas.

### **¿Cómo aportan estas métricas a los objetivos del negocio?**

El objetivo del modelo es **detectar noticias falsas con alta precisión y recall,** asegurando que la herramienta pueda ser utilizada para mejorar la verificación de información y la toma de decisiones estratégicas.

#### Impacto Positivo en la Organización

Uno de los impactos más positivos del modelo de regresión logística es que demuestra una alta precisión y recall, lo que ayuda a reducir la propagación de desinformación. Adicionalmente, las métricas muestran que el modelo tiene confianza en sus predicciones, reduciendo el riesgo de errores. Por último, utilizando este modelo es posible priorizar revisiones manuales en noticias dudosas, mejorando la eficiencia del equipo de fact-checking.

#### Riesgos y Consideraciones

El principal riesgo que encontramos radica en que aún hay falsos negativos, lo que significa que algunas noticias falsas podrían ser clasificadas como verdaderas y propagarse. Para corregir esto, es necesrio bajar el umbral para aumentar el recall en la clase 0.

#### ¿Qué Significa Cambiar el Umbral?

El **umbral de clasificación** es el valor a partir del cual el modelo decide si una noticia es  **falsa (0) o verdadera (1).** Como el modelo de regresión logística utiliza **clasificación binaria**, este genera una **probabilidad** entre **0 y 1** de que una una noticia sea verdadera.

* Por defecto, el umbral es **0.5**, lo que significa:
  * **Si la probabilidad es ≥ 0.5** , la noticia se clasifica como **verdadera** .
  * **Si la probabilidad es < 0.5** , la noticia se clasifica como **falsa** .

En el caso puntual de este proyecto, el umbral utilizado es de 0.6. 

#### ¿Cómo afectó esto al modelo?

**Comparación antes y después del cambio de umbral:**

| **Métrica**                | **Antes (Umbral 0.5)** | **Después (Umbral 0.6)** |
| --------------------------------- | ---------------------------- | ------------------------------- |
| Precisión (Clase 0 - Falsas)     | 80%                          | 89% ⬆                         |
| Precisión (Clase 1 - Verdaderas) | 82%                          | 89% ⬆                          |
| Recall (Clase 0 - Falsas)         | 73%                          | 84% ⬆                          |
| Recall (Clase 1 - Verdaderas)     | 87%                          | 93% ⬆                          |
| F1-Score (Clase 0 - Falsas)       | 76%                          | 87% ⬆                          |
| F1-Score (Clase 1 - Verdaderas)   | 84%                          | 91% ⬆                          |
| Exactitud (Accuracy)              | 81%                          | 89% ⬆                          |
