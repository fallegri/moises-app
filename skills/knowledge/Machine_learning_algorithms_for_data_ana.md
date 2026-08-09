<!-- Página 1 -->

brought to you by COREView metadata, citation and similar papers at core.ac.uk REVISTA TECNOLÓGICA N° 11. ENERO - DICIEMBRE 2018provided by Repositorio Digital de la Ciencia y Cultura de El Salvador REDICCES

## ALGORITMOS DE APRENDIZAJE AUTOMÁTICO PARA ANÁLISIS Y

## PREDICCIÓN DE DATOS

## MACHINE LEARNING ALGORITHMS FOR DATA ANALYSIS AND PREDICTION

Lilian Judith Sandoval. Licenciada en Administración de Empresas, con diplomado en Tecnologías de Software.

Docente de la Escuela de Ingeniería en Computación ITCA-FEPADE Sede Central, Santa Tecla. jose.peraza@itca.edu.sv

Recibido: 16/04/2018 - Aceptado: 19/07/2018

## Resumen Abstract

ctualmente podemos ver que hemos entrado en unat present we can see that we have entered into a

# nueva era de información en la que las compañíasnew age of information in which companies knowA A conocen de antemano nuestras preferencias y,in advance our preferences and, according to our de acuerdo con nuestro comportamiento en labehavior in the network, they can predict what red, pueden predecir qué productos preferiremosproducts we will like before them to released those antes de su lanzamiento. Usan nuestra informaciónproducts. They use our information to generate para generar nuevas campañas de marketing connew marketing campaigns with improve certainty mayor seguridad de que los productos tendrán unathat the products will have greater acceptance and mayor aceptación y al mismo tiempo reducirán losat the same time reduce any possible risk. All this riesgos. Todo este conocimiento es proporcionadoknowledge is provided by Data Science, through the gracias a la Ciencia de Datos mediante la técnicaMachine Learning approach. They work with huge del Machine Learning. Trabajan con cantidadesamounts of information, with enough time, all this gigantescas de información, las que, con seguridad,data will certainly establish a behavior, providing establecerán un comportamiento en los datos conpatterns with great probability to keep occurring in el tiempo proporcionando patrones que con muchathe future. That’s how data prediction is generated. probabilidad se seguirán dando en el futuro. Es así como se genera la predicción de los datos.

## Palabras clave Keyword

Inteligencia artificial, inteligencia de negocios, Big Data,Artificial intelligence, business intelligence, Big Data, bases de datos.databases.

## Introducción

Con la cantidad de información que es generaday de forma segura cuál será el comportamiento de un día con día en Internet, ya sea por redes sociales,grupo de personas o equipos electrónicos en un futuro. transacciones comerciales, datos emitidos por distintos dispositivos, etc. existen procesos que aprovechan todaConoceremos sobre la técnica del Machine Learning, esa información y en lugar de conservarla como dataelemento fundamental de la Ciencia de Datos, los almacenada que solo está ocupando mucho espacio enmétodos que utiliza para realizar las predicciones de los servidores, se sigue utilizando para hacer análisisdatos y su presentación. de comportamientos y de algún modo identificar tendencias futuras. Muchas veces se reúne tanta información, que es posible conocer con anticipación

Derechos Reservados • Escuela Especializada en Ingeniería ITCA-FEPADE36

---

<!-- Página 2 -->

REVISTA TECNOLÓGICA N° 11. ENERO - DICIEMBRE 2018

Algoritmo de clasificación: esperamos que el algoritmo

## Inteligencia Artificial nos diga a qué grupo pertenece el elemento en estudio. El algoritmo encuentra patrones en los Los dispositivos que cuentan con inteligencia artificial datos que le damos y los clasifica en grupos. Luego pueden ejecutar distintos procesos análogos al compara los nuevos datos y los ubica en uno de los comportamiento humano, como la devolución de una grupos y es así como puede predecir de que se trata. respuesta por cada entrada (similar a los reflejos de los seres vivos), la búsqueda de un estado entre todos los La variable por predecir es un conjunto de estados posibles según una acción o la resolución de problema discretos o categóricos. Pueden ser: mediante una lógica formal. Binaria: {Sí, No}, {Azul, Rojo}, {Fuga, No Fuga}, etc. Cuando se otorga a estos dispositivos la habilidad de Múltiple: Comprará {Producto1, Producto 2…}, etc. aprender y de discernir, se les convierte en entidades Ordenada: Riesgo {Bajo, Medio, Alto}, etc. que rozan las capacidades de un superhombre, dado que alcanzan velocidades de procesamiento imposibles para los humanos y no necesitan descansar para funcionar, entre otras ventajas que los ubican por sobre los seres vivos en este contexto [1].

## Machine Learning

Es una rama de la Inteligencia Artificial que se encarga de generar algoritmos que tienen la capacidad de aprender y no tener que programarlos de manera explícita. El desarrollador no tendrá que sentarse a programar por horas tomando en cuenta todos los escenarios posibles ni todas las excepciones posibles. Lo único que hay que hacer es alimentar el algoritmo con un volumen gigantesco de datos para que el algoritmo aprenda y sepa qué hacer en cada uno de estos casos. Fig. 2. Gráfico de un algoritmo de clasificación

Algoritmo de regresión: en este método lo que se espera es un número. No lo ubica en un grupo, sino que devuelve un valor específico.

Fig. 1. Fuentes de datos del Machine Learning

Hay dos tipos de aprendizajes: el supervisado y el no supervisado.

Aprendizaje supervisadoA) Fig. 3. Gráfico de un algoritmo de regresiónEs cuando entrenamos un algoritmo de Machine Learning dándole las preguntas (características) y las respuestas (etiquetas). Así en un futuro elPor ejemplo, el precio de una casa. El algoritmo tiene algoritmo pueda hacer una predicción conociendoel precio de diferentes casas, pequeñas, grandes, en el las características.campo, en la ciudad, etc. y por medio de un gráfico de En este tipo de aprendizaje hay dos algoritmosdispersión, puede predecir el precio correcto de una (entrenamientos): el de clasificación y el de regresión.casa en consulta.

Derechos Reservados • Escuela Especializada en Ingeniería ITCA-FEPADE 37

---

<!-- Página 3 -->

REVISTA TECNOLÓGICA N° 11. ENERO - DICIEMBRE 2018

Fig. 4. Ejemplo de gráfico de dispersión en un algoritmo de regresión

Aprendizaje no supervisadoB) Aquí solo le damos las características al algoritmo, nunca las etiquetas. Queremos que nos agrupe los datos que le dimos según sus características. El algoritmo solo sabe que como los datos comparten ciertas características, de esa forma asume que pueda que pertenezcan al mismo grupo.

## Modelos de Machine Learning

Fig. 5. Gráfico de un Modelo de Árbol Los algoritmos de Machine Learning, se pueden agrupar en tres modelos: Redes neuronales3) Las redes artificiales de neuronas tratan, en cierto Modelos lineales1) modo, de replicar el comportamiento del cerebro, Estos tratan de encontrar una línea que se “ajuste” donde tenemos millones de neuronas que se bien a la nube de puntos que se disponen. Aquí interconectan en red para enviarse mensajes unas destacan desde modelos muy conocidos y usados a otras. Esta réplica del funcionamiento del cerebro como la regresión lineal (también conocida como humano es uno de los “modelos de moda” por la regresión de mínimos cuadrados), la logística las habilidades cognitivas de razonamiento que (adaptación de la lineal a problemas de clasificación adquieren. El reconocimiento de imágenes o vídeos, -cuando son variables discretas o categóricas-). por ejemplo, es un mecanismo complejo y una red Estos dos modelos tienen el problema del “overfit”, neuronal es lo mejor para realizarlo. El problema, esto significa que se ajustan “demasiado” a los como ocurre con el cerebro humano, es que son datos disponibles, con el riesgo que esto tiene para lentas de entrenar y necesitan mucha capacidad de nuevos datos que pudieran llegar. Al ser modelos cómputo. Quizás sea uno de los modelos que más ha relativamente simples, no ofrecen resultados muy ganado con la “revolución de los datos” [2]. buenos para comportamientos más complicados.

Modelos de árbol2) Son modelos precisos, estables y más sencillos de interpretar básicamente porque construyen unas reglas de decisión que se pueden representar como un árbol. A diferencia de los modelos lineales, pueden representar relaciones no lineales para resolver problemas. En estos modelos, destacan los árboles de decisión y los random forest (una media de árboles de decisión). Al ser más precisos y elaborados, obviamente ganamos en capacidad predictiva, pero perdemos en rendimiento.

Fig. 6. Gráfico de Redes Neurales

Derechos Reservados • Escuela Especializada en Ingeniería ITCA-FEPADE38

---

<!-- Página 4 -->

REVISTA TECNOLÓGICA N° 11. ENERO - DICIEMBRE 2018

Siri, que convierte conversaciones habladas a texto

## Fases de desarrollo (STT – Speech To Text) [3]. Fase de entrenamientoA) En esta fase se tiene una cantidad enorme de datos, de la cual se separa una parte para entrenar al algoritmo y darle toda esta información para que encuentre los patrones necesarios y después pueda hacer predicciones.

Fase de pruebaB) El resto de los datos que quedan, se van a usar para hacer las pruebas. Así le podemos hacer preguntas al algoritmo y evaluar si las respuestas están bien o mal, y saber si está aprendiendo o no. Si vemos que no coinciden los datos, tendremos que agregar más datos o cambiar el método que estamos utilizando. Pero si se observa que hay entre un 80% a 90% de respuestas correctas, podemos decir que hay un buen grado de aprendizaje y poder utilizar ese algoritmo.

Fig. 8. Brazo robot que utiliza Machine Learning.

Procesos que hacen uso de Machine Learning.

Detectar fraudes en transacciones bancarias. Detectar intrusiones en una red de comunicaciones de datos. Predecir fallos en equipos tecnológicos. Fig. 7. Fases de Machine Learning. Prever qué proyectos serán más rentables el próximo año y con un menor riesgo. Seleccionar clientes potenciales basándose en

## Ámbitos de la aplicación comportamientos en las redes sociales, interacciones en la web, etc. Productos que utilizan algoritmos de Machine Learning Predecir el tráfico urbano y dar rutas alternativas. Vehículos no tripulados que se conducen solos. Conocer anticipadamente qué partido político ganará las próximas elecciones analizando losBrazo robótico que juega ajedrez. comentarios de los usuarios en las redes socialesReconocimiento facial de Facebook para identificar Saber cuál es el mejor momento para publicar tuits,contactos. actualizaciones de Facebook o enviar newsletters.Microsoft Cortana, asistente personal inteligente Prevenir la deserción de clientes en una empresa depara diferentes dispositivos. telefonía.Motores de búsqueda que ofrecen información de Predecir las ventas de los años siguientes analizandoacuerdo a las preferencias de los usuarios. comportamiento actual de los clientes.Machine Translation usado por el traductor de Conocer las preferencias de los clientes a través deGoogle, que reconoce palabras en más de 100 sus operaciones en la red.idiomas humanos. Hacer prediagnósticos médicos basados en síntomasGoogle Trends, son las tendencias de búsquedas en del paciente.Google Cambiar el comportamiento de una App móvil paraGoogle N Gram Viewer, indexa libros que tiene adaptarse a las costumbres y necesidades de cadaGoogle escaneados y sus términos gramaticales. usuario.

Derechos Reservados • Escuela Especializada en Ingeniería ITCA-FEPADE 39

---

<!-- Página 5 -->

REVISTA TECNOLÓGICA N° 11. ENERO - DICIEMBRE 2018

## Diferencias entre el Machine

## Learning y el Business Intelligence

Cualquier tipo de aplicación de Business Intelligence,utiliza herramientas de ETL para acceder a ellos y su primeramente, recoge los datos en bruto desde lapropósito principal es mejorar los objetivos de negocio base de datos transaccional, que es donde se registrande las compañías en un futuro. todas las operaciones del negocio día con día. Una vez almacenados, los ingenieros de datos utilizan lo que seEl mecanismo que lo hace diferente es la detección de denomina herramientas de ETL (Extraer, Transformarpatrones entre millones de datos (Big Data). Esta es y Cargar) para manipular, transformar y clasificar losuna diferencia importante respecto a la inteligencia de datos en una base de datos estructurada, conocidanegocios tradicional, a la que podríamos añadir estos como DataWarehouse. Luego, los analistas de negociotres aspectos: utilizan técnicas de visualización de datos para explorar los datos almacenados en los Data Warehouse. ConFrente al uso de datos agregados, el Machine1) este tipo de herramientas crean paneles visuales (oLearning utiliza datos individuales con características dashboards) para hacer accesible la información adefinitorias de cada una de las instancias. De esta perfiles de negocio no especialistas en datos. Losforma se pueden usar miles de variables para paneles ayudan a analizar y entender los resultados endetectar los patrones. el pasado y sirven para adaptar la estrategia futura que mejore los indicadores clave de negocio.En lugar de basarse en una analítica descriptiva,2) Machine Learning ofrece una analítica predictiva. El Machine Learning, en cambio, es una técnica queEs decir, no solo hace una valoración de lo que ha permite detectar patrones “a bajo nivel” en milespasado y extrapola tendencias generales, sino que de datos individuales. El desarrollo de aplicacioneshace predicciones individualizadas en el que los predictivas es una de las potencias destacables de estadetalles y matices definen los comportamientos del técnica, ya que facilita la automatización de procesos,futuro. la toma de decisiones y el continuo aprendizaje basado en datos. Además, se trata de sistemas que aprendenLos paneles de visualizaciones o dashboards se3) automáticamente con el tiempo, se integran en elsustituyen por aplicaciones predictivas. Estamos desarrollo de la compañía y se adaptan a los cambioshablando de uno de los mayores potenciales del de entorno cuando se les alimenta de forma constanteMachine Learning: los algoritmos predictivos con nuevos datos.aprenden automáticamente de los datos y sus modelos se pueden integrar en aplicaciones para En un principio podría parecer poca la diferencia, ya quedotarlas de capacidades predictivas. Los modelos el Machine Learning también usa los datos para trabajar,se reentrenan periódicamente para que aprendan automáticamente de nuevos datos. [4]

## Referencias

[1] «Definición de inteligencia artificial - Qué es,[3] A., Conchas, «8 aplicaciones de Machine Learning», Significado y Concepto». [En línea]. Disponible en:2017. [En línea]. Disponible en: https://www.inbest. https://definicion.de/inteligencia-artificial/. [Accedido:cloud/comunidad/8-aplicaciones-de-machine-learning. 16-mar-2018][Accedido: 16-mar-2018]

[2] Rayón, «Guía para comenzar con algoritmos de[4] «Diferencias entre Business Intelligence y Machine Machine Learning», Deusto Data (blog), 2017. [En línea].Learning», 2017. [En línea] Disponible en: https:// Disponible en: https://blogs.deusto.es/bigdata/guia-cleverdata.io/diferencias-bi-machine-learning/. para-comenzar-con-algoritmos-de-machine-learning/.[Accedido: 16-mar-2018] [Accedido: 16-mar-2018]

Derechos Reservados • Escuela Especializada en Ingeniería ITCA-FEPADE40