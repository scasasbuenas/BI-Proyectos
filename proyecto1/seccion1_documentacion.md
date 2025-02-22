# BI - Proyecto 1

## Sección 1 - Documentación

**Desarrollado por:**
Santiago Casasbuenas
Manuel Gomez
Juan Pablo Castro

### Descripción

La sección 1 de este proyecto tiene como fin completar el Canvas de aprendizaje automático. En este caso, se responderán las preguntas del canva por bloque.

#### FUENTES DE DATOS

##### ¿Qué fuentes se utilizan? (Mencione tablas de bases de datos internas y externas o métodos API)

Los datos utilizados en este análisis provienen de fuentes periodísticas en línea con licencia **ATTRIBUTION 4.0 INTERNATIONAL**, lo que permite su uso y análisis con atribución adecuada. Las principales fuentes identificadas son los periódicos digitales "**Público**", "**La Marea**" y "**El Común**", entre otros.

##### ¿De dónde se toman los datos?

El conjunto de datos ha sido recopilado con el objetivo de analizar noticias falsas en el contexto político. Se asume que la información ha sido obtenida a través de extracción web (web scraping) o mediante bases de datos previamente estructuradas por investigadores.

##### ¿Se pueden utilizar para realizar el objetivo del análisis?

Estos datos son adecuados para el análisis, ya que contienen el texto completo de las noticias, lo que permite aplicar técnicas de procesamiento de lenguaje natural (NLP) para identificar patrones lingüísticos en noticias falsas. Sin embargo, es necesario evaluar la calidad de los datos y su posible sesgo antes de usarlos en modelos de aprendizaje automático.

#### PROPUESTA DE VALOR

##### ¿Quién es el beneficiario final?

El beneficiario final de este modelo de detección de noticias falsas puede variar según el contexto de aplicación, pero en términos generales, los principales beneficiarios son:

1. **Medios de comunicación y periodistas:** Ayuda a verificar la veracidad de las noticias antes de su publicación, fortaleciendo la credibilidad de los medios.
2. **Organizaciones gubernamentales y reguladoras:** Permite detectar campañas de desinformación que puedan afectar la estabilidad política y social.
3. **Plataformas digitales y redes sociales:** Puede integrarse en sistemas de moderación de contenido para reducir la propagación de noticias falsas.
4. **Ciudadanos y consumidores de noticias:** Facilita el acceso a información verificada, reduciendo el impacto de la desinformación.

##### ¿De qué empresa es?

El proyecto no está asociado a una empresa comercial específica, sino que proviene de un **grupo de académicos e investigadores** que buscan desarrollar un modelo de detección de noticias falsas con fines analíticos y científicos.

Sin embargo, si el modelo fuera implementado en un entorno real, podría ser utilizado por **empresas de medios de comunicación, redes sociales, agencias gubernamentales, organizaciones de fact-checking** o incluso **empresas tecnológicas** interesadas en combatir la desinformación.

##### ¿Qué problemas específicos se abordan?

Se abordan varios problemas relacionados con la **desinformación y la propagación de noticias falsas**, incluyendo:

1. **Manipulación de la opinión pública:** Las noticias falsas pueden influir en elecciones, movimientos sociales y políticas gubernamentales.
2. **Polarización social:** La difusión de información falsa contribuye a la división ideológica y a la radicalización de posturas políticas.
3. **Pérdida de confianza en los medios e instituciones:** La proliferación de desinformación socava la credibilidad de medios de comunicación, gobiernos y organismos internacionales.
4. **Dificultad en la verificación de información:** La sobrecarga de información en internet y redes sociales dificulta la identificación de noticias verídicas.
5. **Uso de noticias falsas como estrategia geopolítica:** Estados o grupos organizados pueden utilizar la desinformación como herramienta de desestabilización.

##### ¿Qué riesgo puede tener para ese beneficiario el uso de este modelo?

El uso del modelo de detección de noticias falsas puede implicar varios riesgos para los beneficiarios:

1. **Falsos positivos y negativos:**

   - Si el modelo clasifica erróneamente una noticia verídica como falsa (*falso positivo*), podría dañar la reputación de un medio o periodista.
   - Si el modelo no detecta una noticia falsa (*falso negativo*), la desinformación seguiría propagándose.
2. **Sesgo en los datos y en el modelo:**

   - Si el conjunto de datos de entrenamiento contiene sesgos ideológicos o lingüísticos, el modelo podría favorecer ciertos puntos de vista.
   - Puede haber un sesgo en la selección de las fuentes consideradas "confiables", lo que afectaría la objetividad del análisis.
3. **Posible censura o limitación de la libertad de expresión:**

   - Si el modelo es implementado por redes sociales o gobiernos, su uso podría ser cuestionado si se percibe como una herramienta de censura.
   - Se debe garantizar que el modelo no elimine contenido legítimo por error.
4. **Manipulación del modelo:**

   - Actores malintencionados podrían encontrar formas de evadir el modelo, generando desinformación que no sea detectada.
   - Grupos con intereses particulares podrían influir en el entrenamiento del modelo para favorecer su narrativa.
5. **Impacto en la confianza pública:**

   - Un modelo con errores o mal implementado podría generar desconfianza en la lucha contra la desinformación.
   - Las personas podrían depender demasiado del modelo sin desarrollar pensamiento crítico sobre las noticias que consumen.

Es importante mitigar estos riesgos mediante una continua revisión del modelo, auditorías de equidad y transparencia en su implementación.

#### DECISIONES

##### ¿Cómo se convierten los resultados del modelo en recomendaciones o decisiones procesables para el usuario final?

Los resultados del modelo se convierten en recomendaciones o decisiones procesables a través de diferentes enfoques según el beneficiario final. Algunas formas de hacerlo incluyen:

1. **Para medios de comunicación y periodistas:**

   - Alertas automáticas cuando una noticia tiene alta probabilidad de ser falsa.
   - Recomendaciones para realizar una verificación manual antes de su publicación.
   - Generación de un informe con palabras clave o patrones asociados a noticias falsas.
2. **Para plataformas digitales y redes sociales:**

   - Marcado automático de publicaciones sospechosas para revisión humana.
   - Reducción del alcance de contenido identificado como desinformación.
   - Etiquetas informativas para advertir a los usuarios sobre la veracidad de una noticia.
3. **Para gobiernos y organismos reguladores:**

   - Identificación de campañas de desinformación y actores responsables.
   - Generación de informes para evaluar el impacto de la desinformación en la opinión pública.
   - Recomendaciones para lanzar campañas de educación mediática.
4. **Para ciudadanos y consumidores de noticias:**

   - Creación de herramientas de fact-checking accesibles al público.
   - Extensiones o aplicaciones que analicen la confiabilidad de fuentes y noticias.
   - Sugerencias de fuentes confiables para contrastar la información.

#### TAREA DE APRENDIZAJE

##### ¿Cuál es el tipo de aprendizaje?

El tipo de aprendizaje utilizado en este proyecto es **aprendizaje supervisado**, ya que el modelo se entrena con un **conjunto de datos etiquetado**, donde cada noticia está clasificada como **falsa o verdadera**. El objetivo del modelo es aprender patrones en el texto que permitan predecir si una noticia nueva es falsa o no, basándose en ejemplos previos con etiquetas conocidas.

##### Si es aprendizaje supervisado, indicar qué se predice.

El modelo predice si una noticia es falsa o verdadera en función de sus características textuales y lingüísticas.

La variable objetivo (label) es una etiqueta binaria que indica:

    1 → Noticia falsa
    0 → Noticia verdadera

El modelo analiza el contenido de las noticias y, con base en patrones aprendidos durante el entrenamiento, asigna una de estas dos categorías a una nueva noticia.

##### ¿Cuáles son los posibles resultados de la tarea de aprendizaje?

Verdadero positivo (VP): El modelo identifica correctamente una noticia falsa.
Falso positivo (FP): El modelo clasifica incorrectamente una noticia verdadera como falsa.
Verdadero negativo (VN): El modelo identifica correctamente una noticia verdadera.
Falso negativo (FN): El modelo clasifica incorrectamente una noticia falsa como verdadera.

##### ¿Cuándo se observan los resultados de esta tarea?

Los resultados del modelo pueden observarse en **distintos momentos**, dependiendo de su implementación y del uso específico:

**1. En tiempo real:**

- Si el modelo está integrado en una plataforma de noticias o redes sociales, puede analizar y clasificar noticias al instante cuando se publican.
- Esto permite marcar contenido sospechoso inmediatamente y advertir a los usuarios.

**2. Por lotes (procesamiento periódico):**

- Si el modelo se usa para monitorear tendencias de desinformación en grandes volúmenes de datos, los resultados pueden generarse diaria, semanal o mensualmente.
- Este enfoque es útil para informes gubernamentales, análisis de campañas de desinformación y toma de decisiones estratégicas.

**3. Previo a la publicación de una noticia:**

- En el caso de medios de comunicación y fact-checkers, el modelo puede aplicarse antes de publicar una noticia, para verificar su veracidad y evitar la difusión de información falsa.

**4. Análisis retrospectivo:**

- El modelo también puede ser utilizado para analizar noticias pasadas y estudiar la evolución de la desinformación en distintos períodos de tiempo.

En nuestro caso específico, estamos hablando más que todo de un anaálisis retrospectivo. Esto debido a que se analizan las noticias, que son pasadas, y se da un recuento de la efectividad del modelo para predecir la veracidad de la información.

#### SIMULACIÓN DE IMPACTO

##### ¿Cuales son los valores de costo/beneficio de las decisiones (in)correctas?

**Decisiones Correctas**

1. **Verdadero Positivo (VP): Detectar correctamente una noticia falsa**
   * **Beneficio:**
     * Se evita la propagación de desinformación.
     * Se protege la confianza pública en los medios de comunicación.
     * Se reduce la polarización social y el impacto de campañas de manipulación.
     * Se ayuda a plataformas digitales y verificadores de datos a actuar con rapidez.
   * **Costo:**
     * Revisión y mantenimiento del modelo para asegurar su precisión.
     * Posible resistencia de actores interesados en la desinformación.
2. **Verdadero Negativo (VN): Identificar correctamente una noticia real**
   * **Beneficio:**
     * Se garantiza que no se censuren noticias legítimas.
     * Se fortalece la credibilidad del sistema de detección.
   * **Costo:**
     * Recurso computacional utilizado en el análisis de cada noticia.

**Decisiones Incorrectas**

1. **Falso Positivo (FP): Etiquetar erróneamente una noticia real como falsa**
   * **Costo:**
     * Posible censura de contenido legítimo.
     * Afectación de la credibilidad del medio de comunicación afectado.
     * Riesgo de que el sistema sea visto como sesgado o parcial.
     * Potencial demanda legal por parte de los medios o periodistas afectados.
   * **Beneficio:**
     * Reduce el riesgo de que una noticia dudosa sea aceptada como real, aunque con el costo de posibles errores.#
2. **Falso Negativo (FN): No detectar una noticia falsa**
   * **Costo:**
     * La desinformación sigue circulando y puede influir en la opinión pública.
     * Potencial impacto en elecciones, políticas públicas y estabilidad social.
     * Pérdida de confianza en los sistemas de detección si se filtran muchas noticias falsas.
   * **Beneficio:**
     * Se evita la censura excesiva, pero a costa de permitir la difusión de información dañina.#

##### ¿Cuáles son los criterios de éxito del modelo para su posterior despliegue?

**1. Precisión y Rendimiento del Modelo**

* **Métricas clave:**
  * **Exactitud (Accuracy):** Proporción de predicciones correctas sobre el total de casos.
  * **Precisión (Precision):** Porcentaje de noticias clasificadas como falsas que realmente lo son (minimiza falsos positivos).
  * **Recall (Sensibilidad):** Capacidad del modelo para detectar noticias falsas (minimiza falsos negativos).
  * **F1-Score:** Equilibrio entre precisión y recall.
  * **AUC-ROC:** Medida de la capacidad discriminativa del modelo.
* **Umbrales:** Se deben definir valores mínimos aceptables para cada métrica antes de desplegar el modelo.

**2. Generalización y Robustez**

* **Capacidad de generalización:** El modelo debe ser capaz de detectar noticias falsas en nuevos conjuntos de datos sin pérdida significativa de precisión.
* **Evaluación en datos no vistos:** Se debe probar en noticias recientes que no hayan sido parte del entrenamiento.
* **Resistencia a adversarios:** El modelo debe ser robusto ante tácticas de manipulación del lenguaje usadas en desinformación.

**3. Interpretabilidad y Explicabilidad**

* **Explicabilidad del modelo:**
  * Uso de técnicas como SHAP#o LIME# para entender qué palabras o patrones llevan a clasificar una noticia como falsa.
  * Generación de informes interpretables para verificadores de datos.
* **Confianza en las predicciones:**
  * Evitar modelos de "caja negra" que no permitan justificar decisiones.

**4. Eficiencia y Escalabilidad**

* **Tiempo de inferencia:**
  * El modelo debe ser rápido para analizar noticias en tiempo real o en lotes sin afectar el rendimiento del sistema.
* **Requerimientos computacionales:**
  * Evaluación de costos de procesamiento para implementaciones en servidores o en la nube.
* **Escalabilidad:**
  * Capacidad de procesar grandes volúmenes de datos sin pérdida de rendimiento.

**5. Cumplimiento Normativo y Ético**

* **Sesgo y equidad:**
  * El modelo debe minimizar sesgos ideológicos o de fuentes.
  * Se debe validar que no favorezca o perjudique sistemáticamente ciertas fuentes de información.
* **Regulación y privacidad:**
  * Cumplimiento con normativas de privacidad de datos (por ejemplo, GDPR en Europa).
  * Garantizar que el modelo no almacene información sensible sin consentimiento.

**6. Aceptación y Uso en el Entorno Real**

* **Facilidad de integración:**
  * Compatibilidad con APIs o sistemas de verificación de noticias existentes.
* **Adopción por usuarios:**
  * Interfaz accesible para verificadores de datos y periodistas.
* **Tasa de error aceptable:**
  * Se deben establecer umbrales de error que permitan decisiones informadas sin causar desconfianza en el sistema.

##### ¿Existen restricciones de equidad?

**Restricciones:**

* **Sesgo en datos de entrenamiento:** Puede favorecer ciertos medios o ideologías.
  * **Solución:** Diversificar fuentes y aplicar balanceo de datos.
* **Equidad en la clasificación:** Mayor tasa de error en ciertos grupos.
  * **Solución:** Usar fairness metrics y ajustar umbrales.
* **Falta de transparencia:** Puede generar desconfianza.
  * **Solución:** Explicabilidad con SHAP, LIME y puntuaciones de confianza.
* **Riesgo de censura:** Conflictos legales y éticos.
  * **Solución:** Validación humana en casos críticos y cumplimiento normativo.
* **Accesibilidad desigual:** Solo grandes plataformas podrían usarlo.
  * **Solución:** Versiones accesibles para periodistas y verificadores.

#### APRENDIZAJE (USO DEL MODELO)

##### ¿El uso del modelo es por lotes o en tiempo real?

**1. Uso en Tiempo Real** (Recomendado para plataformas digitales y verificadores de noticias)

* **Escenario:** Verificación instantánea de noticias en redes sociales, medios digitales o plataformas de fact-checking.
* **Ventajas: #es necesario mostrar ventajas y desventajas**
  * Detecta noticias falsas en el momento en que se publican.
  * Permite alertar a usuarios y verificadores en tiempo real.
* **Desafíos:**
  * Requiere infraestructura potente para procesar datos rápidamente.
  * Puede generar falsos positivos si el modelo no tiene suficiente contexto.

**2. Uso por Lotes** (Útil para análisis a gran escala)

* **Escenario:** Evaluación periódica de grandes volúmenes de noticias, por ejemplo, análisis diario o semanal de medios.
* **Ventajas: #es necesario mostrar ventajas y desventajas**
  * Permite revisar noticias con más contexto y precisión.
  * Menos demanda de recursos computacionales en comparación con tiempo real.
* **Desafíos:**
  * No previene la difusión inmediata de desinformación.
  * Puede perder relevancia si las noticias se viralizan antes de ser analizadas.

##### ¿Con qué frecuencia se usa?

**1. Uso en Tiempo Real**

* **Frecuencia:** Continua, en el momento en que se publican noticias o contenido en redes sociales.
* **Aplicaciones:** Plataformas de verificación de datos, medios digitales y redes sociales que necesitan análisis inmediato.
* **Ventaja:** Detecta desinformación al instante y permite alertar rápidamente.

**2. Uso por Lotes**

* **Frecuencia:** Diaria, semanal o en intervalos definidos según la necesidad del análisis.
* **Aplicaciones:** Reportes de noticias falsas, estudios de tendencias de desinformación, análisis de medios.
* **Ventaja:** Permite un análisis más detallado con mayor contexto y menos falsos positivos.

#### CONSTRUCCIÓN DE MODELOS

##### ¿Cuántos modelos se necesitan?

**1. Un único modelo de clasificación** 

* **Descripción:** Se entrena un solo modelo supervisado para clasificar noticias como falsas o verdaderas.
* **Ventaja:** Fácil de entrenar, mantener y desplegar.
* **Limitación:** Puede no capturar todos los matices de la desinformación.

**2. Modelo principal + modelo de refinamiento**

* **Descripción:**
  * **Modelo 1:** Un clasificador principal (ejemplo: Random Forest o BERT) que predice si una noticia es falsa o verdadera.
  * **Modelo 2:** Un refinador basado en técnicas de  **detección de lenguaje engañoso o verificación de hechos**.
* **Ventaja:** Mejora la precisión al combinar diferentes enfoques.
* **Limitación:** Mayor carga computacional y mantenimiento.

**3. Modelo adaptable con aprendizaje continuo**

* **Descripción:**
  * Se entrena un modelo supervisado inicialmente.
  * Se reentrena periódicamente con **nuevos datos etiquetados** para adaptarse a cambios en la desinformación.
* **Ventaja:** Mantiene la efectividad del modelo a lo largo del tiempo.
* **Limitación:** Requiere actualización constante y recursos adicionales.

##### ¿Cuándo deben actualizarse?

**1. Actualización basada en rendimiento** 

* **Frecuencia:** Cuando se detecta un descenso en métricas clave como **precisión (precision), recall o F1-score** en datos recientes.
* **Razón:** La desinformación evoluciona, y un modelo entrenado con datos antiguos puede volverse obsoleto.
* **Método:** Se recolectan nuevas noticias etiquetadas y se reentrena el modelo con datos más actualizados.

**2. Actualización periódica programada** 

* **Frecuencia:** Cada  **3 a 6 meses** , dependiendo de la velocidad con la que cambian las noticias falsas.
* **Razón:** Asegurar que el modelo sigue aprendiendo de nuevas tendencias y no pierde efectividad con el tiempo.
* **Método:** Se recopilan nuevas noticias, se validan las etiquetas y se realiza un reentrenamiento.

**3. Actualización por eventos críticos** 

* **Frecuencia:** Cuando ocurre un evento que cambia drásticamente el tipo de desinformación (ejemplo: elecciones, crisis sanitarias, conflictos internacionales).
* **Razón:** Los patrones de desinformación pueden cambiar rápidamente en eventos específicos.
* **Método:** Se recopilan datos recientes del evento y se ajusta el modelo en función de estos nuevos patrones.

##### ¿De cuánto tiempo se dispone para generar el modelo (incluido el proceso de ingeniería de características y el análisis o evaluación del mismo)? #No me convence esto ¿ponemos 1 semana?

**1. Entendimiento y Preparación de Datos***(2 a 4 semanas)*

* **Perfilado de datos:** Identificación de calidad, sesgos y distribución de clases.
* **Limpieza y preprocesamiento:** Eliminación de ruido, tokenización, lematización y eliminación de palabras irrelevantes.
* **Ingeniería de características:** Creación de representaciones del texto.

**2. Construcción y Entrenamiento del Modelo** *(3 a 6 semanas)*

* **Selección de algoritmos:** Prueba de modelos.
* **Entrenamiento y ajuste de hiperparámetros:** Optimización del modelo.
* **Evaluación inicial:** Medición de métricas como  **accuracy, precision, recall, F1-score y AUC-ROC** .

**3. Validación y Evaluación del Modelo** *(2 a 4 semanas)*

* **Prueba en datos no vistos:** Evaluación del modelo con datos recientes para medir su capacidad de generalización.
* **Ajuste de umbrales:** Optimización para minimizar falsos positivos y negativos.
* **Explicabilidad del modelo:** Uso de SHAP, LIME o análisis de palabras clave para asegurar transparencia.

**4. Implementación y Monitoreo Inicial** *(2 a 4 semanas)*

* **Despliegue en un entorno de prueba:** Validación del modelo en una aplicación real o API.
* **Monitoreo de desempeño:** Seguimiento de métricas en uso real para detectar necesidad de ajustes.
* **Recolección de retroalimentación:** Evaluación por verificadores de datos para detectar errores o sesgos.

**Tiempo Total Estimado: 9 a 18 semanas** *(Aproximadamente 2 a 4 meses)*

#### Ingeniería de Características

##### ¿Qué variables/características se utilizan en el modelo?

* **Palabras Clave:** Inicialmente, los datos entran al programa separados en tres partes: título (el cual es el título de la noticia),  descripción (el cual es una descripción breve de la noticia), la fecha de publicación y label (el cual indica si la noticia es falsa o no). Sin embargo, luego de transformar el título y la descripción, estos dos elementos se juntan a una sola variable la cual tiene las palabras clave de la noticia, de forma que esta es la única variable que se entrega al modelo para entrenarlo.
* **label:** Es lo que predice el modelo: Indica si una noticia dada es falsa o verdadera y es de naturaleza binaria.

##### Qué agregaciones o transformaciones se aplican a las fuentes de datos originales – incluir las más importantes -?
**1. Limpieza de Datos**

* **Eliminar impurezas:** Se eliminan caracteres especiales y se convierten los textos a minúsculas.
* **Eliminar stopwords:** Se eliminan palabras irrelevantes (stopwords).
* **Eliminar duplicados:** Se eliminan noticias duplicadas.
* **Eliminar columnas:** Se eliminan las columnas innecesarias como la fecha y se junta el texto del titulo y descripción en una sola columna.

**2. Tokenización y Normalización**

* **Extraer palabras clave:** Se extraen las palabras clave del Título y la Descripción.
* **Aplicar lemmatization:** Se lleva las palabras a su palabra raíz.
* **Aplicar stemming:** Elimina sufijos y prefijos de las palabras, entre otros.

**3. Vectorización de texto**

* **TF IDF (Term Frequency-Inverse Document Frequency):** Se usa TF-IDF  para convertir los textos en representaciones numéricas utilizables por modelos de aprendizaje automático


