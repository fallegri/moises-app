<!-- Página 1 -->

---

<!-- Página 2 -->

Edison Humberto Medina La Plata (Lima) Tiene un MBA por la Universidad Peruana de Ciencias Aplicadas (UPC), un máster en Gerencia y Administración por la Escuela de Organización Industrial (EOI, España), un posgrado en Gerencia de Sistemas y Tecnologías de la Información por la Universidad ESAN, y distintas especializaciones en estrategias de transformación digital, data science, big data y analítica de datos. Hace más de 20 años, es consultor en temas sobre el uso estratégico de datos. Asimismo, es director de EML Information, empresa que desarrolla proyectos de business intelligence y analytics en diferentes entidades públicas y privadas con presencia en varios países de la región. Ha sido director académico de nuevos programas en la Escuela de Posgrado de la UPC, y desde hace 17 años es docente y director de programas especializados en business intelligence, analytics, big data y transformación digital en la misma casa de estudios. Además, es conferencista en diversos países de América Latina y autor del libro Business Intelligence. Una guía práctica (Editorial UPC). ORCID: 0000-0001-5305-6516

---

<!-- Página 3 -->

---

<!-- Página 4 -->

© Universidad Peruana de Ciencias Aplicadas (UPC) Autor: Edison Humberto Medina La Plata Edición: Luisa Fernanda Arris

Corrección de estilo: Claudia Prieto Requejo Diseño de cubierta y diagramación: Dickson Cruz Yactayo

Editado por: Universidad Peruana de Ciencias Aplicadas S. A. C. Av. Alonso de Molina 1611, Lima 33 (Perú) Teléfono: 313-3333 www.upc.edu.pe Primera edición: mayo de 2023 Versión e-book: mayo de 2023

Universidad Peruana de Ciencias Aplicadas (UPC) Biblioteca Edison Humberto Medina La Plata Big data. Los datos como generadores de valor Lima: Universidad Peruana de Ciencias Aplicadas (UPC), 2023 ISBN de la versión epub: 978-612-318-468-1 DATOS MASIVOS, EMPRESAS, PLANIFICACIÓN ESTRATÉGICA, ADMINISTRACIÓN DE LA INFORMACIÓN, ESTUDIO DE CASOS, TOMA DE DECISIONES 005.74068 MEDI

DOI: http://dx.doi.org/10.19083/978-612-318-468-1 Hecho el Depósito Legal en la Biblioteca Nacional del Perú n.° 2023-04331 Esta publicación fue sometida a un proceso de revisión de pares antes de su divulgación. Todos los derechos reservados. Esta publicación no puede ser reproducida, ni en todo ni en parte, ni registrada en o transmitida por un sistema de recuperación de información, en ninguna forma ni por ningún medio, sea mecánico, fotoquímico, electrónico, magnético, electroóptico, por fotocopia o cualquier otro, sin el permiso previo, por escrito, de la editorial. El contenido de este libro es responsabilidad del autor y no refleja necesariamente la opinión de los editores.

---

<!-- Página 5 -->

A Luci y Fati, quienes lejos del mundo de los datos me enseñaron a ser padre.

---

<!-- Página 6 -->

# Introducción

En la actualidad, las empresas privadas e instituciones públicas se han volcado hacia la transformación digital; esto debido a la evolución de la tecnología digital y a los cambios en nuestro comportamiento como consumidores. Así, han advertido que deben adecuar sus modelos de negocio para responder a las necesidades de un cliente o ciudadano cada vez más digitalizado. A esto se suma el impacto de la pandemia de la COVID-19, la cual, pese a su afectación en la salud y en la economía, impulsó una mayor explosión del canal digital. Detrás de toda la digitalización en la que nos encontramos, aparecen unos elementos clave, los datos; sin ellos, no sería posible conocer tendencias, patrones, predicciones, no podríamos hablar ni siquiera de inteligencia artificial o machine learning. De hecho, se los puede catalogar como la base de esta era digital. Los datos han estado presentes desde hace tiempo en las estrategias de diversas organizaciones, que supieron generarse mucho valor a través de iniciativas de business intelligence, con toda su capacidad para centralizar la información y ponerla a disposición de la empresa, brindándonos un uso descriptivo sumamente potencial y respondiendo a preguntas como ¿qué pasó? ¿cuánto? ¿cuándo? ¿dónde?; asimismo, mediante iniciativas de business analytics y su gran propuesta de predicción, basada en aprender de la historia para realizar predicciones futuras más precisas, que responden a preguntas como ¿por qué ocurrió? ¿qué pasará? ¿qué sucederá luego? Y ahora big data, con la misma finalidad de apoyo para la toma de decisiones, pero con mucho volumen de datos y variabilidad de fuentes, contribuye al mundo actual inundándolo de

---

<!-- Página 7 -->

datos y plataformas digitales, redes sociales, audios, videos, etcétera. En suma, estas iniciativas aportan mucho valor, inclusive a la generación de ventajas competitivas en las organizaciones, a partir de un uso inteligente y constante de datos. En este viaje de mucha contribución de datos a nuestro mundo, nos hemos distraído pensando que la tecnología lo resolvía todo y que comprando una tecnología de análisis de datos ya era suficiente, ¡error! Se puede hablar de mucha tecnología en big data; sin embargo, la recopilación de datos de diversas fuentes no equivale a un valor agregado, lo que importa es qué se hace con esos datos. La tecnología está preparada para apoyar las iniciativas, pero necesitamos adaptar a nuestras organizaciones para triunfar en esta era de alta digitalización, donde los datos se convierten en un pilar fundamental. En el presente libro, se brindan las pautas necesarias para preparar a nuestras organizaciones para triunfar en esta era donde el uso inteligente de los datos se convierte en un aspecto clave y el big data en el mecanismo para lograrlo. No se trata, por lo tanto, de derivar estas iniciativas al equipo de tecnología, sino de establecer una organización basada en datos, donde cualquier persona de las distintas áreas esté convencida de la contribución de estos y pueda proponer alternativas de uso para la generación de valor. Se aborda el big data desde la óptica de la generación de los beneficios estratégicos y no de las infraestructuras tecnológicas que tenemos que montar. Para ello, se emplea un lenguaje que permita sensibilizar a todo directivo, funcionario, ejecutivo, ejecutiva, decisor en el uso de los datos para que pueda contribuir con su gestión y, en suma, con su organización. Para el efecto, en los primeros capítulos, se muestran los aspectos conceptuales del big data, los beneficios que genera y su gran poder al trabajar con variabilidad de fuentes de datos. En los capítulos 3 y 4, se destaca el impulso hacia un uso inteligente de datos y la importancia de trabajarlos como un activo estratégico. En el capítulo 5, se resalta la necesidad de establecer una estrategia de datos, profundizando en los aspectos clave que debemos impulsar en la organización. Finalmente, en los capítulos 6 y 7, se pone énfasis en el establecimiento de la cultura analítica y las

---

<!-- Página 8 -->

competencias base que debemos fortalecer a todo nivel para que instalemos un uso generalizado de los datos. Se acompaña cada uno de los temas con una serie de casos referentes al contexto global, pero también casos y situaciones que he vivido en mi labor de consultoría, junto con mi equipo, a fin de conseguir una mayor comprensión de los aspectos que incluye el big data y cómo prepararnos para convertirnos en una organización basada en datos.

---

<!-- Página 9 -->

# Capítulo 1.

# ¿Qué es y por qué big data?

Nos encontramos en un escenario mundial donde la transformación digital es una norma en las organizaciones tanto públicas como privadas, y donde los datos se han convertido en un elemento clave para estos procesos, los cuales están permitiendo la generación de mucho valor a quienes han sabido aprovecharlos. Las iniciativas basadas en datos se han adaptado a la evolución digital que venimos experimentando desde hace varios años y, en este contexto, el big data cobra relevancia, pues nos proporciona la posibilidad de cohesionar mucho volumen de datos provenientes de distintas fuentes de datos, como redes sociales, plataformas digitales, audios, videos, etcétera. En la actualidad, somos testigos del gran impacto que está generando el big data a nivel mundial, y es que muchas organizaciones de diversos sectores ya lo vienen aplicando con gran éxito, logrando obtener mucho beneficio y con esto diferenciarse de la competencia. Sin embargo, a pesar de las notables contribuciones del big data, aún no se aprovecha a cabalidad en muchas de nuestras organizaciones en América Latina, donde ya estamos viendo algunos avances, pero todavía falta mucho más. Lo anterior hay que tomarlo

---

<!-- Página 10 -->

desde la óptica de la oportunidad para aprender de la alta aplicabilidad que tiene el big data en las diversas industrias del mercado en el resto del mundo, de las que podemos conocer sus experiencias de implementación y los beneficios obtenidos, y adaptarlas a nuestras propias realidades. Por ello, apoyarse en big data se vuelve aún más necesario en este contexto altamente competitivo, donde, además, estamos viviendo la difícil situación provocada por la pandemia del SARS-CoV-2, no solo por lo sucedido, sino por los efectos que pueda conllevar a futuro. Por lo tanto, en la medida en que nuestras organizaciones reconozcan el gran valor que tienen los datos, seremos testigos de muchas más implementaciones.

## 1.1 Conceptualización del big data

Seguramente, la primera pregunta que le viene a la mente a todo ejecutivo o ejecutiva es ¿qué es el big data? Su nombre proviene de la función que cumple y que ha sido definida desde varias perspectivas debido a que se refiere al manejo de grandes volúmenes de datos. Esto deja un espacio para determinar cuál es la cantidad de datos a la que alude; sin embargo, no hay un acuerdo sobre a partir de qué cifra se le puede llamar big data. Una conceptualización abreviada y precisa de big data podría ser que consiste en grandes volúmenes de datos estructurados y no estructurados que permiten apoyar la toma de decisiones de las organizaciones, indistintamente de su tamaño, rubro comercial o industria en la que participan. Asimismo, cabe resaltar que no se trata de una herramienta de aplicación tecnológica, como muchos piensan, y, por lo tanto, no se debe abordar únicamente desde ese punto de vista, dado que su mayor virtud es que puede generarle beneficios a toda empresa que lo implemente. De ahí la importancia de que seamos conscientes de cómo este manejo de los datos, con la actual hegemonía del big data, puede tener un impacto positivo en las organizaciones. Por ello, el propósito de este libro es dar a conocer las bondades del big data y la

---

<!-- Página 11 -->

amplitud de su aplicabilidad en distintos campos y sectores, a fin de llevar esta práctica a sus propias empresas.

## 1.2 Aplicabilidad del big data

Actualmente, la aplicación de big data se sigue ampliando en organizaciones de distintos tipos y tamaños, siendo Estados Unidos y diversos países de Asia y Europa los grandes referentes en estas iniciativas. Cabe destacar que las organizaciones que trabajan hace varios años con big data son las plataformas digitales y redes sociales con las que hoy interactuamos, como Netflix, LinkedIn, Facebook, Google, Uber, entre muchas otras; son empresas catalogadas como analíticas, ya que todo lo que hacen lo basan en los datos. No obstante, es muy importante considerar que, como la finalidad de utilizar big data es para la generación de beneficios, debemos buscar cómo monetizar el uso de los datos. Esto ya lo resolvieron, por supuesto, las empresas que venimos citando y, más aún, siguen impulsando nuevas iniciativas de generación de valor a partir de sus datos. Algunos de estos beneficios son minimizar costos, mejorar el servicio al cliente, optimizar el marketing de la empresa, aumentar las ventas, desarrollar nuevos productos o servicios, etcétera. En las siguientes líneas, cito como introducción dos casos de big data, el primero es uno de los más emblemáticos de aplicación de big data como Netflix, una empresa que utiliza los datos como gran soporte de toda su estrategia y que viene apoyándose en ellos, incluso, desde antes de la era del streaming. El segundo caso ocurre en la Casa Editorial El Tiempo en Colombia, que de igual forma encontró en el uso de los datos una gran oportunidad para generarse mucho valor y diferenciarse de la competencia.

1.2.1 Caso Netflix Este caso resulta tan particular en el tema del manejo de datos que parecerá sorprendente cómo los emplean todos los días para alcanzar tanto éxito. De hecho, Netflix ya utilizaba analítica de datos desde

---

<!-- Página 12 -->

que entregaba películas en DVD, lo cual evidencia el nivel de confianza que ha depositado siempre en los datos, aunque ha evolucionado con la tecnología hasta convertirse hoy en el líder del streaming. Todo aquel que usa la plataforma de Netflix observa que, al comenzar a emplearla, esta presenta una serie de recomendaciones; por ejemplo, las diez películas y series más populares en el país donde se suscribe el usuario, la fecha en la que se inicia sesión, los contenidos que son tendencia a nivel mundial en la plataforma, y el contenido audiovisual actual para ver algo relacionado con los productos audiovisuales vistos o según las calificaciones otorgadas. Así, al reproducir una serie como Gambito de dama, y otras afines, la plataforma puede sugerirnos contenido similar que también está basado en libros o que pertenece al género cinematográfico del drama. De esa manera, la empresa siempre les está comunicando y sugiriendo a sus usuarios el consumo de cierto contenido, pero de un modo muy personalizado. Ahora bien, ¿cómo una empresa tan grande como Netflix Inc. logra ofrecerles a sus clientes un servicio tan personalizado? La respuesta radica en la forma en que la empresa maneja los datos. La mejor estrategia de marketing que usa Netflix es conocer muy bien a sus usuarios: la empresa sabe qué películas y series vemos; cuáles son las horas en las que visualizamos los contenidos; qué días de la semana vemos los productos; si hay películas o series que comenzamos a ver, pero no las terminamos, o si las retomamos sabe cuándo lo hacemos y a qué hora; incluso, advierte si nos “encerramos” el fin de semana a ver la temporada completa de una serie. Este conocimiento lo obtiene de nosotros mismos. Somos los usuarios quienes le permitimos a la empresa conocer nuestras preferencias al calificar una película como buena o mala con un like o dislike, inclusive, al abrir una película y verla sin brindar ninguna información. Toda esa información se guarda en una base de datos (base estructurada) y, cada vez que consumimos más contenidos, se siguen almacenando en esta. Más aún, Netflix compara nuestro comportamiento de visualización de películas y series con el de otras personas que

---

<!-- Página 13 -->

pertenecen a nuestra misma localidad, distrito, provincia y país para analizarlos e inferir comportamientos geodemográficos. Con el objetivo de ampliar esta información sobre sus usuarios, Netflix accede a los datos de nuestras redes sociales (base no estructurada). Al contar con todos estos datos personales y sobre nuestras preferencias, se halla en condiciones de conocernos bien y, por lo tanto, de personalizar sus acciones de marketing.

Otro aspecto o estrategia para la cual Netflix aplica big data es la creación de productos audiovisuales propios. Así, desde 2012, la empresa ha lanzado sus propias series y películas como House of Cards, que fue la primera serie en estrenarse, y a la fecha cuenta con un amplio catálogo de películas y series propias en su plataforma de streaming. Para tomar la decisión sobre cuáles serían los elementos que incluiría esta primera serie y quiénes participarían en ella, se podría pensar que la empresa realizó un casting para elegir a los actores que conformarían el elenco y definir a los productores. Sin embargo, esto no fue necesario porque, al aplicar big data para elaborar un nuevo producto audiovisual propio, la empresa solo requiere “preguntarles” a los datos. Por ejemplo, en este caso, los datos le “dijeron” a Netflix que, a nivel mundial, un alto porcentaje de clientes había visto la versión británica de la serie House of Cards, la cual contaba con una valoración positiva; y también que estos han visualizado otras

---

<!-- Página 14 -->

películas protagonizadas por Kevin Spacey (quien forma parte del elenco de House of Cards) y, además, otras películas producidas por David Fincher (productor de la serie). De esta manera, los datos prácticamente le configuraron a la empresa el nuevo producto. El resultado fue que, en el trimestre posterior al lanzamiento de la serie, la empresa percibió un aumento de 2 000 000 clientes en los Estados Unidos y de 1 000 000 clientes más en todo el mundo. De acuerdo con lo anterior, advertimos que su estrategia de marketing no sería tan efectiva si la empresa lanzara primero un producto audiovisual, soportada en especulaciones y supuestos sin la base cuantitativa y cualitativa que aporta el análisis de datos, y después de los estrenos de las películas y series recurriera a los datos para determinar cuántos usuarios consumieron el producto y cómo ha sido calificado. Este análisis posterior es totalmente contrario al proceso que deben seguir las empresas que desean establecer una cultura analítica implementando big data, ya que esta iniciativa antecede a la toma de decisiones para apoyar dicho proceso. Así, un análisis basado en datos posterior a la toma de decisiones solo se constituye en un paso de constatación o comprobación de la efectividad de las estrategias implementadas.

1.2.2 Caso Editorial El Tiempo En la actualidad, cada vez más sectores se suman al impulso de iniciativas de big data, como la Casa Editorial El Tiempo, una empresa del ámbito de las comunicaciones en Colombia que descubrió el poder de los datos para contribuir a su éxito en este. Desde 1911, año en el que fue fundado, El Tiempo ha desempeñado una importante labor periodística en el país y, a pesar de su larga trayectoria en el sector, no ha podido eludir la necesidad que tienen todas las organizaciones de reconfigurarse para adaptarse a la sociedad de la información y sus requerimientos. Para el sector de las comunicaciones, los cambios ocasionados por la globalización han sido mayores; ya que, con el surgimiento de la internet y de los avances en la tecnología, la prensa ha tenido que transitar del formato escrito al digital y adaptarse a las nuevas

---

<!-- Página 15 -->

dinámicas que conlleva este medio. Uno de los cambios más significativos claramente ha sido el declive de la prensa tradicional — que utilizaba primeramente el papel para difundir la información noticiosa— y la consecuente consolidación de los diarios digitales en la difusión de la información, puesto que una buena parte de la población muestra más predilección por la lectura en pantallas que en el formato impreso, en especial las generaciones que nacieron en los años de transformación tecnológica, desde 1980 hasta la época actual. Ahora bien, con toda la accesibilidad que permite hoy la tecnología y las innovaciones en las comunicaciones, aún hay una cantidad de población significativa en todo el mundo que prefiere consumir las noticias por el medio escrito, por lo cual la prensa tradicional sigue vigente en el mundo globalizado. Sin embargo, los periódicos necesitan estar a la vanguardia para alcanzar a esta población que prefiere el medio digital, y así llevarle la información oportunamente e, incluso, en tiempo real. Los estudios sobre el tema han confirmado que, en la siguiente década, la gran mayoría de consumidores estará conformada por los nativos digitales, esto es, aquellas personas que nacieron en la época digital, por lo que las empresas deben dirigir hacia ellos estrategias para captar su atención. Esto, claramente, es una realidad que no pasa inadvertida para una editorial como El Tiempo, que cuenta con una vasta experiencia y muchos años desarrollando su labor periodística. Por ello, el diario se ha reconfigurado para atender a ambos segmentos de mercado, tanto al público que lee en pantalla como al que prefiere la lectura en formato físico. ¿Cómo lo ha hecho? El Tiempo ha comenzado a trabajar algo que llama mucho la atención y es la personalización de lo que representa el uso del diario para cada lector. Por lo tanto, si una persona usualmente ingresa a su página web y sus preferencias son las secciones de Política y Deportes, siempre encuentra un contenido personalizado, inicial y, en especial, con extractos de información política y deportiva, mientras que los demás productos noticiosos también le aparecen, pero como complementarios. Esto es posible debido a que la empresa, aun cuando no les ha preguntado a los

---

<!-- Página 16 -->

usuarios por sus preferencias, las conoce de antemano porque previamente ha realizado un análisis sobre su comportamiento de visualización. Así, por ejemplo, a un usuario que prefiere consumir noticias de deporte y espectáculos se le presentará la misma página web del diario, pero con información noticiosa personalizada sobre deportes y espectáculos, mientras que los demás productos noticiosos le aparecerán como complementarios. En ese sentido, para el periódico, no solo resulta trascendental analizar los comportamientos de visualización, sino también los blogs asociados a la información que los usuarios están leyendo. En este ejemplo, buscaría conocer si el primer usuario ingresa a blogs de política o vinculados al canal en el que ve los deportes en los cuales otros usuarios no ingresan. Toda esta información, estudiada en conjunto, va configurando un escenario de personalización extrema. La personalización de los servicios cada vez tiene más auge y esto se debe precisamente a la respuesta que los clientes digitales le dan al mundo de hoy cuando se les pregunta qué quieren: “rapidez, facilidad de uso, agilidad, personalización, omnicanalidad” son las exigencias del mundo actual. Por lo tanto, es imperativo que las empresas reflexionen sobre qué es lo que quieren unos u otros clientes de su organización para lograr satisfacer sus necesidades y requerimientos. Aquellas empresas que han respondido esta pregunta y ajustado su modelo de negocio a estas necesidades están generándose mucho beneficio, a diferencia de quienes aún siguen trabajando con los mecanismos tradicionales, en los cuales preponderan las estrategias generales, llamadas telefónicas o mensajes a los dispositivos digitales con información de productos o servicios que no deseamos. Debemos aprender de los clientes, como lo hace El Tiempo, a fin de personalizar las estrategias.

---

<!-- Página 17 -->

El objetivo del periódico al crear e implementar las estrategias de personalización es doble: por una parte, busca fidelizar a los consumidores de las noticias y que su base de información sea el diario; por otra parte, crear un espacio de personalización que fideliza a los usuarios y les permite conocerlos cada vez más, además de aumentar sus ingresos, dado que vende los espacios laterales de su página web a otras empresas para que estas agreguen banners con publicidad de sus productos y servicios, lo cual también es personalizado. Por ejemplo, si El Tiempo identifica que los jueves y los viernes las personas con ciertas características (con x rango de edad, con y nivel educativo, con z género, etcétera) leen la sección de Política, esta información se la comunica a la empresa interesada en publicitar sus productos y comprar el espacio para que suba un anuncio personalizado para ese segmento o tipo de público descrito, lo que resulta beneficioso para ambos. A partir de los casos anteriores, advertimos grandes beneficios con el uso inteligente de los datos en dos sectores completamente diferentes. Al respecto, muchos consideran que business intelligence, analytics o big data solo se pueden implementar y son útiles para las grandes y medianas empresas; sin embargo, lo cierto es que, si regresamos a los conceptos nativos de estas soluciones, nos refieren a información que se utiliza para apoyar la toma decisiones, sin precisar ningún tipo o tamaño de empresa. ¿Acaso una empresa pequeña no merece también tomar mejores decisiones? Claramente, la respuesta a este cuestionamiento es afirmativa. Y, si para hacerlo

---

<!-- Página 18 -->

necesita los datos, pues será el momento de considerarlos, aunque guardando distancias. Así, una empresa grande tendrá una inversión mucho mayor en infraestructura y licencias de tecnología que una empresa pequeña, en la cual será significativamente menor. El big data nos propone el gran reto de aprovechar los grandes volúmenes de datos que hoy nos rodean, con la evidente necesidad de incorporar tecnología apropiada para que se puedan gestionar adecuadamente. No obstante, esto no es lo más importante que debemos resaltar, sino la contribución estratégica que brindarán estos datos para la generación de beneficios muy tangibles a nuestras organizaciones.

---

<!-- Página 19 -->

# Capítulo 2.

# La variabilidad en el mundo big

# data

La comprensión del mundo del big data requiere que nos refiramos a una de sus principales características: la variabilidad de datos, que en un sentido estricto alude al uso de datos estructurados y no estructurados. Las organizaciones que utilizan big data primeramente guardan información de sus clientes en una base de datos estructurada. En esta, por ejemplo, empresas como Netflix registran de manera inmediata todos los datos de la visualización de sus usuarios (el título de la película o la serie vista, en qué fecha ven el producto audiovisual, en qué momento del día, entre otros) y, luego, los utilizan como fuente de información para crear estrategias para el negocio. A su vez, guardan datos no estructurados que provienen de las redes sociales de los clientes y la información que estos comparten en otras plataformas o aplicaciones digitales distintas a las de las propias organizaciones de las que pueden obtener información de forma directa. Todos esos datos que las empresas adquieren de las redes sociales, las plataformas y aplicaciones digitales los suman a la información

---

<!-- Página 20 -->

que pueden registrar de manera inmediata para realizar un análisis y conocer más al usuario. A esta combinación del uso de bases estructuradas y bases no estructuradas se denomina variabilidad de datos. Definamos un poco más a profundidad en qué consiste este concepto y cuándo las empresas comenzaron a hablar de este. Antes de que apareciera el fenómeno de las redes sociales y la telefonía inteligente que trajo consigo la transformación digital, las organizaciones recogían, almacenaban y procesaban la información de la empresa en bases de datos estructuradas. Así, observamos que una variedad importante de fuentes de información que hoy es utilizada por las empresas para apoyar sus estrategias y toma de decisiones ha sido creada recientemente; aunque los grandes volúmenes de información habían aparecido hace 20 años al mismo tiempo que redes sociales como Facebook o Twitter, fundadas en 2004 y 2006, respectivamente, y más recientemente han mostrado su importancia con el uso de teléfonos inteligentes y otros dispositivos móviles como el iPhone y el iPad, lanzados en 2007 y 2010, respectivamente. La creación de todos estos nuevos canales hizo necesario el desarrollo de la iniciativa del big data. Las empresas requerían capturar, gestionar y analizar también los datos que se encuentran en esas bases no estructuradas y que no podían ser almacenados, procesados y gestionados en una base estructurada, pues esta última no era adecuada por el formato para el que fue diseñada. Y eso es precisamente lo que el uso del big data les permite hacer a las empresas de hoy: reunir esta variedad de información de ambas bases para tener mayor conocimiento de sus clientes. Una base no estructurada almacena enormes flujos de información para las empresas que está relacionada con las personas; esta aporta conocimientos sobre sus actividades, comportamientos de compra, ubicaciones, gustos y preferencias, personalidad, entre otro tipo de información de la cual toda organización debe aprender para satisfacer las necesidades del mercado y seguir creciendo en el tiempo. Esos flujos de información o variedad de datos, a los que las empresas no tenían acceso, ahora puede recogerlos el big data para ellas, los cuales son obtenidos de

---

<!-- Página 21 -->

mensajes, del rastro de la personalidad y de los gustos que los internautas dejan con los botones de likes y demás plugins sociales en sus redes o blogs, señales GPS, videos, interacciones que tienen las personas con plataformas y páginas web de empresas, lectura de sensores, incluso, imágenes que se publican en las redes sociales, entre otros que le permiten brindarles un mayor conocimiento de los clientes. Dado que en la actualidad los dispositivos, las plataformas y las redes sociales donde se encuentran estos datos forman parte de nuestra cotidianidad, sumado a que el big data requiere menos tiempo para el almacenamiento y procesamiento de los datos, así como menos costos en el aprovisionamiento de los elementos — tecnológicos y de computación como la memoria o el ancho de banda — que requiere para ello, favorece a que cada vez más las empresas quieran realizar un uso intensivo de estos datos. Así, con la digitalización de la actividad empresarial, estas nuevas fuentes de información se deben combinar con las fuentes de información tradicionales, llevando así a las empresas a esta era de variabilidad de datos. En suma, la variedad en el mundo del big data se trata de recoger y combinar más datos de distintas fuentes y en diferentes formatos para aprovecharlos en la generación de valor en las organizaciones.

## 2.1 ¿Cómo obtienen esa cantidad y

## variabilidad de datos las empresas? Las empresas pueden obtener todos estos datos porque las fuentes de información que hemos mencionado poseen algoritmos que permiten leer y recoger una cantidad ingente de datos de cada persona, quienes al usarlas posibilitan a sus programadores a compartir esta información con otras organizaciones y entidades de carácter público y privado de las que son usuarias. Esto, por una parte, porque el dato es el activo con el que estas fuentes de información trabajan; y, por otra parte, porque las empresas con las que interactuamos desean aprender más de nosotros para mejorar nuestra experiencia de compra y cumplir sus objetivos

---

<!-- Página 22 -->

empresariales. Sin embargo, muchos usuarios de redes sociales desconocen el carácter que tiene esta información porque nunca se han preocupado por esta; su interés se centra mucho más en conectarse con otras personas, buscar entretenimiento, comunicar algo (lo que se hace, siente o piensa), expresarse, contar o debatir sus ideas. En ese afán, nadie se pregunta ¿por qué estos productos son gratis?, y lo cierto es que hoy todos tenemos acceso gratuito a las redes sociales, precisamente, porque los datos a los que les damos acceso son información compartida. En un documental de Netflix, llamado El dilema en las redes sociales, se dijo que “si un producto es gratis, el producto eres tú”, y efectivamente es así porque a las redes sociales les interesa acceder a nuestra información para venderla. Ese es el modelo de negocio de las plataformas digitales y redes sociales, entre otro tipo de empresas, como el periódico El Tiempo, que obtiene información sobre nosotros con los rastros que cada usuario deja de sí en su base de datos estructurada al ingresar a su dirección URL <https://www.eltiempo.com/>, visualizar las noticias que le interesa y, por lo tanto, el tipo de noticias que consume. Además, el diario se remite a nuestras redes sociales para ampliar la información que tiene sobre nosotros y, de esa forma, obtiene datos no estructurados que, al juntarlos con los estructurados, enriquecen la información de cada usuario. Así, nos conoce mucho más y con ese conocimiento lanza estrategias de personalización. La información proviene, entonces, de los rastros de personalidad y preferencias que los usuarios dejan en sus lecturas del diario en versión digital, pero también de la consulta de la información pública en sus redes sociales, donde el periódico verifica si un usuario comenta mucho o poco sobre un tema o si abre discusiones sobre este con amigos o conocidos para extraer conclusiones con base en ello. Retomando el ejemplo sobre un usuario que visualiza las noticias de las secciones de Política y Deporte, si toda esta información se relaciona con temas políticos, la empresa deducirá que al usuario le gusta la política y personalizará su entrada o navegación con temas políticos; igualmente, teniendo acceso a los blogs vinculados a los canales de deporte, podrá deducir que si el

---

<!-- Página 23 -->

usuario ingresa frecuentemente a ESPN o a Fox Sports es porque le gusta el deporte, incluso, puede saber cuál es el deporte de su preferencia. Así, las empresas van conociendo a las personas para ofrecerles un servicio personalizado y de su agrado. El mundo globalizado provoca que los consumidores demanden estas nuevas herramientas o experiencias. Con el big data, las empresas deben estar preparadas para tomar datos de las redes sociales, las plataformas digitales y demás bases no estructuradas para cumplir esos requerimientos de la sociedad actual. De ahí la importancia de hablar de la variedad de datos, de bases estructuradas y no estructuradas, puesto que al combinar toda la información que recogen les generan a las empresas mucho conocimiento. Este les sirve para personalizar la comunicación y el servicio con sus clientes, y no enviarles una información generalizada que no se relaciona con sus preferencias.

## 2.2 ¿Qué hace el big data con los datos

## que recoge? En los últimos años, hemos escuchado con mucha regularidad la 1 gran cantidad de datos que se genera cada día. En 2017, Deloitte afirmaba que el 90% de los datos a nivel mundial se había producido 2 en los últimos dos años. Según Statista, la cantidad total anual de datos consumidos a nivel mundial en 2021 fue de 79 zettabytes y, para 2025, se proyecta crecer a más de 180 zettabytes. Esa abundancia de información digital que les brindan hoy las redes sociales y plataformas digitales, las tarjetas bancarias, los GPS, los sensores de cámaras distribuidas por las ciudades, los teléfonos móviles inteligentes, el comercio en línea, las comunicaciones electrónicas, etcétera, apoya decididamente las operaciones y la toma de decisiones en las organizaciones. Dado que estos datos surgen con mucha velocidad y en grandes cantidades, se requiere tecnología idónea y técnicas que incorporen la estadística y la matemática para analizarlos en el menor tiempo posible y que sean aprovechados por las empresas extrayendo características, rasgos de personalidad y

---

<!-- Página 24 -->

patrones de comportamiento de compra comunes entre sus clientes, y ese es el terreno de lo que hoy conocemos como big data analytics. Esta combinación de big data y analytics viene siendo muy poderosa en esta era de alta digitalización, pues contiene una diversidad de oportunidades de uso para aplicarse en organizaciones tanto públicas como privadas, tales como las siguientes:

Conocer mucho más a los clientes.

Disminuir la fuga de clientes.

Ofrecer un mejor producto o servicio.

Conocer mucho mejor los comportamientos de compra.

Advertir la necesidad o la demanda de ciertos productos.

Atraer nuevos clientes que aumenten el rendimiento de la empresa.

Optimizar costos de producción o prestación del servicio.

Mejorar la captación de clientes.

Fidelizar clientes.

Los usos del big data analytics son tan extendidos que hasta es posible detectar si una persona puede sufrir depresión tan solo con leer la cantidad de mensajes que ingresa en una red social, las palabras que utiliza, a qué hora revisa los mensajes que recibe o a cuántas personas les ha escrito. Esto se debe a la combinación en el empleo de esta información que hace el big data al relacionar los nuevos datos con la analítica y el aprendizaje que obtuvo de los datos referentes al comportamiento de las personas que se habían deprimido antes. La comparación o relación de las características comunes o patrones de comportamiento le permiten advertir que, cuando una persona comienza a tener el mismo tipo de comportamiento, está en riesgo de entrar en un estado de depresión.

---

<!-- Página 25 -->

2.2.1 Caso Amazon La empresa Amazon ha logrado reunir mucho conocimiento sobre sus clientes, incluso más que los supermercados o los bancos, a tal grado que las propuestas y recomendaciones de productos y servicios que ofrece son muy efectivas tanto para los clientes como para la empresa, que obtiene un 30% de las ventas anuales por recomendaciones de sus clientes. Su éxito se debe a que Amazon tiene ofertas personalizadas, a diferencia de otras empresas que promocionan con un descuento especial líneas de productos o unidades con estrategias generales (le ofrecen a todos lo mismo), lo cual evidentemente consigue resultados muy pobres. Estas son prácticas lamentables que aún existen en muchas empresas en nuestra región latinoamericana. Al interactuar con la plataforma de Amazon, se guarda en la base de datos toda la información de navegación de cada usuario (la hora de consulta, el día de ingreso, el tiempo que permaneció en la plataforma, etcétera), ya sea si solamente está viendo el catálogo de productos o si agrega un producto al carrito y no lo compra. Con esta información y con la que reúne de otros usuarios de la plataforma, Amazon nos lanza recomendaciones personalizadas: una serie de productos que son similares o iguales a los que otras personas llevaron con ese producto que hemos seleccionado. Esta empresa guarda una variedad de datos de distinta índole de millones de clientes, la cual no solo recoge de la interacción de los usuarios de la plataforma, sino también de las redes sociales y plataformas digitales de sus clientes. Aún más, Amazon no solo dispone del canal de venta online Amazon.com, sino que ha abierto un nuevo canal de venta físico que es Amazon Go, del cual también recopila información sobre sus clientes y su comportamiento de compra; es decir, la empresa recibe información tanto de una fuente física (compras en el canal presencial) como de una digital y todos esos datos los combina para aprender más de sus clientes. En la actualidad, se requiere que las empresas se integren en el mundo del big data, conozcan sus demandas y comiencen a ver todos los beneficios que aún no han descubierto. Para ello, es

---

<!-- Página 26 -->

necesario que se realice un tratamiento de los datos, lo que implica, a su vez, que las organizaciones tengan conocimiento, entre otras cosas, de las 4V con las que debe contar el big data.

Las 4V del big data En los últimos años, se han planteado diversas alternativas de las V que gobiernan el mundo del big data, pero consideramos que las cuatro que se presentan son bastante representativas. Así que el volumen, la veracidad, la velocidad y la variedad permiten caracterizar las cualidades que el big data le propone al mundo. El volumen es la primera característica que comprende el big data y que, de hecho, se plasma en su definición. Ahora bien, este gran volumen de datos viene acompañado de otras tres características: en primer lugar, la cantidad de datos generada se debe recoger con un nivel de calidad alto, es decir, el big data exige veracidad; sin embargo, que se maneje un gran volumen de datos no significa que estos se produzcan de forma lenta, pues el mundo de hoy exige velocidad, y así surge la tercera V. Al mismo tiempo, este manejo de cantidades ingentes de datos implica que el big data debe recoger información de diversas fuentes de datos, incluyendo aquellas que están completamente desestructuradas, especialmente ahora que estamos inmersos en un escenario de transformación digital y avances tecnológicos; es aquí donde aparece el concepto de variedad, dado que los datos se pueden tomar de mensajes, información de GPS, imágenes, audios, videos, plataformas digitales, redes sociales, etcétera. Todos estos canales y elementos se combinan en este escenario de la variedad para que tengamos mucha más información de la que nos proporcionaban únicamente las bases de datos tradicionales.

---

<!-- Página 27 -->

Ahora bien, al hablar de variedad de datos, es importante aclarar que la información no se encuentra cohesionada. Muchas empresas piensan que esto es necesario para generar aprendizaje; sin embargo, hoy es posible usar algoritmos que permiten realizar una lectura de la orientación política, religiosa, sexual, deportiva, entre otras preferencias de las personas, a través de los likes e interacciones como los plugins y los comentarios de los usuarios en las redes sociales y las plataformas digitales en las publicaciones. Es así porque todas estas interacciones tienen una connotación. En el caso de darle like a algo, significa que estamos viendo un contenido que nos gusta; por ello, con una cantidad importante de likes, un analista puede percibir una gran certeza de la información que está detrás de las pantallas, como la personalidad de los usuarios.

Muchas organizaciones pueden aprovechar este tipo de interacciones de sus clientes para generarse oportunidades. Por ejemplo, cuando una persona le ha dado like a una receta en el blog de un supermercado y, en un momento posterior, se detecta que ha ingresado a alguno de sus locales (lo cual se puede saber si se tiene un lector de código QR), inmediatamente este le puede lanzar una promoción de descuento en todos los insumos de la receta a la cual le ha dado like. Esta es una estrategia muy personalizada que requiere

---

<!-- Página 28 -->

una gran cohesión entre los distintos canales en una empresa. A continuación, se citan dos experiencias que permiten resaltar usos potenciales de la variedad de datos que propone big data, la primera corresponde al sector de salud pública, cuyo empleo inteligente de datos genera mucha contribución social; y la segunda, al sector hotelero, que, mediante una práctica enmarcada en su proceso de transformación digital, está consiguiendo desarrollar estrategias muy efectivas para conocer, captar y fidelizar clientes.

2.2.2 Caso Prestadoras de salud en el sector Gobierno Hace aproximadamente ocho años, estuve trabajando con la entidad que administra la gestión de salud estatal en uno de los países de nuestra región. Allí identificamos una problemática vinculada a la cantidad de subsidios que el Gobierno nacional les entregaba al año a los trabajadores por lesiones o enfermedades que requieren varios meses de incapacidad laboral temporal y reposo. En ese momento, los subsidios alcanzaban un aproximado de 16 000 000 dólares anuales. Al analizar los datos de las personas que el Gobierno subsidió en los últimos cinco años, encontramos patrones similares y características comunes que permitieron relacionar una enfermedad con trabajadores que desarrollaban cierto tipo de actividad, en un rango específico de edad, ubicación geográfica, enfermedades congénitas, entre otros datos internos y externos; y, a la vez, reconocer similitudes en estos aspectos con otros trabajadores. De ese modo, este uso de los datos posibilitó identificar la probabilidad de que esas personas también sufrieran el mismo tipo de afecciones, lesiones o enfermedades. Con esta información, la entidad puede desplegar labores de prevención y campañas de salud para evitar que un porcentaje importante de esos trabajadores se enferme, así como disminuir la cantidad de subsidios por incapacidad laboral temporal. Al bajar el aporte anual de subsidios en algunos millones de dólares, el Gobierno tenía la posibilidad de destinarlos a un mejor aprovisionamiento de medicamentos o al arreglo de la infraestructura de las entidades de salud, contribuyendo así a

---

<!-- Página 29 -->

brindar un óptimo servicio a los ciudadanos. Cabe resaltar que esta aplicación ya se está efectuando en otros países de América Latina como Colombia. El big data forma parte de la transformación digital que viven hoy las empresas de salud, las cuales buscan, con el uso de los datos, reducir el índice de enfermedades. Para ello, desarrollan labores y campañas de prevención en la población, al mismo tiempo que generan una gran contribución social. Por su parte, la Administración pública, que busca la eficiencia de los recursos, contribuye con el uso de los datos a la disminución en los gastos y a mejorar su gestión en beneficio de la sociedad.

2.2.3 Caso Meliá Hotels International Un ejemplo muy interesante que podemos mencionar es el del Hotel Meliá. Este, antes de la pandemia por el COVID-19, la cual afectó en mayor medida al sector hotelero, implementaba con el uso de datos una estrategia digital centrada en el cliente. Teniendo en cuenta que en la actualidad muchas personas prefieren contactarse directamente con los hoteles cuando van a viajar, y no recurrir necesariamente a intermediarios, o consultar en TripAdvisor u otras fuentes para leer los comentarios de otros clientes sobre los alojamientos, los hoteles Meliá tienen como pilar fundamental de su transformación digital una orientación al cliente que permite una gran contribución hacia la fidelización. Para el efecto, han establecido un manejo de datos que les permite realizar estrategias muy personalizadas, basados en lo que buscan sus clientes, en los datos de estos que obtienen de diversas plataformas y redes sociales, así como en la información de viajes anteriores que han realizado (qué hoteles han visitado, qué tipo de habitación han escogido, en qué aerolíneas han viajado, su ticket promedio, cuántas personas usualmente viajan, etcétera), respondiendo e interactuando con clientes y prospectos de forma precisa con sus intenciones de búsqueda, lo que incrementa notablemente la posibilidad de reservas. Hoy este programa de fidelización cuenta con 14 millones de usuarios y un dato muy valioso que brindaba el CEO de la

---

<!-- Página 30 -->

empresa en el 2019 era que en ese momento sus 12,5 millones de clientes realizaron el 91% de las reservas en un año. Un resultado realmente espectacular para cualquier estrategia de fidelización. La manera en que los hoteles Meliá les responden a todos sus clientes y a personas interesadas ha sido un éxito rotundo, pues sus respuestas son completamente distintas y muy personalizadas. De ahí que se le llame estrategia digital centrada en el cliente, puesto que los datos y la analítica ayudaron a descubrir elementos con los cuales la empresa hotelera podía mejorar la experiencia de los clientes. Esta iniciativa que lanzaron, denominada MeliáRewards, representaba antes de la pandemia el 80% del total de las ventas directas de la empresa. Por ello, se considera una experiencia de éxito y un ejemplo muy interesante de cómo se da la variedad de datos, pues siendo un modelo de negocio tan tradicional está aplicando un uso muy inteligente de datos y generando mucha contribución. Estas empresas son ejemplares porque han encontrado el valor de los datos y han utilizado otros medios o fuentes de información externa valiosos, como las redes sociales y distintas plataformas digitales, para conseguir un mayor conocimiento de sus clientes. Las organizaciones han demostrado cómo la toma de decisiones y la creación e implementación de estrategias basadas en datos tienden a generar muchos beneficios y rentabilidad.

---

<!-- Página 31 -->

# Capítulo 3.

# Uso inteligente de los datos para

# mejores decisiones

Muchas empresas han comenzado a emplear, junto con los datos, todo el potencial que les brindan las herramientas y los medios tecnológicos para crear nuevas unidades de negocio y mejorar la oferta de un producto o servicio desde diferentes aspectos (modo de venta, marketing, etcétera), impactando positivamente en los resultados para la organización. Ahora, si bien el manejo de los datos con big data es útil para resolver muchos problemas que afectan el rendimiento y los procesos de las organizaciones, las empresas actuales están desarrollando al máximo su capacidad creativa en lo que respecta al tratamiento de los datos y al aprovechamiento del big data y de la analítica de datos en una variedad de actividades y proyectos innovadores. Así, en la actualidad, advertimos que muchas organizaciones emplean formas de trabajo distintas que permiten recoger y procesar la información, con el objetivo de elaborar estrategias no solo para llegar a más público, optimizar sus procesos internos y aumentar su rentabilidad, sino también para mejorar la experiencia de compra y la vida de los consumidores de los productos o servicios que ofertan. En este capítulo, presentaré algunos casos de empresas que

---

<!-- Página 32 -->

incluyen los datos como activos estratégicos y que los utilizan de formas innovadoras para generar muchos beneficios económicos. Con ello, estas empresas han demostrado que su tarea respecto al uso de los datos va más allá de considerarlos un activo más, pues encontraron maneras muy inteligentes de emplearlos para obtener contribuciones significativas. Es decir, en las organizaciones, debe existir una cohesión entre el uso de los datos y su capacidad de innovación; por lo tanto, es una buena práctica analizar los casos de éxito para despertar ideas y estrategias que puedan aplicar en sus propios negocios para adquirir mayor valor. Revisemos un caso de éxito en el que se relacionan perfectamente la creatividad y la innovación con estrategias de datos en las organizaciones. Se trata de la empresa Rebecca Minkoff, una marca de ropa y accesorios fundada por los hermanos Rebecca y Uri Minkoff, que en la actualidad cuenta con más de 900 tiendas alrededor del mundo.

## 3.1 Caso Rebecca Minkoff En el sector retail de la moda, a nivel global, con la naciente era de la inteligencia artificial muchas empresas cuentan con sensores y dispositivos tecnológicos de conteo para determinar el número de personas que entra a las tiendas físicas de ropa. Esto debido a que una ratio importante para los negocios de este sector es saber cuántas personas ingresan a las tiendas y cuántas de ellas realizan compras; esto por supuesto dista aún de algunas empresas en cuyos locales se encuentra una persona en la puerta contabilizando con un contador manual la cantidad de clientes que ingresa a cada local. Ahora bien, pese a que algunas de estas empresas tenían un sistema de sensores para el conteo automático de las personas que entraban a la tienda, hasta hace unos años no disponían de ningún tipo de herramienta o plataforma analítica que les permitiera saber cuántas personas ingresaban a los probadores, cuáles y cuántas prendas llevaban a los probadores, cómo las combinaban, o cuántas de las ropas que se probaron habían comprado y dejado. Esta situación ha cambiado con el uso de la inteligencia analítica

---

<!-- Página 33 -->

en lo que se puede denominar probadores inteligentes. Estos les brindan los datos mencionados y realizan recomendaciones de prendas a los clientes con alta probabilidad de que los compren (ver el video en YouTube: <https://www.youtube.com/watch? v=_l0pJdQOsZA>). Rebecca Minkoff es una de las empresas del sector que ha resuelto esta situación y ha contribuido con este cambio en la industria de la moda. Los hermanos Minkoff que fundaron la empresa hicieron un análisis y advirtieron que aproximadamente un 33,3% de las personas que entraba a los probadores de la tienda le solicitaba a los asistentes de estas que le alcanzaran otras prendas que combinaran con la que llevaría y que no había seleccionado. La empresa hoy no solo cuenta con sensores de conteo en las entradas de sus tiendas físicas, sino también en el probador para generar datos y obtener un conteo más completo de la cantidad de clientes que compran y cómo combinan las prendas y los accesorios. Esta información le sirve de insumo para efectuar futuras recomendaciones a clientes con gustos similares. De ese modo, mediante el análisis de datos del probador, a la empresa le ha sido posible sugerirles a los clientes una cantidad de combinaciones de prendas que no habían pensado hasta ese momento y que probablemente les gustarían y las comprarían al verlas, o incluso algunos accesorios con los que pueden completar el outfit escogido. Así es como la empresa ha modificado la experiencia de compra de las personas que visitan sus tiendas, con lo cual han logrado triplicar el número de prendas vendidas en el periodo estudiado.

A partir de esta experiencia, otras marcas famosas se han sumado a este tipo de manejos de probadores inteligentes, como Zara y

---

<!-- Página 34 -->

Mango. Inclusive, recientemente, en el mismo sector retail, también se ha comenzado a utilizar la realidad virtual y a incorporar los escáneres 3D para personalizar aún más la experiencia de compra. Desde 2016, las distintas marcas han empezado a usar las plataformas y visores de realidad virtual como las Oculus Rift y las Google Cardboard en sus tiendas, con el objetivo de incluir en la experiencia del diseño a los clientes que los visitan. Asimismo, la empresa Rebecca Minkoff ha dado un paso más adelante y hoy les ofrece a sus clientes vivir la experiencia de las pasarelas con estos visores, desde cualquier lugar en el que se encuentren. En todos los casos, se identifica un manejo analítico de los datos para que, de acuerdo con la prenda que cada cliente usa y las características de la persona que está en el probador, se le alcancen determinados productos como complemento. En consecuencia, para las empresas, es fundamental saber desarrollar su capacidad creativa, así como inyectar una forma de trabajo distinta adaptando estos ejemplos de uso inteligente de los datos a sus modelos y unidades de negocio, para que las estrategias que apliquen sean verdaderamente efectivas. Se trata, pues, de combinar los datos generados con la capacidad creativa que debemos impulsar en nuestras empresas.

## 3.2 Caso Entidades tributarias Las organizaciones del sector público también tienen mucha oportunidad para combinar su capacidad creativa y el uso de datos en beneficio de su gestión. Hay entidades tributarias que, con el apoyo de empresas que manejan datos de redes sociales, se pueden alimentar de información valiosa que les permitan conocer mejor a sus contribuyentes, y así mejorar la gestión tributaria. Se trata de identificar información incompatible que las lleve a activar acciones tributarias focalizadas; por ejemplo, detectar viajes de vacaciones recurrentes de ciertos contribuyentes por sus fotos publicadas, pero cuyos ingresos reportados a la entidad tributaria no guardan proporción con estos. La personalización que el mundo demanda hoy se pone aquí en

---

<!-- Página 35 -->

práctica para asociar acciones tributarias de acuerdo con las características de cada contribuyente. Se aprecia que es necesario el cruce de información que proviene de fuentes externas a la institución, sin caer en temas éticos, que se cohesionan para generar un aprendizaje de los contribuyentes, junto con la información interna tributaria, donde se pueden evidenciar hallazgos de interés. Esto evitará las prácticas generalistas y, más bien, se apelará a la personalización de las acciones. De igual forma, se pueden organizar los datos de los contribuyentes para que, según sus comportamientos de pago habituales, se distingan los regularmente buenos pagadores de los malos, a fin de personalizar las acciones de cobranza. La mala noticia es que habitualmente se les cobra a todos por igual, lo cual en muchos casos provoca una gran insatisfacción. Por ejemplo, en cierta oportunidad, detectamos en una entidad tributaria a contribuyentes con un buen comportamiento de pago, pero que, por algún motivo particular, no habían cancelado a tiempo; aún así, la entidad les lanzó acciones de cobranza como si pagaran regularmente mal. Cuando les hicimos la observación, la respuesta fue que la “norma” dispone que a todos se les debe tratar igual. Si una entidad de Gobierno tiene como premisa fundamental generar la satisfacción de los ciudadanos, definitivamente, estas prácticas deben cambiar, y los datos son un aliado para lograrlo.

## 3.3 Big data en el deporte El uso de analítica de datos y big data también llegó al deporte. En la Copa Mundial de la FIFA Brasil 2014, se comenzó a implementar el sistema GoalControl-4D. Este se basaba en el uso de cámaras de video con capacidad de procesar los datos que recogían para determinar si el balón cruzaba la línea de gol y evitar la anulación de un gol cuya anotación no ha sido comprobada y validada en el partido. En esta Copa Mundial, también hubo algunos equipos que utilizaron la analítica de datos para crear estrategias tácticas. Este fue el caso de la famosa goleada de semifinales en el partido

---

<!-- Página 36 -->

Alemania vs. Brasil, donde el marcador quedó 7 a 1. Detrás de este evento, hay una historia en la que los datos tuvieron una gran implicación. Años atrás, la selección de fútbol de Alemania usaba la aplicación Match Insights, un producto desarrollado por la empresa SAP Enterprise Portal que trabaja con la analítica de datos, la cual le permitía ver el recorrido de los jugadores, su posición y velocidad en el campo, su rendimiento en el partido y en las áreas que ocupaban para obtener métricas de rendimiento, y hacer los respectivos cambios y sugerencias, así como para analizar el comportamiento y las debilidades de los contrincantes, y aprovechar tácticamente —a nivel individual y colectivo— toda esta información para ganar los encuentros. En ese sentido, el uso de esta iniciativa en el fútbol ha cobrado mayor relevancia al advertir que la cantidad de información que los equipos recibían al utilizar la analítica de datos era similar a la que podían obtener viendo alrededor de 20 a 50 partidos anteriores de la selección rival. Otras selecciones como las de Uruguay y Honduras también usaron el football analysis en su planteamiento táctico en la Copa Mundial de la FIFA Sudáfrica 2010, donde ambos equipos llegaron a las rondas de semifinal y final, respectivamente. A esto se le conoce hoy como sports analytics; pues ya no solamente se aplica en el fútbol, sino también en el béisbol, en el básquetbol, en el tenis y en otros deportes que están aprovechando toda la información que les brinda este tipo de datos para elaborar sus planteos tácticos. Ahora bien, no en todos los equipos y los clubes ni en todas las disciplinas deportivas se está implementando, pero fijémonos cómo lo están haciendo. Tanto en el cuerpo técnico como en los vestuarios de los estadios se toman decisiones basadas en los datos, principalmente, para aumentar el rendimiento individual y colectivo de los jugadores y conocer las debilidades de los equipos rivales, aunque también para prevenir las posibles lesiones en los jugadores. Para ello, les colocan a los jugadores un sujetador deportivo con tecnología wearable, que lleva incorporado un sensor que guarda mucha información generada durante su recorrido en los entrenamientos y sirve para monitorear su juego y desempeño en el

---

<!-- Página 37 -->

campo. El sensor monitorea las pulsaciones de los jugadores; además, cuenta con un acelerómetro para que los analistas puedan observar cómo se mueven en todas las direcciones y un sistema GPS para medir su velocidad y las deceleraciones, así como las distancias que recorren y posibles desequilibrios mientras corren para prevenir una lesión. Así, este sujetador funciona como una importante fuente de información que sirve para alimentar un banco de datos numéricos. Luego, este se relaciona para que los técnicos obtengan la información necesaria y sintetizada de todos los miembros del equipo, y con base en esta puedan elaborar su planteamiento táctico y dirigir a los jugadores a nivel individual y colectivo. Esta tecnología se aplica en muchos equipos y les sirve para afianzar las fortalezas de los jugadores, pues en la analítica también se considera el ratio de esfuerzo pasivo; es decir, las medidas y los datos numéricos que están relacionados con su estado físico y su rendimiento, pero que se toman de la cantidad de horas de sueño de cada jugador, su nivel de cansancio o estrés, y su percepción del nivel de exigencia físico y mental en los entrenamientos. De acuerdo con la lectura de los analistas de los datos que registra el sensor sobre el estado de todo el equipo, el técnico puede efectuar una valoración distinta de cada jugador. Así, es posible saber si un jugador se acercó a su punto de fatiga y debía recorrer más kilómetros en el partido, pero no lo hizo y, por lo tanto, tiene que fortalecer ese aspecto o descansar; si hay un jugador en riesgo de sufrir una lesión; o qué jugadores se encuentran en un estado de mayor rendimiento. A su vez, esta información les sirve de insumo a los técnicos para tomar decisiones respecto a los descansos, el tiempo de juego que tendrá cada futbolista, entre otros aspectos. De esa manera, sacan conclusiones tanto para sus equipos como para cada jugador, y también pueden estudiar a un rival para aprovechar sus debilidades y generarse una ventaja. Estos casos demuestran que, en la medida en que una persona confía más en los datos, en este ejemplo el técnico del equipo deportivo o del club, podrá sumar toda esta información valiosa que le generan a su planteamiento táctico, lo cual le brindará una ventaja en el campo y la posibilidad de aumentar el rendimiento de sus

---

<!-- Página 38 -->

jugadores. Otro uso muy potente de big data en el deporte es en la Fórmula 1. Su aplicación se ha convertido en un default. Todas las escuderías lo utilizan con la finalidad de tomar decisiones con mucho sustento y, por supuesto, en este deporte, el margen de tiempo del que disponen es muy corto. Para ello, los autos tienen entre 150 y 300 sensores que miden su comportamiento, siendo posible obtener información relevante que permite no solo tomar decisiones estratégicas durante la carrera, como ajustes por realizar o paradas en los boxes, sino también para conocer el comportamiento del auto y con esto poder generar optimizaciones. Hay sensores cuya ubicación solo la conocen los ingenieros de cada equipo, pues los datos que aportan pueden suponer una ventaja competitiva o quizá evidenciar una debilidad. Hay otros sensores que están a la vista, ya que son de uso común, por lo que cualquier persona puede verlos fácilmente; por ejemplo, los que evalúan la velocidad y aerodinámica del coche, o los que aportan información sobre los neumáticos. Quien cuenta con más datos puede tener mayor ventaja competitiva, así que se busca la manera de medir hasta el último detalle. Cabe precisar que la clave no es la cantidad, sino el análisis y explotación de los datos; por ello, hoy vemos que las escuderías adquieren las mejores plataformas de análisis de datos del mercado, además de los mejores profesionales para utilizarlas. Los deportes se seguirán sumando al poder de los datos, en la medida en que vayan identificando el valor que les pueden generar. Se trata de confiar, de realizar las pruebas del caso y de invertir en plataformas tecnológicas que faciliten el análisis correspondiente. En los casos que he presentado en este capítulo, el uso del big data sigue en aumento gracias a los procesos de transformación 3 digital que atravesamos. De hecho, según la consultora Accenture, no se puede concebir un proceso de transformación digital sin big data, dado que necesitamos establecer nuevos modelos de negocio para satisfacer las necesidades de un consumidor cada vez más digitalizado. En este esfuerzo, las organizaciones deben recoger información de múltiples fuentes de datos, como plataformas digitales, redes sociales, base de datos, etcétera, y esto representa la

---

<!-- Página 39 -->

tarea esencial que realiza el big data en un sentido estricto. De este modo, el universo de opciones que tienen las empresas para implementar estrategias de uso de datos es infinito, solo se requiere creatividad para desarrollar proyectos innovadores que transformen diversos procesos o áreas dentro de la organización. Esta es la forma en que podrán ver materializados los beneficios reales que tienen los datos en el mundo de los negocios y en las entidades públicas.

---

<!-- Página 40 -->

# Capítulo 4.

# Los datos como activos

# estratégicos

Dentro de las organizaciones, existen muchos activos que contribuyen diariamente a su correcto funcionamiento, tales como la infraestructura, la tecnología de punta o el personal calificado; sin embargo, existe uno que tiene un gran valor y que muchas veces no se considera: los datos. Por ello, en este capítulo, analizaré por qué los datos se deben tratar como activos estratégicos para operar como una verdadera organización basada en ellos, y así lograr generarse mucho valor y diferenciarse en este escenario altamente competitivo. En la actualidad, muchas organizaciones gestionan los datos y cada vez de una manera más intensiva, por supuesto, con la gran finalidad de generarse beneficios, lo cual las está llevando a obtener ventajas competitivas. Además, cuentan con estructuras organizacionales y procesos preparados para un aprovechamiento constante y proactivo de los datos. Han establecido, también, una cultura basada en el análisis, de mucha confianza en los datos y que les permite apoyarse decididamente en estos para facilitar su gestión a todo nivel. A estas empresas se les puede denominar “analíticas” debido a que reúnen datos, los analizan y actúan a partir de ellos. Estas son

---

<!-- Página 41 -->

organizaciones que descubrieron el gran valor que tienen los datos para la generación de beneficios, lo cual puede ser difícil de asimilar para quienes aún apelan solo a la intuición para su toma de decisiones. Sin embargo, cada vez son más las organizaciones que se suman a la necesidad de basar sus acuerdos en la evidencia, dado que, a mayor sustento, estaremos contribuyendo a la toma de mejores medidas.

Ahora bien, a muchos les podría desanimar la gran cantidad de datos que se produce en el mundo, dada la complejidad detrás de la administración de un gran volumen y variedad de tipos de datos. No obstante, es precisamente aquí donde vemos la riqueza, pues los audios, los videos, las plataformas digitales y las redes sociales, además de las bases de datos, nos permiten adquirir un mayor conocimiento. Con todo esto estaremos en excelentes condiciones para mejorar la experiencia del cliente, optimizar procesos de gestión, añadir valor a los productos o servicios, o crear nuevos modelos de negocio. Para que se genere este tipo de contribuciones, es necesario que comencemos a tratar los datos como verdaderos activos estratégicos. Para ello, se debe realizar una buena administración del recurso, es decir, gestionar los datos para lograr un correcto almacenamiento y acceso a estos. Se trata de evitar las islas de información que abundan en las organizaciones y dar paso a un almacenamiento

---

<!-- Página 42 -->

centralizado que permita el acceso democratizado a cualquier usuario que lo requiera, salvaguardando siempre los niveles de seguridad de ingreso y el ámbito de responsabilidad de cada uno.

## 4.1 Descubriendo el valor en los datos

El primer paso hacia el establecimiento de los datos como un activo estratégico es encontrar su valor. Se trata, pues, de evidenciar la contribución decisiva que impactará en la rentabilidad de un negocio o la rentabilidad social en una entidad de Gobierno. Aunque esto suena algo novedoso, lo cierto es que hay quienes ya identificaron ese valor hace muchos años y, desde entonces, vienen generando mucha diferenciación en el mercado mundial. Cabe recordar que las definiciones nativas del concepto de business intelligence ya nos decían que este se trataba de un proceso para convertir los datos en conocimiento, y el conocimiento, en acciones para producir la ventaja competitiva del negocio. Hay quienes ya tomaron esto para convertirlo en una gran oportunidad. Una empresa a la que quiero referirme para graficar esta asociación de los datos con la ventaja competitiva es Walmart, una transnacional considerada como la cadena de supermercados más grande del mundo y que encontró en los datos ese valor que ha contribuido significativamente en su ventaja competitiva. Si reflexionamos sobre cuál puede ser la ventaja competitiva de una empresa como Walmart, hallamos alternativas como precios bajos, disponibilidad de muchos productos, presencia en muchos lugares, las cuales son muy válidas, pero encontró algo más: comportamientos de compra distintos dependiendo de la geografía donde se ubican sus locales —denominado como el comportamiento geodemográfico—. Precisamente, abastecer sus tiendas considerando este conocimiento le genera un gran valor, dado que, si se quedan con productos en stock, es dinero muerto en el almacén; en cambio, si tienen stock cero de otros productos, dejan de vender. Por ello, su ventaja competitiva se encuentra sustentada en la eficiencia de la cadena de abastecimiento. Es decir, se trata de aprender de los datos para establecer estrategias de negocio ganadoras.

---

<!-- Página 43 -->

Veamos ahora el caso de una entidad del sector Gobierno que tiene entre sus funciones la supervisión de diversas instituciones, una tarea repetitiva que realiza cada mes. Esta labor cuenta con un presupuesto asignado, por lo que mes a mes debe seleccionar cuáles son las instituciones que inspeccionará; así, luego de llevar a cabo las tareas correspondientes y finalizar el proceso, se obtiene un grupo minoritario de entidades que presentó anomalías en la supervisión. El problema es que se trata al proceso como si su finalidad suprema fuese la supervisión en sí cuando el propósito es encontrar una mayor cantidad de instituciones con anomalías, de manera que se logre un mayor beneficio para la sociedad. Es aquí donde ingresa la analítica de datos para optimizar el proceso de selección de las instituciones que se supervisarán. Imaginemos que esta entidad puede conocer de antemano qué instituciones tienen una alta probabilidad de mostrar anomalías; de ser así, podría seleccionarlas con mayor evidencia, lo cual aumentaría la eficiencia del proceso. Para el efecto, se trabaja la información de todas las instituciones que presentaron anomalías en las supervisiones anteriores para encontrar las características comunes entre ellas. Después, al comparar este perfil con la base de datos de las instituciones para elegir a cuáles supervisar, se pueden identificar las que tienen mayor probabilidad de presentar dichas anomalías y seleccionarlas para supervisarlas. Es decir, se trata de encontrar el valor que tienen los datos para beneficio de la organización. Un tercer ejemplo que me gustaría citar es una experiencia que viví, junto con mi equipo, en una entidad de cobranza hace algunos años. Esta entidad, como la gran mayoría de las organizaciones o áreas dedicadas a esta labor, tiene prácticas muy establecidas que no se atreven a cuestionar; por ejemplo, las formas de cobrarles a los clientes, de manera telefónica, virtual o presencial. Esta última es la que resulta más costosa; sin embargo, es sorprendente ver que estas entidades salen a buscar a la gran mayoría de los clientes para “asegurarse” cierto porcentaje de nivel de pago. Cuando trabajamos con esta empresa, tuvimos que demostrarle que no era necesario asumir esa estrategia con todos sus clientes debido a que no todos tienen el mismo comportamiento de pago; esto es, hay clientes que

---

<!-- Página 44 -->

sin buscarlos pagan y también otros a los que sí se debe buscar “con toda la artillería” para que cancelen. El reto aquí es que la entidad se pueda alimentar de la información histórica con la que cuenta para aprender sobre el comportamiento de los malos pagadores y de los buenos pagadores. Con base en ese aprendizaje, y usando el criterio de comparación con los clientes a quienes hoy les debe cobrar, puede encontrar quiénes tienen una alta o baja probabilidad de pago y así “personalizar” la acción de cobranza; por ejemplo, a algunos clientes les puede enviar un recordatorio de pago por WhatsApp, mientras que a otros los debe visitar. Con estas acciones, la entidad no solo logra una gran contribución monetaria en la labor de cobranza, sino que, además, no afecta su relación con los clientes, dado que al salir a buscarlos a todos podría generar insatisfacción en aquellos que tienen un buen comportamiento de pago. Por lo tanto, el valor de los datos aquí permitió una gran contribución a la eficiencia operativa. Otro caso que quisiera mencionar es el de una empresa de remesas en la que trabajé un proyecto de business intelligence. Este permitió darle mucha visibilidad de los hechos que venían ocurriendo en su gestión comercial y en las operaciones, lo cual contribuyó a acciones de mejora. Se incorporó una funcionalidad provista por un componente de lectura de redes sociales de sus clientes e, incluso, de clientes de la competencia. Este consistió en proporcionarle a la empresa tableros de control donde se mostraban reclamos, sugerencias y comentarios de las publicaciones que hacían tanto sus clientes como los de su competidor; además, tenían la opción de permitir el ingreso de una palabra clave para buscar comentarios que la incluyeran. Así, por ejemplo, cuando se buscaban palabras como estafador o mentiroso, incluso cuando se trataba de términos soeces, el componente le permitía a la organización leer los comentarios completos donde se usaron estas palabras. También permitía ver qué agencia estaba relacionada con el comentario, quién era el autor de este y hasta se podía acceder en ese momento a su perfil de Facebook para saber exactamente quién era. El beneficio en este caso se reflejaba en lo siguiente: se encontraron consumidores que habían interpuesto reclamos o escrito un mal comentario, los cuales eran clientes recurrentes de envío de

---

<!-- Página 45 -->

remesas, pero a partir de ello dejaron de serlo. Al identificarlos, la empresa podía poner en marcha una estrategia de recuperación de ese cliente y los muchos que podían estar en una situación similar. Una contribución adicional se presentó cuando se hallaron clientes de la competencia que agregaron ese tipo de comentarios o reclamos, pues en este caso la organización tiene la oportunidad de llamar a esos clientes potenciales en una estrategia de captación. Se trata de encontrar el valor de los datos para la generación de beneficios organizacionales. A través de estos ejemplos, se evidencia la generación de valor que pueden lograr organizaciones de diversos sectores con un uso inteligente de datos. No obstante, lamentablemente, al mirar al interior de muchas de nuestras organizaciones, notamos que aún los datos se trabajan de manera superficial o que se les da un tratamiento ligero. Por lo tanto, para convertirlos en un activo estratégico dentro de las organizaciones, se necesita que estas cambien su forma de trabajar con ellos y les asignen un valor distinto, tal como proceden las organizaciones emblemáticas y de mayor éxito en el mercado mundial.

## 4.2 Garantizar datos de calidad Otro aspecto clave que debemos tener presente para impulsar los datos como activos estratégicos es garantizar datos de calidad. Generarlos es un reto al que se enfrentan constantemente las organizaciones, y esto se relaciona con situaciones diversas como el registro de malos datos, la proliferación de hojas de cálculo, los sistemas de información no integrados, los errores en procesamiento de datos, etcétera. Esta problemática se ha presentado desde hace mucho tiempo porque se han sumado años de malas prácticas internas; sin embargo, ahora es más notorio con el uso de iniciativas para el manejo de mayores volúmenes de datos como el big data. De ahí que sea necesario impulsar prácticas internas de sensibilización en las personas involucradas en cada proceso, dado que deben ser conscientes de que un dato mal registrado generará un análisis erróneo. Si una organización quiere convertirse en una

---

<!-- Página 46 -->

empresa analítica, es sumamente importante que efectúe un correcto registro de los datos. En complemento, las organizaciones deben pensar en llevar a cabo un correcto procesamiento de los datos; es decir, garantizar que el viaje del dato sea adecuado, lo cual implica tener una clara trazabilidad de todos los procesos que rodean el manejo de los datos: desde su registro y su procesamiento hasta su visualización y posterior análisis. Todos estos detalles son de suma relevancia hoy, toda vez que debemos asegurar la buena calidad de los datos y en formatos distintos, como lo propone la big data. Una de las mayores dificultades para las organizaciones, y que perjudica la labor de garantizar la generación de datos de calidad, es que están acostumbradas a convivir con bajos niveles de calidad y no impulsan prácticas para atenuar los problemas relacionados con estos. Ello provoca conflictos internos; puesto que, por ejemplo, cada usuario maneja una hoja de cálculo con la cual genera islas de información en la organización y, de ese modo, también reporta resultados distintos a los de otro usuario. Es fundamental tomar conciencia de que este escenario se tiene que revertir si aspiramos a un manejo más trascendental de los datos. Para ello, las empresas deben pensar en la integración y en poner los datos a disposición de todos. Así, aunque cada uno tendrá accesos distintos a esta información de acuerdo con su ámbito de responsabilidad, todos podrán consultar y trabajar con la misma fuente de datos. Cabe recalcar que hoy se torna cada vez más necesario impulsar estrategias que permitan tener un mejor manejo de los datos, aunque, como hemos crecido con los desórdenes mencionados, esto puede ser una tarea compleja. En ese sentido, es muy oportuno compartir el caso de una empresa del sector educación en el periodo de pandemia de la COVID-19, cuyo gerente general me comentaba que tres áreas distintas de la empresa le estaban reportando valores diferentes de un indicador clave que monitorean, y la pregunta era ¿a cuál de las tres le hace caso para apoyar su decisión? Esta clase de situaciones la encontramos con mucha recurrencia aún, pero debemos tomar conciencia de que es fundamental cambiar nuestras prácticas hacia una mejor contribución a la gestión basada en datos.

---

<!-- Página 47 -->

Asimismo, en una empresa del sector seguros, se propuso implementar una estrategia de omnicanalidad, la cual es muy demandada en el escenario actual de transformación digital, debido a que consiste en mantener un hilo conductor con el cliente, independientemente del canal por el cual este se comunica con la empresa. Esta medida le está tomando nada menos que dos años, lo que refuerza, por un lado, los desórdenes con los que hemos crecido y que demandan un buen tiempo enmendar; y, por otro lado, la decisión de muchas empresas de lanzarse al cambio, aunque pueda parecer mucho tiempo, es esencial porque representa una de las necesidades clave del cliente digital de hoy.

En la medida en que afiancemos prácticas internas para atenuar los problemas de calidad, fomentaremos un manejo de datos mucho más confiable, lo que se convierte en un gran impulso para las iniciativas de big data en las organizaciones.

## 4.3 Democratizar el acceso a los datos a

## nivel organizacional Muchas organizaciones guardan bastante reparo en el acceso a la información, lo cual puede provocar un perjuicio al proceso de toma de decisiones de quienes la requieren. Si bien es necesario salvaguardar la seguridad de los datos, también lo es brindar el

---

<!-- Página 48 -->

debido acceso para generar dinamismo en la gestión. Un mes antes del inicio de la pandemia estuvimos en un banco de primera línea en Perú, y una persona del Área Comercial nos compartió una experiencia. Hace poco tiempo, necesitaba una información para completar una campaña que estaba impulsando, pero no tenía acceso. Tuvo que atravesar un proceso burocrático interno para obtenerla y, por supuesto, cuando llegó a disponer de esta, ya era demasiado tarde para desarrollar la campaña. Muchas veces creemos que este tipo de situaciones solo ocurre en algunas entidades públicas en nuestro país, pero ciertamente sucede aún en las mejores familias.

Las organizaciones deben delinear accesos debidos a los datos, esto es, delimitar qué miembros de la organización pueden obtenerlos, pues no todos deben conocer todos los datos o la información registrada. Para ello, se sugiere elaborar una matriz donde se reúnan los tipos de datos que la empresa utiliza y qué personas o áreas pueden obtenerlos (tipo y cantidad). Con esto se cultiva la transparencia de acceso a los datos, no se detienen acciones que los requieran para la generación de valor y, sobre todo, se logran manejos más ágiles, ya que en un mundo de constante cambio debemos actuar así. Si los datos son un activo para la empresa, no puede seguir sucediendo que cuando una persona necesite una información deba atravesar largos procesos burocráticos. Esto solo ralentiza la toma de decisiones, dilata los procesos y ocasiona que caduquen las propuestas y las oportunidades para la organización. El mundo de hoy es altamente dinámico y las empresas no pueden perder el

---

<!-- Página 49 -->

tiempo en estos procesos que de ninguna forma contribuyen a su crecimiento. Así, la catalogación de los datos como activos estratégicos debe llevar a las organizaciones a trabajar en disminuir los problemas de calidad de datos, eliminar las islas de datos o las hojas de cálculos diversas e independientes, y brindar un acceso democratizado a la información al interior de la empresa.

---

<!-- Página 50 -->

# Capítulo 5.

# La necesidad de establecer una

# estrategia de datos

Como he mencionado en el capítulo anterior, para implementar con éxito el big data en las organizaciones, el primer paso es que estas posicionen a los datos como un activo estratégico, y para llevarlo a la práctica se requiere la elaboración y ejecución de una estrategia de datos. Al respecto, según Accenture:

El 72% de las compañías a nivel mundial dice no contar con una estrategia de Datos y Analytics, y que además sólo el 33% de las compañías confía en que su data les genera valor. No obstante, las organizaciones basadas en datos están creciendo a un promedio de más del 30% anual.

La receta para lograrlo es estableciendo una estrategia de datos con un enfoque fundamentalmente organizacional. Una estrategia de datos se refiere a un plan de acción que traza una organización para aprovechar los datos como generadores de valor. Este plan debe considerar aspectos como la definición y las acciones que se deben seguir para contar con datos internos y externos necesarios para contribuir a la toma de decisiones, la gestión del cambio hacia el establecimiento de una cultura analítica,

---

<!-- Página 51 -->

los condicionamientos jurídicos para el uso de datos, la definición y establecimiento de plataformas tecnológicas adecuadas a las necesidades de la organización en su visión en el uso de datos, y la determinación de las necesidades específicas de las distintas áreas de la organización que permitan establecer los objetivos que se deben alcanzar con las iniciativas de uso de datos, y contribuir así con los logros estratégicos.

## 5.1 Uso de datos internos y externos

En el establecimiento de una estrategia de datos, es fundamental poner a disposición de nuestros usuarios de las diversas áreas de la organización los datos necesarios para el apoyo a su gestión. Para ello, es necesario definir e impulsar estrategias de centralización de datos, lo cual permitirá disponer de ellos con la oportunidad y la calidad requeridas a través de un acceso autónomo a los usuarios. En este escenario, se debe garantizar un acceso fácil, rápido, seguro y democratizado a los datos. Es importante tener presente que, en la definición de los datos necesarios, hoy se suman también de manera contundente los datos externos que posibiliten un mayor conocimiento del cliente, por ejemplo. En primer lugar, debemos identificar qué información es valiosa para los fines que se proponga la organización, y el siguiente paso es establecer los mecanismos para disponerlos como alianzas estratégicas, apoyo de empresas especializadas o producir sus propios datos con diversas estrategias de marketing. Aquí es donde debemos considerar el gran apoyo de la tecnología para capturar datos de fuentes heterogéneas, como las redes sociales, las plataformas digitales, los audios, los videos, etcétera. En este plan, se define cómo les facilitarán a los miembros de la empresa el acceso a los datos de acuerdo con su competencia y departamento de trabajo, qué manejo se les dará a los datos al interior de esta y cómo será su utilización, cuál es el proceso que deben seguir los departamentos de la empresa y los miembros de esta para compartir la información, y de qué manera se administrará la cantidad de datos y su contenido.

---

<!-- Página 52 -->

Un ejemplo muy valioso donde encontramos este uso ejemplar de datos internos y externos es la cadena de Hoteles Meliá, que como parte de su proceso de transformación digital llega a cada prospecto y cliente de forma muy personalizada a partir de la recopilación de todos los rastros que dejamos en este canal. Esto, sumado a sus datos internos, crean segmentos avanzados para permitirle abordar a cada grupo en el momento adecuado y con el contenido más relevante. Gracias a esta estrategia, se diferenció de la oferta de sus principales competidores y experimentó grandes resultados, ya que antes del inicio de la pandemia su programa MeliáRewards representaba el 80% del total de sus ventas directas. Este caso nos permite advertir que, a pesar de lo tradicional de los sectores, siempre podemos encontrar maneras de diferenciarnos de la competencia, y los datos nos ayudan de manera decisiva en este esfuerzo. Otro ejemplo que permite resaltar esta necesidad muy creciente de establecer un uso integrado de datos internos y externos para la generación de valor, como parte de la estrategia de datos que tenemos que impulsar, nos ocurrió en una entidad de cobranzas. Debido a que el servicio que brinda es por cobranzas de infracciones de tránsito, los clientes dejan deliberadamente datos incorrectos (cuando se les pide validar, por ejemplo, si su dirección actual es la que figura en el documento de identidad, ellos lo confirman, aunque luego se comprueba que en un porcentaje considerable es falso). En este caso, se podría conseguir el dato correcto de estas direcciones a través de una alianza con las entidades públicas de pago de servicio, como agua o energía, donde los datos de los clientes son correctos. Esto reduciría el problema generado en tiempo y recursos financieros para cuando se requiere contactar a los clientes para el proceso de cobranza. El uso de big data con los datos internos y externos que venimos resaltando es una necesidad latente en el contexto actual de transformación digital; para el efecto, debemos transformar la manera en que la organización utiliza los datos para tomar decisiones más rápidas y adecuadas. En este esfuerzo, se sentarán las bases para un uso más responsable de los datos en la organización. Para ello, como mencioné en un capítulo anterior, es necesario

---

<!-- Página 53 -->

identificar todos los puntos de generación de datos con mala calidad, a fin de definir acciones para atenuar este problema, y aquí, a pesar de que muchos no quieran reconocerlo, hay una gran responsabilidad de las personas que no realizan correctos registros de datos. Una buena recomendación es organizar reuniones de sensibilización para motivarlas a mejorar, dado que de sus registros de información dependerá un adecuado análisis posterior.

## 5.2 Gestión del cambio Toda estrategia de datos es el cambio hacia una cultura analítica. Por lo tanto, se trata del gobierno de esfuerzo organizacional que debe ser impulsado por la alta dirección y a todos los niveles de la empresa. El objetivo de esta nueva cultura consiste en poner a los datos como eje central de la gestión diaria de cada uno, independientemente del rol o función que cumplan, dado que ahora brindarán mayor evidencia para la toma de decisiones y, con esto, una mayor contribución a la organización. Las empresas que han reconocido el valor en los datos y han comenzado a gestionarlos, procesarlos y analizarlos para utilizarlos de forma estratégica, identificar nuevas oportunidades para el negocio, obtener mayores beneficios e, incluso, generar ventajas competitivas establecen una cultura analítica al interior de la organización. Esta importancia estratégica del dato y su gestión requieren una estructura, uso de la tecnología y procesos de trabajo concretos, los cuales deben adoptar todas las empresas que se quieran sumar al uso de estas iniciativas. El talento humano que implementa la estrategia de datos no solo incluye a los ingenieros que administran los softwares y las herramientas tecnológicas que se utilizan en la empresa y que se necesitan para la implementación, sino también, y principalmente, a los ejecutivos y a las ejecutivas de las organizaciones. Su inteligencia analítica y mentalidad crítica aplicada al uso y tratamiento de los datos como un activo de la empresa marcan la ruta de éxito de una estrategia de datos. En ese sentido, debemos identificar las diferentes capacidades en el uso de datos que se impulsarán en un proceso

---

<!-- Página 54 -->

formal de capacitaciones, pero distinguiendo entre roles como directivos y usuarios de las distintas áreas funcionales y de los equipos de las áreas de tecnología o gestión de información, e inclusive en cada grupo tenemos personas con mayor o menor acercamiento al uso de datos, lo que podría llevarnos a separar aún más los grupos a manera de subsegmentos para asociar cada capacitación que se desarrollará.

## 5.3 Condicionamientos jurídicos

Ahora que emprenderemos un uso de datos con mayor preponderancia en la organización, es necesario que tengamos mucho respeto por la forma en que lo haremos de aquí en adelante; esto porque cada vez cobra mayor importancia su empleo adecuado de cara a conseguir una mayor satisfacción de los clientes. Un 4 estudio realizado por Accenture y SASrevela que en adelante los clientes confiarán más en las empresas que demuestren mayor transparencia en el uso de sus datos, lo cual nos ubica ante la necesidad de trabajar con mecanismos éticos mediante políticas de privacidad que sean claras y sin señales de usos indebidos porque generarían insatisfacción en los clientes. Asimismo, se suma a este esfuerzo el gobierno de datos, que permite un manejo más correcto de estos, considerando aspectos como su disponibilidad, facilidad de uso e integridad. De esta manera, se logran contribuciones clave como datos fiables, integración de negocios, toma de decisiones con menores riesgos, entre otros aspectos. En ese afán, el gobierno de datos efectivo requiere que los datos sean accesibles a cada persona en el momento correcto, aunque manteniendo los niveles de seguridad de acceso solo a quienes están autorizados. Estos datos deben ser consistentes, es decir, evitar duplicidades y redundancias; pero, a su vez, conservando niveles óptimos de calidad, en cuanto a su exactitud y alineados a las normas establecidas. Finalmente, los datos deben ser susceptibles de ser auditables para explicar su origen y toda información referida a su propósito.

---

<!-- Página 55 -->

Por lo tanto, el establecimiento de la gobernanza de datos nos plantea retos hacia la integridad, la transparencia, la responsabilidad y, por supuesto, alineada a la estrategia organizacional.

## 5.4 Infraestructura tecnológica Este elemento hace referencia a todos los activos tecnológicos, técnicas y herramientas de análisis relacionados con la infraestructura de datos y de sistemas, lo cual incluye el modelo de gestión de la informática de datos de las empresas, así como las plataformas técnicas y su integración. Es particularmente importante que la organización, a través del Chief Data Officer (CDO), defina la hoja de ruta que se seguirá con respecto a la estrategia de datos que se aplicará, y en base a esto tendrá sentido la definición de una u otra plataforma tecnológica. Aquí será especialmente importante la alianza de cada organización con empresas de tecnología, a fin de proponer la mejor arquitectura a partir de los estándares de la organización, pero de acuerdo con la visión en el uso de datos que hayan definido. Para el efecto, es necesario planificar las iniciativas basadas en datos que puedan visionar el norte al cual se dirigirá la organización, en cuanto a su capacidad de generación de valor apoyándose en datos. Esto permitirá definir, a su vez, el soporte tecnológico que se debe incorporar en este proceso, dependiendo del grado de avance que vayan logrando. Cabe precisar que se tienen los llamados niveles de madurez en big data, en los cuales se pueden identificar precisamente estos grados de consolidación de uso de datos que vamos obteniendo en nuestra organización. Un primer nivel caracteriza a una organización en un entorno inicial en big data, en el que recién está realizando algunos pilotos para demostrar su valor. Un segundo nivel se relaciona con el establecimiento de tecnología base para efectuar análisis exploratorios de los usos primarios de big data. Un tercer nivel consiste en la generación de mayor conocimiento a partir de un análisis profundo de bases estructuradas y no estructuradas. Un cuarto nivel es una organización con casos de uso múltiple de big

---

<!-- Página 56 -->

data, mediante los cuales se generan conocimientos predictivos integrados en sus operaciones. Finalmente, un quinto nivel se refiere a una organización basada en datos, donde se tiene mucha colaboración y usos compartidos de datos a todo nivel. Estos niveles de madurez, a modo de escalones de crecimiento en el mundo del big data, nos brindan la posibilidad de delinear nuestro accionar desde los frentes estratégicos y técnicos, y comprometer a toda la organización en el esfuerzo.

5.5 Retos Este elemento considera que los usuarios de las diversas áreas de la organización propongan, a modo de retos, preguntas clave que permitan soportar su gestión y contribuir con el logro estratégico en su organización. Esto debe originar la movilización de todo el mecanismo de uso de datos comentado en los elementos anteriores. Es decir, de acuerdo con los requerimientos planteados por los usuarios, se identificarán los datos internos y externos necesarios que, salvaguardando los aspectos jurídicos, se podrán aprovechar para establecer estrategias adecuadas. En suma, se determinarán los proyectos que la organización desarrollará apoyada en los datos, como planes de mejora o proyectos de crecimiento que permitan alcanzar las metas y el estado al que se quiere llevar la organización a futuro. Por lo general, estos objetivos se establecen por sectores, por ejemplo: las empresas del sector retail generalmente tienen objetivos orientados a mejoras en los departamentos de Marketing y Ventas, para lo cual utilizan una estrategia basada en customer analytics o analítica de clientes, dada la importancia de entender el comportamiento de los consumidores; o las empresas del sector industrial y de servicios públicos, que requieren para sus actividades la obtención de información del internet de las cosas (IoT) mediante la instalación de sensores o medidores en el terreno. Las estrategias de uso de los datos necesitan la elaboración de una agenda estratégica, que se debe revisar con frecuencia, así como de proyectos estratégicos e infraestructurales soportados en los datos

---

<!-- Página 57 -->

que sean de largo alcance, pero que les permitan a las empresas ver mejoras en sus procesos y soluciones a los problemas que presentan en el corto plazo. Cabe anotar que la estrategia de aprovechamiento de los datos no puede hacerse efectiva y dar resultados en una semana, pues su aplicación y montaje son dos procesos que requieren tiempo. Para llevarla a cabo, las empresas deben invertir un costo mayor en términos de tiempo de trabajo de las personas que laboran en ellas, así como la incorporación de presupuesto para que su desarrollo sea óptimo, entre otras acciones importantes. En la actualidad, advertimos que muchas empresas, a pesar de ver los beneficios del uso de big data en las organizaciones en general, se niegan a implementar estas estrategias precisamente porque les cuesta tiempo, y porque su preocupación se centra en el resultado que obtendrán del trabajo de cada día y no en los mejores resultados que pueden alcanzar en un plazo mayor con el uso de iniciativas como el big data, por lo que dejan de lado todos los proyectos que se relacionan con estas.

---

<!-- Página 58 -->

# Capítulo 6.

# Competencias internas

# necesarias para triunfar en la era

# del big data

La implementación del big data en las empresas, como adelantamos, requiere no pensar la iniciativa únicamente en términos tecnológicos. Así, tenemos que comenzar a mirar a nivel interno qué debe cambiar en nuestras empresas, qué refuerzos implementar y qué competencias impulsar para que las aplicaciones del big data se ejecuten de manera correcta, esto es, con el enfoque adecuado. Dada la forma como se construye la arquitectura del big data, este necesita ingredientes tecnológicos aun cuando la finalidad de su aplicación es fundamentalmente estratégica. Si se considera solo su función y aplicabilidad tecnológica por la solución que brinda a los problemas de este tipo, su implementación será una tarea derivada al Área de Tecnología; sin embargo, si el big data se enfoca desde una óptica estratégica, lo cual debe definirlo la alta dirección, a partir de ella es posible que se adopte este uso de datos a nivel organizacional. Entonces, ¿quiénes son los encargados de la aplicación del big data en las empresas?

---

<!-- Página 59 -->

Muchos ejecutivos y ejecutivas todavía piensan que el manejo del big data es de competencia meramente tecnológica. Por ello, trabajan en sus empresas con este enfoque o se lo delegan a los departamentos relacionados con la tecnología y sistemas, desconociendo que los beneficios que el big data genera se materializan en la mayor rentabilidad de todo el negocio y no se circunscriben a un área específica o a aquella que lo aplica. Así, impulsar iniciativas basadas en los datos, como business intelligence, analytics o big data, implica establecer una cultura basada en el análisis y en contar con mucha evidencia para sustentar nuestras decisiones. De ahí que el impulso de esta cultura deba provenir de la alta dirección de las organizaciones. Son los directivos, por lo tanto, quienes deben impulsar la aplicación de estas iniciativas, ponerse a sí mismos el reto de implementarlas para tener una cultura analítica en sus empresas. De lo contrario, se pueden proponer y desarrollar muchos proyectos, como se ha hecho hasta ahora; pero, si no cuentan con el apoyo de la Gerencia, en lugar de fortalecerse, se irán debilitando y no alcanzarán el éxito esperado. Por ello, es fundamental que las organizaciones tomen conciencia de la importancia de establecer una cultura analítica, es decir, de tener a los datos como grandes aliados de todo el accionar empresarial para encontrar y aprovechar las nuevas oportunidades, estar atentos a los nuevos problemas y, a la vez, ganar diferenciadores en el mercado. Por consiguiente, para lograr los más altos beneficios con el uso de big data, es necesario el establecimiento de una cultura analítica.

---

<!-- Página 60 -->

Se trata, entonces, de gestionar el cambio hacia una cultura analítica de una forma eficaz. En ese sentido, se deben observar cinco elementos que son sumamente importantes en el proceso para tener una buena gestión de los datos y ver realmente los beneficios de aplicar el big data. A continuación, conozcamos cuáles son esas cinco competencias internas que requieren las empresas para triunfar en la era del big data.

## 6.1 Liderazgo La primera competencia es el liderazgo y la confianza que los directivos, gerentes, funcionarios, etcétera, deben tener en el uso de los datos, puesto que la implementación del big data necesita el impulso de la dirección de las empresas y su apoyo para establecer verdaderamente la cultura analítica en estas. La catalogación del dato como un activo no se puede quedar en el uso de los datos por parte del departamento de tecnología, se trata de generar una gran cultura analítica al interior de cada organización que implemente una estrategia de datos. Por lo tanto, sin el liderazgo ni el apoyo de los ejecutivos y las ejecutivas, no funcionará la aplicación del big data. Convertir el dato en un activo estratégico cobra mayor importancia cuando hablamos de las competencias internas, ya que las empresas necesitan líderes que no solamente adopten la idea del

---

<!-- Página 61 -->

big data para ver cómo les va con su aplicación, sino que también sean los primeros en tener la cultura analítica y convencerse de lo beneficioso que puede ser. Ellos deben tener la capacidad de liderar el proceso de cambio de cultura estableciendo metas, definiendo cuáles son esos objetivos que quieren lograr con la implementación del big data y fomentando este tipo de iniciativas en sus empresas. En la medida en que ese liderazgo se ajuste a lo que demanda el mundo actual en el uso de datos, tanto la iniciativa implementada como el establecimiento de la cultura analítica tendrán éxito. No se trata, entonces, únicamente de la cantidad de información o la calidad de los datos que recojan las empresas; sino también de la forma en que los líderes de las empresas visionan el éxito y su capacidad para determinar objetivos claros, entender cómo se comporta el mercado en un momento dado, articular y comprometer a los miembros de la empresa y los distintos departamentos, apoyar las iniciativas y trabajar por cada estrategia que se implemente, desarrollar ideas creativas e innovadoras, detectar las oportunidades, y desplegar estrategias de datos para aprovecharlas. En este punto, podemos volver a citar el ejemplo de Amazon, cuyo liderazgo fue un elemento fundamental para el éxito de la estrategia de datos. En Amazon, cuando se propuso incorporar un motor de recomendación en la plataforma, al mismo Jeff Bezos no le pareció que tendría mucho valor al inicio; aun así, debido a que la empresa trabaja como un laboratorio desarrollando sus proyectos a manera de ejercicio o taller práctico, se decidió realizar un piloto para analizar los resultados. El resto es historia, fue un resonante éxito que, como dijimos, llevó a la empresa a que sus recomendaciones representen el 30% de sus ventas anuales, y ahora esos motores de recomendación le dan la vuelta al mundo en distintas empresas que trabajan con datos. En definitiva, si en una empresa no se cuenta con un liderazgo que esté impulsando este tipo de prácticas y se desaprovechan las oportunidades, se frenará la innovación. Vemos aquí la importancia del liderazgo en el esfuerzo de implementar el big data y en el éxito que se puede alcanzar.

---

<!-- Página 62 -->

## 6.2 Gestión del talento humano

Al liderazgo, es importante sumarle prácticas internas para afianzar el establecimiento de la cultura analítica, las cuales llevan a cabo los miembros de la organización. El liderazgo debe lograr que el equipo esté dispuesto a acompañar su gestión en la empresa con los datos, no de una manera superficial y poco comprometida reteniéndolos en islas de información y hojas de cálculo independientes; sino apoyándose en ellos, en la cultura analítica y sus prácticas para basar su toma de decisiones en los datos, convencido de que estos contribuyen a mejorar su gestión. Es fundamental que la competencia humana incorpore a su gestión diaria esta cultura analítica y añada los datos en ella de una manera formal. Desde hace años, se ha comenzado a estudiar grupos de empresas a través de sus ejecutivos y ejecutivas para ver cómo manejan los datos y se ha advertido una mala práctica al respecto, dado que muchos están recibiendo información para apoyar su toma de decisiones, pero en el momento de hacerlo la dejan de lado y no la utilizan. Esto pasa aún por la consideración de que la intuición es el elemento más importante que se tiene en cuenta al momento de tomar decisiones en lugar de basarse en los datos. Si las organizaciones no tienen personas que incorporen formalmente el dato como parte de ese proceso, la iniciativa no es efectiva. Por ello, resulta crucial que sus miembros, especialmente los tomadores de decisiones, cuenten con esta competencia. Esta no solo debe ser impulsada por el liderazgo, sino que también el talento humano tendrá que alinear la estrategia de datos y la cultura analítica como una práctica interna. Además, debido a que el uso de big data demanda y hace cada vez más valiosas y necesarias las habilidades como las que desarrolla el perfil profesional de la data scientist, es importante que como parte del talento humano las empresas vinculen a estos científicos de datos, así como a informáticos y demás profesionales capacitados para manejar grandes volúmenes de información.

6.3 Equipo de tecnología

---

<!-- Página 63 -->

Las empresas también requieren herramientas tecnológicas para recoger grandes volúmenes de datos con buena calidad, procesarlos con la velocidad con la que se generan y organizar la variedad de formatos en que se presenta la información. Por lo general, la tecnología es asequible para las empresas, y tanto en el proceso de recogida de datos como en la analítica se utilizan softwares de licencia o código abierto, por ejemplo, Hadoop, que incorporan herramientas específicamente para estas tareas. Dado que muchas de las habilidades que se necesitan son nuevas para los departamentos de tecnología de las empresas, y no todos los miembros de las organizaciones deben conocer las prácticas estadísticas o matemáticas que se requieren para trabajar los datos, estas deben reunir un equipo humano que esté capacitado en el uso de la tecnología para tratar y combinar adecuadamente los datos que se generan en las fuentes de información internas y externas. Si bien la aplicación de big data debe estar acompañada de las competencias de los tomadores de decisiones, un cambio de cultura y un equipo técnico capacitado en estadísticas matemáticas y en el trabajo con los datos, hoy el científico de datos viene a ser el perfil más alineado con esta labor, dadas las competencias que se les demanda: (i) conocimiento técnico sobre cómo trabajar el dato, en estadística, uso de la tecnología, cómo generar análisis predictivos y técnicas estadísticas matemáticas; (ii) conocimiento del negocio; y (iii) capacidad de comunicación a los tomadores de decisiones. Usualmente, en varios países de América Latina, no se desarrollan estas competencias porque a los profesionales se les ha formado para desarrollar competencias y habilidades en sus disciplinas, pero no en otros campos de estudio. Por ello, muchos profesionales especialistas en marketing o en finanzas, por ejemplo, desconocen el trabajo con datos o lo consideran como una tarea netamente del Área de Sistemas. Sin embargo, también hay países en la región que han fortalecido e impulsado el desarrollo de estas competencias en las profesiones en general, pues el contexto actual demanda estas dos capacidades en las que se ha ejercitado el científico de datos.

---

<!-- Página 64 -->

## 6.4 Toma de decisiones También es esencial que las organizaciones permitan que la información esté disponible para sus miembros y los departamentos funcionales que las conforman y a los que les corresponde llevar a cabo una tarea soportada en los datos; es decir, al interior de cada empresa, debe existir una cooperación interfuncional para que las áreas funcionales trabajen juntas y compartan una visión sobre los objetivos y las metas que estas buscan alcanzar. Ello da cuenta de por qué en la era del big data las organizaciones no pueden seguir manejando los datos de manera independiente en cada departamento ni retenerlos en islas de información, sino que deben transferirlos y compartirlos para buscar y encontrar oportunidades de crecimiento, así como para hallar la solución a los problemas con este trabajo y entendimiento mutuo entre las diferentes áreas. De ahí la importancia de que las empresas presenten una cohesión entre los perfiles funcionales conocedores del negocio y los perfiles técnicos, ya que el éxito de toda estrategia de datos resulta del trabajo y de la analítica de datos que soporta la toma de decisiones. Así, si una persona utiliza la estadística matemática y la analítica de datos para identificar, por ejemplo, el perfil de deserción de los clientes de una empresa y encuentra ciertas características comunes entre los que han dejado de ser usuarios del negocio, las cuales le permiten saber qué clientes actuales tienen alta probabilidad de desertar, les corresponde a los especialistas de marketing tomar los datos que le proporciona el equipo técnico para lanzar estrategias y acciones de marketing que eviten que esos clientes se vayan de la empresa. Si no hay una cultura analítica, es probable que, una vez que la información obtenida por el equipo técnico sobre el perfil y la probabilidad de deserción de los clientes pase al Área de Marketing, esta decida no implementar ninguna acción porque aún no tiene confianza en los datos y considera que no van a desertar o confía en sus prácticas de retención tradicionales. Hay que decir que ningún modelo de analítica es infalible y por eso es necesario el rol de los tomadores de decisiones en las distintas aplicaciones del big data. En este caso, la analítica no podrá asegurar

---

<!-- Página 65 -->

con un porcentaje de probabilidad del 100% si un cliente va a desertar, pero sí predice esta acción con un porcentaje del 85%, por ejemplo, y basado en los rangos de probabilidad que lanza este análisis es que los ejecutivos toman las decisiones. Si en la base de datos de clientes hay un conjunto que tiene un 80% de probabilidad de desertar y otro conjunto con un 50% a un 60% de probabilidad, el equipo de marketing debe decidir qué estrategias o acciones de marketing segmentadas lleva a cabo con cada grupo. De ahí que sea tan importante para las empresas incorporar un equipo humano que tenga mucho conocimiento técnico y del negocio, con el fin de que el equipo funcional (en este caso, el equipo de marketing), basado en el trabajo inicial del equipo técnico con los datos, pueda convertir toda la información en acciones. Así vemos que, si bien el trabajo y las competencias deben estar cohesionados, la decisión de las acciones de marketing no le corresponde al equipo técnico.

## 6.5 Cultura analítica en la empresa Establecer una cultura analítica en las empresas significa que los tomadores de decisiones dejarán de implementar sus estrategias y acciones según su intuición y comenzarán a basarlas en datos. Asimismo, significa que las organizaciones deben abandonar el hábito de utilizar los datos como justificación o soporte de las estrategias que ya han implementado, en lugar de usarlos para impulsar esas acciones y decisiones. Retomemos el ejemplo del trabajo cohesionado que lleva a cabo el equipo técnico con el equipo de marketing para ilustrarlo. Los encargados del Área de Marketing obtienen, gracias a la analítica que realiza el equipo técnico, una clasificación de los clientes para identificar en quiénes debe centrar sus esfuerzos para retenerlos o fidelizarlos. Incluso, la analítica de datos permite conformar grupos humanos según características comunes observando sus comportamientos de compra para así lanzar promociones segmentadas que causen mayores efectos positivos sobre cada tipo de comportamiento. Todas las competencias se deben sumar para

---

<!-- Página 66 -->

asociar esas acciones: la categorización de los clientes en grupos de acuerdo con su comportamiento de compra y la decisión de lanzar promociones para cada grupo. La cultura analítica es tan fundamental para las empresas porque, dependiendo de la confianza que se tenga en el dato, estas pueden tener mayores o menores beneficios, inclusive pueden verse afectadas por las acciones que siguen tomando basadas en la intuición. En este caso, por ejemplo, si el equipo de Marketing no confía en los datos, y por eso piensa en no segmentar la oferta, sino en lanzar una promoción para todo tipo de público, puede provocar que la empresa pierda la oportunidad y el dinero destinado a la publicidad. El hecho de llegar a una mayor cantidad de personas no significa que todas o una gran parte de ellas vayan a comprar, y esta probabilidad disminuye aún más si las promociones son de productos o servicios que no están alineados a su perfil. Por ello, hoy se suman a la analítica de datos otros perfiles profesionales, no solo los que poseen conocimientos en tecnología o ingeniería de sistemas, pues las empresas buscan conocer cada vez más a sus clientes para que las estrategias de marketing sean mucho más efectivas y los productos o servicios ofertados tengan mayor probabilidad de ser aceptados por el público objetivo y potencial. Esto no significa que los datos recogidos y agrupados por los algoritmos nos dirán todo lo que necesitamos saber; como hemos visto, también se requiere que el equipo funcional realice un análisis basado en los datos para la toma de decisión. De este modo, si los miembros de las organizaciones que conforman los equipos funcional y técnico desarrollan sus competencias y las cohesionan, y estas, además, son administradas con un liderazgo adecuado, esto permitirá la formulación de estrategias efectivas para las empresas. Si los usuarios no confían en los datos, aun cuando tienen un equipo conformado por personas que han trabajado en empresas con una cultura analítica, la estrategia basada en datos no funcionará. Esto mismo sucede en el caso contrario, esto es, si las empresas cuentan con una cultura analítica y un liderazgo que impulsa la iniciativa del big data, pero no con el equipo ni la capacidad técnica para hacerlo o un recurso

---

<!-- Página 67 -->

humano que no confía en los datos. A su vez, la organización, a través del liderazgo, debe encontrar las oportunidades para aprovechar el uso de los datos y definir con claridad cuáles son los objetivos que quiere lograr. Por ejemplo, muchas empresas buscan cómo disminuir el porcentaje de deserción; otras, cómo llevar a cabo acciones de cobranza con cada tipo de cliente y disminuir la morosidad; y algunas, reducir los altos costos. No se trata, pues, de decir que se usan los datos, sino de trabajar con estos con un objetivo. En este capítulo, hemos visto la importancia del liderazgo, la cultura analítica y el expertise técnico. La aplicación del big data requiere una capacidad técnica distinta porque el especialista en sistemas anteriormente solo era formado para trabajar con bases estructuradas, pero hoy se demanda un perfil profesional que conozca y trabaje con la información generada en las bases no estructuradas, que permita que las empresas consoliden la información de distintas estructuras.

---

<!-- Página 68 -->

# Capítulo 7.

# Pasos para crear una cultura

# analítica en las empresas

Las empresas analíticas usan los datos para pronosticar el futuro, optimizar sus estrategias, mejorar su desempeño y crear ventajas 5 competitivas, afirma Thomas Davenport. Precisamente, un rasgo característico de este tipo de organizaciones es haber constituido una cultura basada en datos. Al hablar de una empresa que ha establecido una cultura analítica, nos referimos a una organización que basa todas sus actividades, decisiones y estrategias en los datos, tanto las estrategias y acciones de marketing que elaboran para promocionar un producto como las que llevan a cabo para la prestación del servicio, la oferta de dichos productos a los clientes, la eficiencia interna, entre otras. No obstante, muchas empresas siguen este proceso de manera inversa; es decir, primero, lanzan sus estrategias de marketing o comerciales, por ejemplo, y, posteriormente, utilizan los datos para justificar la ejecución de la estrategia y definir si esta fue efectiva o no. Ahora bien, siendo el dato un activo estratégico para las organizaciones, este es el elemento que se debe considerar como insumo, guía o base para elaborar las propuestas y acciones de marketing; y no como justificación y soporte de las decisiones

---

<!-- Página 69 -->

tomadas. El manejo de los datos debe ser una acción que preceda a la toma de decisiones y a la creación y puesta en marcha de las estrategias en las empresas. Las empresas analíticas son aquellas que aprovechan los datos y los usan todos los días para apoyar la toma de decisiones, las distintas actividades y las unidades de negocio que son competencia de diferentes áreas de la compañía. Sin embargo, llegar a serlo no suele ser una tarea sencilla, toda vez que los grandes obstáculos no son tecnológicos, sino principalmente culturales. Si bien podemos citar y comentar la necesidad de apoyarse en datos para tomar decisiones, esto implica un cambio de mentalidad, lo cual, por supuesto, es complicado. En nuestra idiosincrasia, se prefiere, en muchos casos, seguir con las prácticas tradicionales, perdiendo la oportunidad de aprovechar los beneficios que produce la incorporación del big data en nuestra gestión estratégica. Toda empresa que desee establecer esta cultura a nivel organizacional y encaminarse a ser una empresa analítica debe comenzar a replantearse formas de trabajo. En ese sentido, una buena práctica es mirar cómo operan al interior de sus organizaciones los grandes referentes, como Amazon, Uber Technologies Inc., Google LLC o Netflix Inc., y muchas más, a fin de identificar aspectos que nos sirvan de base para aplicarlos de igual forma en nuestras propias empresas y nos dirijamos en la dirección correcta. A continuación, sugeriré algunos de esos pasos que considero relevantes para sentar las bases de una cultura analítica.

## 7.1 La cultura basada en datos debe

## comenzar desde la alta dirección Implementar cualquier cultura en una empresa implica una gestión de cambio que no se logra sin el liderazgo de la alta dirección, la cual debe impulsar a toda la organización a establecer la cultura analítica con una alta confianza en los datos. Si un líder no cree en los datos, tampoco puede transmitirle esa cultura que desea compartir al resto de la compañía.

---

<!-- Página 70 -->

Para que una persona cambie un hábito, desarrolle una competencia u oriente su acción a un tipo de comportamiento, es necesario que quien lo dice esté convencido de ello. Así como un día Mahatma Gandhi le pidió a una madre que regresara tiempo después con su hijo, a quien quería que lo exhortara a dejar de comer dulces, pues en ese primer encuentro era imposible que le dijera al niño que abandone un hábito que él mismo tenía, un líder no puede pedirle a su organización desarrollar una cultura que él no ha establecido o en la que no confía. A medida que los líderes tengan la disposición para asumir esa cultura analítica, podrán trasmitirle esa confianza en los datos y en las buenas prácticas al resto de la organización. El impulso y la confianza en los datos deben partir de la dirección hacia los demás niveles para movilizar a todo el talento humano de la empresa a implementar la cultura analítica. Hoy el número de competidores que trabaja con big data sigue aumentando. Por lo tanto, no implementar iniciativas en el manejo de datos, aun cuando las empresas se ven forzadas a hacerlo, significará quedar rezagadas y frenar el avance en todo sentido, o encontrarse en una situación de desventaja en el mercado cuando decidan aplicarlas porque sus competidores ya se habrán adelantado, tal como está sucediendo en la actualidad. Las empresas que habían comenzado su proceso de transformación digital antes de la pandemia han transitado por esta situación con menos dificultad que aquellas que no. Así, quienes han querido transformarse digitalmente en medio de la pandemia, no estando acostumbrados a ello, han enfrentado múltiples complicaciones para llevar a cabo estas iniciativas y mantenerse en el mercado en medio de esa situación, pues compiten con empresas que tienen una gran ventaja y experiencia en el uso de los datos y en el terreno digital.

## 7.2 Potenciar la confianza en los datos Una de las vallas que debemos superar y que aún está presente en muchas organizaciones es la desconfianza en el dato. Si bien ello está sustentado en la mala calidad de algunos datos y en las prácticas

---

<!-- Página 71 -->

internas para el manejo de estos, son muchas las razones que han llevado a los líderes a no creer en los datos y apelar en mayor medida a su intuición en este proceso. Esto se ha convertido en una práctica recurrente y tan arraigada que difícilmente, con solo decirle a la alta dirección que ahora sí tiene que confiar en los datos, cambiará su forma de pensar. Para incentivar el cambio de cultura en muchas empresas y sectores, se requiere generar mayor confianza en el dato. Una alternativa es apoyarse en casos de éxito, ya sea del sector en particular o de otro del que puedan adaptar una idea a su contexto, y mediante la implementación de un piloto de alcance acotado demostrar la contribución del uso de datos en comparación con los mecanismos tradicionales. El piloto es una práctica necesaria en muchos casos para que al interior de las empresas y desde la alta dirección se reconozca el valor de los datos y se suscite confianza en ellos. En la entidad de cobranza que cité en un capítulo anterior, por ejemplo, el responsable del área era un defensor de las prácticas tradicionales. Por ello, se probó un piloto en el que utilizamos un tipo de producto y un segmento de clientes, a través del cual demostramos que se podría obtener el mismo valor o más de lo que recaudaba, pero empleando menos recursos. Así, la dirección de la institución tomó la decisión de trabajar el proyecto a nivel organizacional. Usualmente, las empresas y las áreas de cobranza de diversas organizaciones tienen prácticas muy tradicionales para su cobranza de productos o servicios, y que no se atreven a cuestionar para encontrar formas más beneficiosas de realizarlas. Por otro lado, para que se gane confianza en los datos, es necesario que la organización resuelva los problemas básicos de calidad y acceso a estos. Para el efecto, las empresas deben llevar un registro riguroso de los datos por parte de sus miembros en cada área y departamento, y efectuar a nivel organizacional todos los cambios, las acciones y las implementaciones pertinentes para que cada vez sea de mayor calidad. Toda estrategia de big data, business intelligence y analytics requiere que las organizaciones promuevan interiormente la

---

<!-- Página 72 -->

disponibilidad de esa información, pues ese es el sentido de estas iniciativas: compartir la información entre los miembros de las empresas y ponerla a disposición en todos los niveles de usuarios. Permitir que se retengan o concentren los datos en un área o que únicamente las personas que recogen determinada información tengan acceso a esta es una situación desfavorable para las empresas, lo cual, lamentablemente, se presenta con frecuencia en muchas de nuestras empresas.

## 7.3 Impulsar los equipos

## multifuncionales En la experiencia, en diversas organizaciones, encontramos frecuentemente mucho divorcio entre los equipos de tecnología o gestión de información y los usuarios de las áreas funcionales. Esto conlleva que, cuando se abordan los proyectos basados en datos, se les da la total o mayor preponderancia a los primeros, quienes, si bien son muy conocedores de las tecnologías, tienen una óptica estratégica distinta de quienes toman las decisiones. Las iniciativas de big data demandan esfuerzos cohesionados de ambos equipos. Como advertimos anteriormente en la estrategia de datos, las preguntas clave son planteadas a modo de retos por los diversos usuarios de las áreas funcionales de la organización, quienes ahora con la competencia analítica desarrollada identifican las oportunidades potenciales de uso de datos para la generación de valor y conocen todo el proceso para generarlo. Sin embargo, es el equipo del Área de Tecnología que, además de aportar con su experiencia y conocimiento para el establecimiento y soporte de la infraestructura tecnológica necesaria, realizará el trabajo analítico para proporcionar los resultados esperados con los datos. Todo esto teniendo ahora al CDO como el gran articulador de los esfuerzos basados en datos en la organización. Hace algunos años, estuvimos trabajando en un proyecto de planificación de iniciativas de business intelligence y analytics en una entidad de Gobierno. En la etapa de relevamiento inicial,

---

<!-- Página 73 -->

identificamos, entre otras cosas, que los usuarios de las distintas áreas no solo no se compartían datos entre ellos, sino que no les interesaba hacerlo. En este escenario, no podríamos ni siquiera hablar de la posibilidad de implementar una base centralizada de datos, pues cada uno seguiría defendiendo sus fuentes particulares. Necesitamos establecer esa cultura analítica que destacamos anteriormente, y eso predispone a que seamos capaces de avanzar hacia logros unificados y no logros independientes. El mundo de hoy lo demanda más que nunca. En suma, es necesario que los líderes potencien iniciativas con esfuerzos cohesionados de los distintos equipos y se encarguen de limar posibles asperezas que existan. Una buena práctica es incorporar progresivamente las metodologías ágiles en las iniciativas que se emprenderán, puesto que precisamente buscan la participación constante de todos los involucrados en un proyecto, donde cada uno aporta con lo suyo, pero con un objetivo común.

## 7.4 Garantizar el acceso a los datos Barry Beracha, a quien cito en el epígrafe de este capítulo, mantuvo en su escritorio esa frase durante todo el tiempo que fue el CEO de la empresa Sara Lee Bakery Group, con el fin de impulsar a toda la empresa a usar recurrentemente los datos, a sustentar y basar en estos su gestión y su toma de decisiones; en suma, a establecer una cultura analítica. Uno de los aspectos que guarda en sí esta cultura es un cambio en la forma en que se manejan los datos y, por lo tanto, la adopción de un nuevo hábito en cuanto a su tratamiento y la predisposición a compartir la información entre las distintas áreas de las empresas y sus diversos usuarios. Con este tipo de impulso, las organizaciones dejarán de apoyarse en hojas de cálculo libres y en el uso aislado de los datos para manejar la información de una manera más cohesionada. De ese modo, el big data les permite a las organizaciones guardar y consolidar en una base de información centralizada una variedad de datos que se genera en una multiplicidad de fuentes y que es

---

<!-- Página 74 -->

importante para que cualquier miembro pueda acceder y obtenga información en el momento que lo requiera. En consecuencia, no se pueden seguir reproduciendo las malas prácticas en el manejo del dato que se han repetido en las organizaciones de forma habitual y que son contraproducentes para el flujo de la información, como la retención de esta en un área de la empresa o el desinterés de sus miembros por compartir sus datos con otro departamento distinto. En un escenario de transformación digital, es necesario compartir la información y superar todos estos aspectos si queremos trasladar la idea de la cultura analítica a una práctica organizacional. Se trata de que todos los miembros de una empresa compartan la misma base de información, pero que cada uno, de acuerdo con su ámbito de responsabilidad, tenga acceso a más o menos información. Solo así vamos a garantizar una mayor fluidez en el manejo de la información y brindar respuestas rápidas a las diferentes situaciones que debemos afrontar, y ahora con mayor evidencia.

## 7.5 Brindar formación especializada Las iniciativas basadas en datos como big data requieren conocimientos y capacidades distintas, por lo cual debemos propiciar que se realicen capacitaciones a todo nivel en la organización. Para ello, es necesario elaborar un plan formativo en el que se establezcan características diferenciadas de acuerdo con cada grupo identificado en la organización, y así plantear capacitaciones idóneas en cada caso. En primer lugar, siempre se requiere brindar un primer tipo de capacitación para todos en el que se resalten las características de una organización basada en datos y los beneficios que aportará a todo nivel en la empresa. En segundo lugar, se deberán establecer niveles de capacitación según las características de los grupos de trabajo, a los líderes con un enfoque más estratégico, a los usuarios analistas de las áreas funcionales con un enfoque metodológico y práctico sin llegar a temas muy técnicos, y por supuesto a los equipos de tecnología con todas las bondades del manejo de bases de datos, técnicas estadísticas matemáticas y gobierno de datos.

---

<!-- Página 75 -->

Sin embargo, hemos visto en varias ocasiones que por “ganar tiempo”, por “comodidad” u otras razones generalizan las capacitaciones a la vez y a todos por igual. Además, y dado que no todos los proyectos se llevarán a cabo a la vez, es mejor desarrollar las capacitaciones en el momento correcto a cada grupo de trabajo y de acuerdo con el plan de implementaciones.

---

<!-- Página 76 -->

# Conclusiones

La finalidad del presente libro ha sido brindarles a los lectores un acercamiento a los aspectos clave que debemos impulsar para aspirar a ser organizaciones basadas en datos, donde el big data se convierta en ese gran instrumento para triunfar en esta era digital. He querido concentrarme en un mensaje no técnico dirigido a los directivos, tomadores de decisiones y usuarios funcionales en general para sensibilizarlos en los grandes soportes organizacionales que requieren estas iniciativas basadas en datos, a fin de no caer en la práctica habitual de tener esfuerzos aislados y, por el contrario, sumar ahora a nuestra gestión este uso de datos de manera decisiva, tal como lo demanda el mundo digital actual. En ese sentido, a manera de insistencia, es necesario que los usuarios de todas las áreas o departamentos de una organización posicionen a los datos en el centro de su accionar. Como hemos dicho, esto no es una tarea sencilla debido a las malas prácticas que hemos arraigado, donde las hojas de cálculo y las islas de información son las grandes protagonistas. Por ello, capacitemos, formemos, especialicemos a nuestros equipos de trabajo. Para lograrlo, es particularmente importante que los líderes impulsen este gran cambio hacia una organización basada en datos, quienes pueden promoverlo con el ejemplo, incorporando nuevos hábitos y creando las expectativas necesarias sobre lo que significa la generación de valor a partir de un uso inteligente de datos. Finalmente, cabe resaltar el importante papel de la tecnología en el soporte de toda estrategia de datos. Sin embargo, antes de pensar en cualquier plataforma tecnológica, es fundamental definir lo que podemos realizar con los datos para contribuir con una mayor

---

<!-- Página 77 -->

generación de valor e impulsarnos a una organización centrada en los datos, lo cual, por supuesto, no se logrará solo adquiriendo tecnología. La ecuación es, primero, la estrategia y, luego, la tecnología.

---

<!-- Página 78 -->

# Bibliografía

Amazon Web Services. (2019). La importancia de los datos en las transformaciones digitales actuales. Recuperado de https://es.scribd.com/document/477075040/La-importancia- de-los-datos-en-las-transformaciones-digitales-actuales-pdf [Consulta: 1 de julio de 2021].

Cukier, K. & Mayer, V. (2013). Big data. La revolución de los datos masivos. Madrid: Turner.

Davenport, T. & Harris, J. G. (2017). Competing on analytics. Boston: Harvard Business School Press.

El futuro es apasionante de Vodafane. (20 de marzo de 2016). Probadores inteligentes para hacer la experiencia de compra más interactiva [Archivo de video]. Recuperado de https://www.youtube.com/watch?v=_l0pJdQOsZA [Consulta: 1 de julio de 2021].

Goberna América Latina. (2017). Manual sobre utilidades del big data para bienes públicos. Recuperado de https://goberna.org/publicaciones/manual-utilidades-del-big- data-bienes-publicos/ [Consulta: 1 de julio de 2021].

González, I. (2017). Big data para CEO y directores de marketing. Madrid: Independently Published.

Harvard Business Review Press. (2018). Data Analytics Basics for Managers. Boston: Autor.

La receta para convertir big data en dinero. (1 de julio de 2016).

---

<!-- Página 79 -->

Forbes. Recuperado de https://www.forbes.com.mx/la-receta- para-convertir-big-data-en-dinero/ [Consulta: 20 de diciembre de 2021].

Marr, B. (2017). Big data en la práctica. Barcelona: Teell.

Marr, B. (2018). Data Strategy. Barcelona: Teell.

McAfee, A. & Brynjolfsson, E. (2012). Big data: The Management Revolution. Harvard Business Review, 1-9.

a Medina, E. (2012). Business Intelligence: una guía práctica (2.ed.). Lima: UPC, Fondo Editorial.

Rodríguez, J. R. (2016). ¿Cómo son las empresas orientadas a los datos? Harvard Deusto Business Review, (256), 46-54.

Rodríguez, P., Palomino, N. & Mondaca, J. (2017). El uso de datos masivos y sus técnicas analíticas para el diseño e implementación de políticas públicas en Latinoamérica y el Caribe. Banco Interamericano de Desarrollo (BID).

---

<!-- Página 80 -->

# Anexo.

# Casos de éxito globales

# de big data

Si bien he acompañado los capítulos del libro con algunos casos y situaciones de aprovechamiento de los datos, a fin de aportar algunas buenas prácticas para establecernos como empresas basadas en datos, revisaremos a continuación ciertos casos emblemáticos en los que he querido apoyarme para desarrollar algunas ideas finales del uso del big data. Por un lado, estas podrían despertar ideas adicionales de aplicación de datos en nuestras propias organizaciones; por otro lado, podrían resaltar la importancia de que no se trata de aplicar los datos sin un horizonte claro de su aprovechamiento, sino que debemos identificar algún punto de dolor o problema que nos lleve a una solución para superarlo y generarnos muchos beneficios. Por lo tanto, en los siguientes casos, destacaré el problema que tenían, cómo usan el big data y los beneficios que se han generado.

## 1 Caso Airbnb Este caso representa un hito importante en nuestra historia debido a que se puso en práctica un modelo que contrasta con el sistema habitual de alojamientos en hoteles. Airbnb ha experimentado un crecimiento sostenido desde su lanzamiento en 2008. Es una de las

---

<!-- Página 81 -->

aplicaciones más utilizadas a nivel mundial para reservar un alojamiento en una ciudad que, dada la gran oferta generada a lo largo de los años y los distintos intereses de los usuarios, debe contar con un mecanismo idóneo para este proceso. Así, la plataforma emplea big data para guiar la recomendación.

## 1.1 Problema

Conectar adecuadamente a una gran cantidad de huéspedes a quienes ofrecen sus alojamientos. Para lograrlo, es necesario conocer las preferencias de cada uno, a fin de contar con la propiedad idónea en el lugar correcto y a un precio justo.

## 1.2 Uso de big data No solo es importante conocer qué alojamiento eligió un cliente, sino también los pasos que siguió para optar por uno u otro. Esto representa un gran aprendizaje para las medidas que adoptará la empresa con relación al producto en sí, la priorización de recursos e, inclusive, la fijación de un precio apropiado. Es decir, lejos de tomar decisiones basándose en la intuición, se apoya en datos que recoge de los mismos clientes para obtener un mayor éxito. Los algoritmos de la empresa consideran una serie de datos como la secuencia realizada por cada usuario para la elección final, la ubicación geográfica del alojamiento, época del año, tipo de alojamiento, etcétera. Todo ello está pensado para recrear lo que le gusta y no le gusta a cada persona en el proceso realizado para su elección, lo que representa un gran valor al momento de personalizar la propuesta. Una empresa basada en datos está renovando estrategias a partir de las diversas formas de usarlos ante nuevas oportunidades que identifica o situaciones adversas que debe superar; por ejemplo, durante la pandemia, este sector atravesó serios problemas y quienes no pudieron reponerse hoy son historia. En Airbnb también se sintieron las repercusiones; pero, cuando comenzaron a retomarse los viajes, tuvieron que identificar la necesidad del mercado, lo que

---

<!-- Página 82 -->

conllevó ajustar su algoritmo de recomendación para sugerir viajes más seguros hacia lugares con naturaleza y alejados de las grandes ciudades. Asimismo, cobra mucho sentido el sonado proyecto de construcción de sus propios alojamientos, dado que conocen los lugares y tipos de alojamientos de mayor preferencia. Se trata de identificar siempre las oportunidades que te brindan los datos para impulsar acciones que permitan la generación de valor en la empresa.

## 1.3 Beneficios

La evolución que ha tenido este tipo de empresa desde su lanzamiento global en 2008 ha sido impresionante. Hoy se estima que representa un 20% del alquiler vacacional y que, si bien la pandemia le generó un tropiezo en su historia (sus reservas cayeron en un 40%), ha sabido reponerse notablemente. Según Statista, esta empresa obtuvo como resultado, en 2022, un 20% del incremento de reservas en comparación con 2019, y el valor bruto de estas reservas equivale a un 66% más. Indudablemente, las decisiones basadas en datos que toma la organización le significan grandes beneficios.

## 2 Caso Casino Caesars Durante muchos años, estuve compartiendo en mis cursos de gestión estratégica de datos el famoso caso de la cadena de casinos Harrah’s, por su poderosa estrategia centrada en el cliente y un uso explosivo de datos que le permitió ser un referente en el sector y obtener beneficios notables. Luego, esta empresa asumió a Caesars Entertainment y continuó con su estrategia centrada en los datos. Su programa de lealtad tiene como objetivo impulsar estrategias de marketing personalizadas para cada cliente a partir de los datos como grandes aliados para generar conocimiento de cada uno y de modelos predictivos para compensar adecuadamente sus niveles de gasto.

---

<!-- Página 83 -->

## 2.1 Problema Establecer un programa de lealtad conlleva conocer muy bien a tus clientes y, para hacerlo, necesitamos la mayor cantidad de datos que podamos recoger de cada uno. Por ello, era clave conocer datos generados en el negocio, como preferencias de juego, gastos, horarios, locales, respuestas a acciones de marketing, etcétera, y también datos adicionales como el porcentaje de presupuesto para juego que estaban gastando en el negocio, y seguir aprendiendo con cada nueva visita.

## 2.2 Uso de big data Al apoyarse en big data, el programa reúne la mayor cantidad posible de datos de los clientes, a fin de establecer un plan de recompensas asociado al nivel de gasto de cada uno. Esto significa que, a mayor gasto en el casino, mayor será la recompensa. Este tema fue manejado de una manera ejemplar: al saber que muchos de sus clientes tenían aún buena parte de su presupuesto para gastarlo en la empresa, propiciaban con sus acciones de marketing que puedan elevar su nivel de consumo. Detrás de esto se escondía una estrategia aspiracional muy bien sustentada que le fue generando mucho éxito no solo al casino, sino al grupo en general. Dado que se monitorea a los clientes en tiempo real, las recompensas podían ser una comida de cortesía, noches de estadía gratuita en los hoteles Caesars o tarifas aéreas pagadas como premio consuelo a un cliente al que no le fue bien en el juego.

## 2.3 Beneficios

A pesar de algunas situaciones difíciles que la empresa afrontó, el programa Total Rewards ha sido muy exitoso: hace algunos años fue valorizado en 1,08 mil millones de dólares. Esto permite resaltar la importancia de los datos que se ha consolidado a través de los años, cuyo foco es establecer relaciones de largo aliento con los clientes, quienes, en la medida que las acciones de marketing producidas por

---

<!-- Página 84 -->

el programa estén alineadas a cada uno, continuarán manteniendo su lealtad.

## 3 Caso Uber

Este es uno de los casos más emblemáticos por la característica del negocio del que muchos somos usuarios, dado que impuso una nueva forma de llevar adelante un servicio tan clásico como el taxi. Si bien cuando comenzamos a utilizar el servicio pareció novedoso, hoy ya afianzado y con diversos competidores disfrutamos del nuevo modelo, pero no notamos cómo está operando en su interior para poder ofrecer su servicio tal como lo conocemos. La respuesta radica en los datos, pues la empresa no solo debe brindarnos una unidad de taxi en forma rápida, sino que además con mucha eficiencia.

## 3.1 Problema Cada vez que se utiliza este servicio, la aplicación tarda unos segundos en asignar un conductor. Existen excepciones por demanda u horas pico; pero, al margen de esto, se debe resolver en poco tiempo la situación del tráfico o la duración del servicio, a fin de determinar el precio.

## 3.2 Uso de big data Es indudable la necesidad de contar con la mayor cantidad de datos para conseguir este modelo de negocio. Uber posee datos constantes que le permiten visualizar con claridad la red de transporte público en las ciudades donde tiene presencia, gracias a lo cual organiza la disponibilidad de unidades, con mayor incidencia en las zonas donde el servicio público llegue menos. Es una empresa que recoge datos en todo momento, incluso cuando los conductores no están en servicio, dado que es importante conocer la velocidad, localización u otros datos. Por supuesto, cuando están con pasajeros, usan navegadores GPS para su desplazamiento. Todo esto hay que imaginarlo en una operación que

---

<!-- Página 85 -->

tiene más de 15 millones de viajes diarios en más de 10 000 ciudades en los países donde opera.

## 3.3 Beneficios Como muchos de los sectores, Uber también experimentó resultados negativos durante la pandemia, pero la recuperación ha sido notable. En el último trimestre de 2022, aumentó sus ingresos en un 49% respecto al mismo periodo de 2021. Alcanzó un nuevo récord en la cantidad de viajes realizados en un trimestre: 2000 millones alrededor del mundo, según el propio CEO de la empresa Dara Khosrowshahi; es decir, un promedio de alrededor de un millón de viajes cada hora. Sus ganancias representaron un 82% más que el año anterior. Definitivamente, debemos destacar que una empresa basada en datos genera mucho valor y se consolida en el tiempo a partir de nuevas formas de aprovecharlos. En este caso, si bien hemos resaltado el negocio de la movilidad de Uber, otro tanto lo representa su negocio de las entregas.

## Reflexión final Mientras termino de escribir este libro, se escucha con mucha fuerza nuevamente el tema de la inteligencia artificial debido al reciente lanzamiento del ChatGPT. Este es un chatbot de la empresa OpenAI, perteneciente a Microsoft, que brinda al usuario respuestas escritas a sus inquietudes, lo que para muchos significa un gran avance, pero para otros implica un peligro mayor para la humanidad por los usos inadecuados que se le puede dar. En cualquier caso, seguimos observando un escenario donde en nuestro día a día tendremos asistentes más poderosos para brindarnos toda la información que podamos requerir. Esto es una muestra más del nuevo escenario que debemos aceptar y, por supuesto, aprovechar para nuestras propias organizaciones. No se trata simplemente de comentar las bondades de estos avances, sino de tomar ideas para aplicarlas en nuestro contexto y así generar

---

<!-- Página 86 -->

muchos beneficios. Por lo tanto, es evidente hacia dónde debemos dirigir nuestras organizaciones, a fin de diferenciarnos en un mercado cada vez más competitivo. Las transformaciones digitales se seguirán acentuando en nuestros países, y con esto la necesidad de proyectarnos a ser empresas basadas en datos. Es aquí donde tenemos que unir las piezas que propone el mundo de hoy para ser más exitosos, adecuar nuestros modelos de negocio a las necesidades de un cliente/ciudadano influenciado por la evolución de la tecnología digital, con mucha creatividad e innovación para advertir estos cambios al interior de nuestra empresa. Asimismo, en su justa medida, se debe incorporar la tecnología que se adecúe a nuestras necesidades (las tecnologías emergentes no serán de utilidad para todos) y, en este contexto, incluir con mucha astucia los datos para propiciarnos mucho valor, como los casos que hemos citado a lo largo del libro. Seamos partícipes del cambio, salgamos a abrazarlo y adoptémoslo antes que la competencia; solo así podremos estar siempre a la vanguardia.

## Bibliografía

Business Intelligence Marketing. (5 de setiembre de 2022). Así es como Airbnb ha utilizado el biga data. Recuperado de https://www.bimarketingsas.com/2022/09/05/asi-es-como- airbnb-ha-utilizado-el-big-data/ [Consulta: 2 de mayo de 2023].

Expansión. (8 de febrero de 2023). Uber tiene el “trimestre más fuerte” de su historia. Recuperado de https://expansion.mx/tecnologia/2023/02/08/uber-tiene-el- trimestre-mas-fuerte-de-su-historia [Consulta: 2 de mayo de 2023].

FourWeekMBA. (s. f.). Estadísticas de Airbnb. Recuperado de https://fourweekmba.com/es/airbnb-statistics/ [Consulta: 2 de mayo de 2023].

---

<!-- Página 87 -->

Hosteltur. (24 de marzo de 2023). Airbnb supera las cifras prepandemia a lo grande. Recuperado de https://www.hosteltur.com/156656_airbnb-supera-las-cifras- prepandemia-a-lo-grande.html [Consulta: 2 de mayo de 2023].

Marr, B. (18 de mayo de 2015). Big Data At Caesars Entertainment - A One Billion Dollar Asset? Recuperado de https://www.forbes.com/sites/bernardmarr/2015/05/18/when- big-data-becomes-your-most-valuable-asset/ [Consulta: 2 de mayo de 2023].

MixTrategy. (s. f.). Uber y big data. Recuperado de https://www.mixtrategy.com/uber-y-bigdata/ [Consulta: 2 de mayo de 2023].

ReasonWhy. (8 de febrero de 2019). Uber en datos: el secreto del éxito de las VTC. Recuperado de https://www.reasonwhy.es/actualidad/uber-datos-secreto-exito- vtc [Consulta: 2 de mayo de 2023].

---

<!-- Página 88 -->

## Recientes publicaciones de la Editorial

## UPC

2023

Mariana Gálvez Vásquez Santos, huacas y otras yerbas Víctor Rodríguez Cedeño, Milagros Betancourt Catalá y María Isabel Torres Cazorla Diccionario de Derecho Internacional Lydia Fossa Khipu. Instrumento de gestión, memoria y poder Pablo C. Herrera, Rodrigo Scheeren y David M. Sperling Homo Faber 3.0. Appropriations of Digital Fabrication from Latin America 2022

2022

Iván Villanueva-Jordán, John Jairo Giraldo-Ortiz y Paula Andrea Montoya-Arango (eds.) II Coloquio Internacional de Jóvenes Investigadores en Traducción e Interpretación UdeA-UPC Pablo C. Herrera, Cristina Dreifuss Serrano, Paula Gómez Z. y Luisa Fernanda Arris Calderón (eds.) SIGraDi 2022. Critical Appropriations María José Castro Bernardini y Bruno Rivas Frías Campeonas. Cambiando las reglas del juego Joel Gallardo Bravo Diseño de grandes almacenes. Claves para un layout exitoso Editorial UPC Club de Lectura UPC. Una selección de reseñas literarias 2022-2

---

<!-- Página 89 -->

Luis Andrade Ciudad, Raquel de Pedro Ricoy y Rosaleen Howard Traducir derechos, traducir culturas. Entre el castellano y las lenguas originarias del Perú Vidal Guerrero Támara El dios del rayo. De hirka Llamoq a san Pedro de Huancarpata Jorge Alberto Balerdi Arrarte y Eugenio Giacchetti Lobatón Reciclajes arquitectónicos. Arquitectura limeña doméstica transformada Leonardo Ysla Heredia María Jesús Alvarado. Retrato de una intelectual y activista peruana Manuel Eráusquin Oblitas, César Pita Dueñas y Oscar Sánchez Benavides (eds.) Pídelo con respeto. Medio siglo con El padrino Jeremy Munday Introducción a la traductología. Teorías y aplicaciones Víctor Rodríguez Cedeño y Thairi Moya Sánchez Glosario de justicia internacional penal Editorial UPC Club de Lectura UPC. Una selección de reseñas literarias 2022-1

Luis Alexander Pacora Cabrera y Enrique Blanc Rojas Sabor peruano. Travesías musicales Enrique Ciriani Ciriani. 11 años del Taller de Diseño Avanzado

Junior Pichón De La Cruz Faltas disciplinarias en el servicio civil peruano. Compendio de criterios jurisprudenciales

2021

---

<!-- Página 90 -->

Angélica Brañez Medina Moda y tradición. El vestido del pueblo limeño en el siglo     republicano John Jairo Giraldo-Ortiz, Iván Villanueva-Jordán y Paula Andrea Montoya-Arango (eds.) I Coloquio Internacional de Jóvenes Investigadores en Traducción e Interpretación UdeA-UPC Michele Albanelli Espacios de aprendizaje. Reflexiones sobre la relación entre el diseño, la arquitectura y la pedagogía Mayté Ciriaco Ruiz Niñas sin infancia. La normalización del abuso en la selva peruana Gerardo Karbaum Padilla La evolución de la narrativa audiovisual. Analógica, transmedia y social media Elizabeth Cárdenas Arroyo, Liliana Checa Yábar, Marissa Consiglieri de Chackal y Cristina Dreifuss Serrano Bocadillos de arte. Alimentando el alma, la mente y los sentidos

David Reyes Zamora Reto bicentenario. Una mirada a las fracturas que limitan el desarrollo del Perú tras la pandemia Pedro Cateriano (comp.) 25 peruanos del siglo   

Jorge Alberto Balerdi Arrarte Restaurantes limeños del boom gastronómico. Arquitectura e identidad Emiliano Brancaccio y Samuele Bibi Anti-Blanchard. Un enfoque comparativo para el estudio de la macroeconomía

Piero Che Piu Palao

---

<!-- Página 91 -->

Leer con binoculares. Crea contenido significativo que las personas disfruten

Encuentra más publicaciones de la Editorial UPC en versión impresa y digital ingresando a editorial.upc.edu.pe

Visita la página de Facebook de la Editorial UPC www.facebook.com/editorialupc

---

<!-- Página 92 -->

1 Firma privada número uno de servicios profesionales del mundo. 2 Portal de estadística en línea. 3 Empresa multinacional de consultoría estratégica, servicios tecnológicos y externalización. 4 Empresa multinacional fabricante de software de inteligencia empresarial. 5 Académico y autor estadounidense especializado en gestión del conocimiento e inteligencia artificial.

---

<!-- Página 93 -->

This file was downloaded from Z-Library project

Your gateway to knowledge and culture. Accessible for everyone.

z-library.sk z-lib.gs z-lib.fm go-to-library.sk

Official Telegram channel

Z-Access

https://wikipedia.org/wiki/Z-Library