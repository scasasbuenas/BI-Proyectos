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