<!-- Página 1 -->

¿QUÉ SABEMOS DE?

# Big data

# Conceptos, tecnologías

# y aplicaciones

## David Ríos Insua y

## David Gómez-Ullate Oteiza

---

<!-- Página 2 -->

---

<!-- Página 3 -->

# Big data

Conceptos, tecnologías y aplicaciones

David Ríos Insua David Gómez-Ullate Oteiza

---

<!-- Página 4 -->

Colección ¿Qué sabemos de?

COMITÉ EDITORIALCOnsEJO AsEsOR

PILAR TIgERAs sánChEz, DIRECTORAJOsÉ RAMón uRquIJO gOITIAROsInA LóPEz-ALOnsO FAnDIñO CARMEn guERRERO MARTínEz, sECRETARIAAvELInO CORMA CAnósMARíA vICTORIA MOREnO ARRIBAs RAMón RODRíguEz MARTínEzgInÉs MORATA PÉREzDAvID MARTín DE DIEgO JOsE MAnuEL PRIETO BERnABÉLuIs CALvO CALvOsusAnA MARCOs CELEsTInO ARAnTzA C hIvITE vázquEzMIguEL FERRER BAEnACARLOs PEDRós ALIó JAvIER sEnÉn gARCíAEDuARDO PARDO DE guEvARA y vALDÉsMATILDE BARón AyALA CARMEn vIAMOnTE TORTAJADAvíCTOR MAnuEL ORERA CLEMEnTEPILAR hERRERO FERnánDEz MAnuEL DE LEón RODRíguEzPILAR LóPEz sAnChOMIguEL ángEL P uIg-sAMPER M uLERO IsABEL vARELA nIETOPILAR gOyA LAzAJAIME PÉREz DEL vAL ALBERTO CAsAs gOnzáLEzELEnA CAsTRO MARTínEz

CATáLOgO gEnERAL DE PuBLICACIOnEs OFICIALEs hTTP://PuBLICACIOnEsOFICIALEs .BOE.Es

Diseño gráfico de cubierta: Carlos Del Giudice

© David Ríos Insua y David Gómez-Ullate Oteiza, 2019 © CSIC, 2019 http://editorial.csic.es publ@csic.es © Los Libros de la Catarata, 2019 Fuencarral, 70 28004 Madrid Tel. 91 532 20 77 www.catarata.org

IsBn (CsIC): 978-84-00-10534-1 IsBn ELECTRónICO (CsIC): 978-84-00-10535-8 IsBn (CATARATA): 978-84-9097-842-9 IsBn ELECTRónICO (CATARATA): 978-84-9097-843-6 nIPO: 694-19-069-4 nIPO ELECTRónICO: 694-19-070-7 DEPósITO LEgAL: M-31.093-2019 IBIC: PDz/PDR

REsERvADOs TODOs LOs DEREChOs POR LA LEgIsLACIón En MATERIA DE PROPIEDAD InTELECTuAL. nI LA TOTALIDAD nI PARTE DE EsTE LIBRO, InCLuIDO EL DIsEñO DE LA CuBIERTA, PuEDE REPRODuCIRsE, ALMACEnARsE O TRAnsMITIRsE En MAnERA ALgunA POR MEDIO yA sEA ELECTRónICO, quíMICO, óPTICO, InFORMáTICO, DE gRABACIón O DE FOTOCOPIA, sIn PERMIsO PREvIO POR EsCRITO DEL COnsEJO suPERIOR DE I nvEsTIgA- CIOnEs CIEnTíFICAs y LOs LIBROs DE LA CATARATA. LAs nOTICIAs , LOs AsERTOs y LAs OPInIOnEs COnTEnIDOs En EsTA OBRA sOn DE LA ExCLusIvA REsPOnsABILIDAD DEL AuTOR O AuTOREs. EL COnsEJO suPERIOR DE InvEsTIgACIOnEs CIEnTíFICAs y LOs LIBROs DE LA CATARATA, POR su PARTE, sOLO sE hACEn REsPOnsABLEs DEL InTERÉs CIEnTíFICO DE sus PuBLICACIOnEs .

---

<!-- Página 5 -->

A Susa y mis surfeiras favoritas, Isa y Carla David Ríos

A Neeltje, June y Emma, siempre por alegrías David Gómez-Ullate

---

<!-- Página 6 -->

---

<!-- Página 7 -->

## Índice

AGRADECIMIENTOS 9

PRÓLOGO 11

CAPÍTULO 1. Frente al mar de datos 15

CAPÍTULO 2. Tecnologías del big data 24

CAPÍTULO 3. Métodos estadísticos y de aprendizaje automático para el tratamiento de big data 39

CAPÍTULO 4. Big data para la política y la Administración 58

CAPÍTULO 5. Big data en sanidad 69

CAPÍTULO 6. Big data y ciberseguridad 89

CAPÍTULO 7. La otra cara del big data 104

CAPÍTULO 8. A modo de conclusión 125

BIBLIOGRAFÍA 129

---

<!-- Página 8 -->

---

<!-- Página 9 -->

## Agradecimientos

Sean nuestras primeras palabras de agradecimiento al CSIC por darnos esta oportunidad de continuar nuestra colabora- ción en este campo, explicando nuestra visión sobre cómo navegar en el proceloso océano de los datos. Un agradecimiento especial a nuestro director, Manuel de León, que prácticamente de la nada pilotó el ICMAT, de ser un instituto bebé hasta ser un centro principal en investi- gación en ciencias matemáticas. En la mar cambian las co- rrientes, pero siempre se vuelve al equilibrio natural. En ICMAT damos también gracias especiales a la ener- gía que aportan nuestros compañeros del SPOR DataLab y al apoyo de nuestro equipo de gestión. El trabajo de David Ríos está financiado por los progra- mas MTM2017-86875-C3-1-R MTM2015-72907-EXP del Ministerio de Economía e Innovación de España y la Cátedra AXA-ICMAT sobre Análisis de Riesgos Adversarios del AXA Research Fund. Este trabajo también ha sido en parte financiado a través del Programa H2020 de Investigación, Desarrollo Tecnológico y Demostración de la Unión Europea, bajo el acuer- do nº 740920 (CYBECO). Se agradece también la ayuda de la FGCSIC para realizar las actividades de la precitada Cátedra. El trabajo de David Gómez-Ullate está financiado por los proyectos MTM2015-65888-C4-3 y MTM2015-72907-EXP

9

---

<!-- Página 10 -->

del Ministerio de Economía e Innovación de España. El autor agradece especialmente a la Fundación BBVA que, a través de su beca Leonardo, apoyó su primer proyecto de investi - gación en inteligencia artificial. Agradece también la ayuda de sus compañeros en el UCA Datalab y al Vicerrectorado de Transferencia de la Universidad de Cádiz por su confianza en la labor realizada y su apoyo a la investigación en ciencia de datos.

10

---

<!-- Página 11 -->

## Prólogo

En estos últimos años hemos sido testigos del rápido creci- miento en la capacidad de las empresas y las administracio- nes públicas para explotar los avances recientes en las tec- nologías de la información y de las comunicaciones (TIC), de la investigación operativa y de la modelización estadísti- ca, para recopilar y procesar datos sociales y de mercado, de sensores y de operaciones, para apoyar sus procesos de to- ma de decisiones. La captura de datos a través de aplicacio- nes online y móviles produce cantidades ingentes de infor- mación potencial que debemos aprehender para entender cómo actuamos, nos sentimos, nos movemos e interactua- mos y cómo respondemos frente a las políticas de los go- biernos y las decisiones de las empresas. Los datos alcanzan así cada vez mayor valor para las organizaciones que inten- tan vislumbrar cómo aprovecharlos para mejorar las relacio- nes con los ciudadanos o los clientes, personalizar servicios y productos y automatizar todo tipo de procesos. Hasta hace poco, la toma de decisiones y el diseño de políticas en mu- chos ámbitos se hacía según criterios basados en informa- ción cualitativa, cuando no directamente según impresiones subjetivas. La irrupción del big data está implicando que, cada vez más, la información proporcionada por los datos constituya la base del análisis y las decisiones, posibilitando

11

---

<!-- Página 12 -->

procesos más objetivos y automáticos, con las ventajas y riesgos que ello supone. En cierta forma, existe algo de exageración sobre el fe- nómeno que hoy se conoce como big data, motivado en parte por éxitos indudables en aplicaciones industriales como los coches autónomos, la traducción automática o el reconoci- miento del habla. Esta exageración se refleja en titulares como “El diluvio de datos vuelve obsoleto el método científico” (Wired, 2008) o “el big data salvará la política” (Technology Review, 2013) y ha llevado a cierta confusión en empresas y administraciones al querer realizar proyectos big data per se, cuando realmente no los necesitan, y en confundir big data con una mera tecnología, típicamente asociada con Hadoop o Spark. En este libro introducimos los conceptos, tecnologías y metodologías básicas del big data y describimos algunas apli- caciones actuales y potenciales para contribuir a un mejor desarrollo de la sociedad. Intentamos desmontar algunas ideas equivocadas y promover una concepción más global de este fenómeno orientada a la obtención de valor de los datos a través de un uso responsable de la tecnología y la ciencia dirigido a apoyar la toma de decisiones basada en evidencia. Tras una introducción al fenómeno del big data, identi- ficando los pilares estadístico-matemático, informático-tec- nológico y aplicado que deben sostener este tipo de proyec- tos, hacemos una breve incursión en sus tecnologías principales, con la obvia advertencia de la rápida evolución de las mismas. Revisamos, después, el otro pilar fundamental re- ferido a los métodos estadísticos y de aprendizaje automático dentro del paradigma de la ciencia de datos. Los siguientes tres capítulos se refieren a aplicaciones en campos de interés principal como son su uso para la promoción de políticas pú- blicas, en lo que denominaríamos “analítica de políticas”, y en la comunicación política, en particular en referencia al fenómeno de las fake news; su empleo en la promoción de la salud, y, en tercer lugar, en su adopción para el desarrollo de sociedades más ciberseguras. Finalmente, hacemos una

12

---

<!-- Página 13 -->

referencia a los aspectos éticos y de responsabilidad social del tratamiento de los big data, para concluir con una mirada al futuro. Cada capítulo se completa con una breve reseña bi- bliográfica con la que el lector podrá ampliar los contenidos. Comienza la singladura.

DaviD Ríos insua y DaviD Gómez-ullate oteiza Pantín-El Puerto de Santa María

13

---

<!-- Página 14 -->

---

<!-- Página 15 -->

CAPÍTULO 1

## Frente al mar de datos

Introducción

Las últimas décadas han visto un rápido crecimiento en la capacidad de las empresas para explotar los numerosos avances recientes en las TIC, en la investigación operativa (IO) y la modelización estadística, de cara a recopilar y pro- cesar datos de mercado y de operaciones para apoyar sus procesos de toma de decisiones. Como resultado, la analítica de negocios (business analytics) se ha convertido en un cam- po floreciente para la consultoría y la formación empresa- rial. Sin embargo, aunque muchas decisiones de algunos gobiernos a menudo vienen apoyadas con métodos tradicio- nales del análisis de políticas públicas, incluyendo aproxi- maciones como el análisis de coste-beneficio, pocos depar- tamentos y agencias gubernamentales han logrado, por el momento, aprovechar de forma sistemática las grandes ma- sas de datos disponibles, los hoy llamados big data, y los métodos avanzados de estadística y de aprendizaje automáti- co (machine learning) para obtener evidencias que informen sus decisiones. Este hecho constituye una interesante novedad desde una perspectiva histórica, ya que los métodos cuantitativos de ayuda a la toma de decisiones han surgido frecuentemente en

15

---

<!-- Página 16 -->

el sector público. Por ejemplo, la estadística social, que se re- monta a Quetelet, se inició en el siglo XIX para apoyar a los gobiernos a partir de la idea de que las regularidades estadís- ticas proporcionan señales sobre realidades sociales. Del mis- mo modo, el campo de la investigación operativa nació du- rante la Segunda Guerra Mundial al servicio de las fuerzas armadas de los Estados Unidos de América y del Reino Unido, y creció rápidamente a partir del desarrollo de distin- tos métodos de apoyo a la toma de decisiones en problemas militares. Indudablemente, si lo comparamos con cómo se toman decisiones en el sector empresarial, los responsables de las decisiones públicas se enfrentan a tareas más complejas. Además de las dificultades propias de los problemas del sec- tor privado, los decisores públicos deben enfrentarse a cues- tiones adicionales relacionadas con el hecho de tomar decisio- nes por y para otras personas. Así, los responsables políticos se enfrentan a las cuestiones asociadas a decidir cómo se asig- nan los recursos públicos, tratándose de determinar “quién obtiene qué, cuándo y cómo”. Puesto que tales recursos son escasos, deben tomarse decisiones complejas, como en la fa- mosa disyuntiva “cañones o mantequilla”. Por otra parte, si nos centramos en el caso de los sistemas democráticos, algu- nas de las peculiaridades adicionales de la toma de decisiones en el sector público se referirían a que:

- El público y/o sus representantes toman las decisio- nes, dependiendo del grado de participación que se contemple. - Hay funcionarios públicos que, generalmente, se en- cargan de la gestión de la organización en la que debe tomarse la decisión. - En general, el público es el que financia los análisis previos a la toma de decisiones a través de sus im- puestos. - Los impactos de la toma de decisiones afectan a la sociedad en general.

16

---

<!-- Página 17 -->

- La valoración última de los resultados de una decisión es, típicamente, no solo monetaria sino que incorpora otros objetivos. - Los métodos empleados para informar sobre las deci- siones están sujetos al escrutinio público.

Otras cuestiones que diferencian las decisiones públicas frente a las privadas se refieren a la coexistencia de distintos sistemas de valores y culturas en una sociedad, y que tales decisiones pueden verse afectadas por los breves horizontes electorales de los representantes, con el consiguiente riesgo asociado a adoptar una visión demasiado cortoplacista de lo público. Nuestro objetivo en este libro es, por un lado, describir las técnicas y métodos para el análisis de big data, e ilustrar cómo pueden emplearse por parte de los gobiernos y ciuda- danos para un mejor desarrollo de la sociedad.

Analítica para negocios

Ya hemos mencionado cómo en sus orígenes las disciplinas de la estadística y de la investigación operativa provenían del apoyo de la toma de decisiones en políticas públicas. Durante la última década, el crecimiento de la potencia de cálculo y los avances en tecnologías para grandes conjuntos de datos han proporciona- do nuevas perspectivas en tales disciplinas, y en otras afines co- mo el aprendizaje automático, lo que ha llevado a una nueva visión denominada analítica (analytics), que ha demostrado ser extremadamente valiosa para ayudar a los responsables de toma de decisiones en áreas de negocios y de la industria. La analítica puede centrarse en enfoques descriptivos, pre- dictivos o prescriptivos. Típicamente apoya el descubrimiento y la presentación de patrones relevantes en problemas con gran- des conjuntos de datos registrados para cuantificar, describir, predecir y mejorar los resultados de una organización. Cuando nos referimos al entorno de negocios se denomina “analítica de

17

---

<!-- Página 18 -->

negocios”, un término popularizado en los últimos años. A menudo combina métodos de la estadística, la IO, el aprendi- zaje automático y la informática, junto con disciplinas como la sociología, la psicología y la economía. La evidencia pro- porcionada por los datos se emplea para recomendar accio- nes y guiar las decisiones y la planificación en las organiza- ciones. Sus resultados pueden emplearse como entrada a la toma de decisiones por personas; pero también pueden ali- mentar sistemas automáticos de ayuda a la toma de decisio- nes. Por contraste, el ya más tradicional concepto de inteli- gencia de negocio (business intelligence) tiende a referirse a la extracción de información, la elaboración de informes y la provisión de alertas en conexión con algún problema aplica- do de interés. En la industria, el énfasis en el área de la analítica se ha puesto en resolver problemas relacionados con el análisis de conjuntos de datos masivos y complejos, frecuentemente en entornos muy cambiantes, más allá de la evolución y el de- sarrollo de sistemas de planificación empresarial y los alma- cenes de datos convencionales. Tales conjuntos de datos suelen denominarse big data y se caracterizan por tres ras- gos típicos de los negocios que emplean sistemas transaccio- nales online:

- Grandes volúmenes de datos generados. Como ejem- plos, Walmart acumula más de 2,5 petabytes por hora de transacciones de clientes; Facebook recoge 300 mi- llones de fotos y 2,7 millones de likes por día. - Gran heterogeneidad de los datos generados, que pueden provenir de fuentes tales como mensajes de blogs, imágenes en redes sociales, correos electróni- cos, archivos PDF, datos geoespaciales, lecturas de sensores en una ciudad o señales GPS en teléfonos móviles. De hecho, hoy en día podríamos contem- plarnos cada uno de nosotros como generadores per- manentes de datos a partir de las interacciones con nuestros smartphones.

18

---

<!-- Página 19 -->

- Datos generados a gran velocidad. En muchos casos, la velocidad de generación tiende a ser más impor- tante que el volumen disponible, en el sentido de que se deben tomar decisiones, teniendo que evaluarse la información, a partir de los datos obtenidos, todo ello en tiempo real.

Así pues, disponemos de una cantidad cada vez mayor de información digitalizada proveniente de dispositivos y sen- sores cada vez más baratos. En consecuencia, nos enfrenta- mos a una nueva era en la que hay una enorme cantidad de datos digitales —el mar de datos— sobre numerosos temas de interés potencial para una empresa o un gobierno. Sin embar- go, con bastante frecuencia dicha información es altamente desestructurada y difícil de gestionar y, a veces, poco relevan- te, aportando poco valor. El análisis de estos tipos de datos no estructurados, o no muestreados, constituye un reto importante en la industria y ha dado lugar a nuevos paradigmas como la ciencia de datos y la ingeniería de datos. Los datos no estructurados difieren de los que lo son en que su formato es muy variable y no pueden al- macenarse en bases de datos relacionales tradicionales sin un esfuerzo significativo que conlleve transformaciones complejas de los mismos. Se emplean así bases de datos NoSQL (not only SQL) más escalables, siendo un ejemplo MongoDB, Cassandra o CouchDB. Gestionar tales masas de datos requiere marcos que permitan realizar cálculos paralelizables a gran escala, co- mo MapReduce y su implementación Hadoop, que facilita el procesamiento distribuido sobre conjuntos más pequeños de datos. Finalmente, necesitamos también infraestructuras de al- macenamiento que faciliten el resumen de datos y sus análisis, como Hive. Dentro de estos desarrollos tecnológicos, debería- mos mencionar Python como el actual lenguaje principal de programación con propósito numérico, así como R, para infe- rencia y predicción. Además de los avances tecnológicos, también hay nuevas clases de métodos de análisis que permiten la extracción de

19

---

<!-- Página 20 -->

información de conjuntos masivos de datos. Estos van más allá de las técnicas tradicionales, como los modelos de re- gresión, los de series temporales, basados por ejemplo en modelos dinámicos lineales o los clasificadores de k veci- nos más cercanos; llegando a métodos más recientes como los árboles de clasificación y de regresión, los conjuntos de máquinas (ensemble methods), las máquinas de soporte vectorial (support vector machines) o las redes neuronales profundas. Con frecuencia, estos requieren nuevas imple- mentaciones como en el caso de la biblioteca en R biglm para la regresión lineal en lugar del tradicional lm. Otro ejemplo es Mahout, que facilita la clasificación y el análisis de conglomerados sobre Hadoop. La mayor parte de los algoritmos más usados en aprendizaje automático están implementados en bibliotecas de código abierto en los len- guajes de programación más utilizados en ciencia de datos, como scikit-learn (python), caret (R), MLLib (Apache Spark), etc., cuyas versiones se actualizan con frecuencia para incluir nuevos desarrollos o mejoras en rendimiento. El análisis de redes sociales, con orígen en la sociología, y otros métodos analíticos de estructuración y extracción de significado, como los mapas cognitivos, también están ga- nando importancia cuando nos enfrentamos a datos prove- nientes de redes sociales. Las herramientas de inteligencia artificial (IA) para el procesamiento de lenguaje natural también están experimentando un desarrollo considerable en los últimos años. En cualquier caso, los datos parecen ahora más accesi- bles a los gestores, que tienen una gran oportunidad para to- mar mejor sus decisiones utilizándolos para aumentar sus ingresos, reducir sus costes, mejorar el diseño de sus produc- tos, detectar y prevenir el fraude o la mejora de la participa- ción de clientes a través del marketing personalizado. Esto ha conducido a un nuevo concepto de empresa que toma deci- siones basadas en la evidencia, con ejemplos claros como Google, Facebook, Amazon, Walmart y algunas de las líneas aéreas más avanzadas.

20

---

<!-- Página 21 -->

Analítica para políticas públicas

Las mismas cuestiones mencionadas en relación con la dispo- nibilidad y el posible uso de datos se están encontrando en el contexto de las políticas públicas, como por ejemplo en los casos de los ingresos hospitalarios, de los registros médicos electrónicos, de los datos meteorológicos, de la venta de pro- piedades o de los datos procedentes de cámaras de vigilancia o de posicionamiento de teléfonos móviles, entre muchas otras fuentes que pueden ser tremendamente útiles para nu- merosos departamentos gubernamentales. Además, estas fuen- tes coexisten con otras más tradicionales procedentes de sis- temas prediseñados de recopilación masiva de datos, como los censos, los documentos de recaudación de impuestos o los distintos sondeos que realizan los gobiernos. Así, podríamos pensar en aplicar la analítica para apoyar la toma de decisiones en la elaboración de políticas públicas, lo que lleva, de forma natural, al concepto de analítica para políti- cas (policy analytics). Sin embargo, cuando se realiza una bús- queda de ese término vemos que aparecen solo un par de em- presas con nombre relacionado (Policy Analytics, Public Policy Analytics) y empresas como Oracle, Booz-Allen-Hamilton o IBM que han incluido el término dentro de su cartera de activi- dades. Carnegie Mellon tiene también una sección de analytics dentro de su programa de políticas públicas. Pero, como men- cionamos en la introducción, pocas decisiones gubernamenta- les se benefician ya del aprovechamiento sistemático de grandes masas de datos y técnicas avanzadas de modelización. Por comparación con las aplicaciones industriales, no es di- fícil vislumbrar las enormes aplicaciones potenciales que tendrían en problemas como examinar la distribución de los patrones de sucesos de salud, el desarrollo racional de planes para infraes- tructuras, el empleo del conocimiento sobre comportamientos para promover la eficiencia energética, el desarrollo de servicios personalizados de gobierno, la mejora de la experiencia en visitas turísticas, la identificación de barrios con servicios sociales inade- cuados o el diseño de ciudades inteligentes, entre otros muchos.

21

---

<!-- Página 22 -->

El camino que nos espera

En este libro haremos una revisión de los conceptos, tecnolo- gías y metodologías propias del big data y una reflexión a través de ejemplos reales y potenciales sobre cómo este fenó- meno puede ayudar, y también perjudicar, en la toma de de- cisiones y políticas públicas dirigidas a mejorar nuestras so- ciedades. Así, en las siguientes páginas responderemos a preguntas como ¿por qué han empezado a ser relevantes estas disciplinas en tiempos recientes?, ¿cuáles son las principales tecnologías y metodologías empleadas en ciencia e ingeniería de datos?, ¿por qué hay un predominio, por el momento, de estas disciplinas en el sector privado?, ¿qué fuentes de datos, de origen público y privado, son relevantes en la toma de deci- siones públicas?, ¿en qué campos de aplicación en política pú- blica podríamos emplear la ciencia de datos?, ¿qué aspectos éticos y de privacidad deberíamos tener en cuenta en un pro- yecto big data aplicado al sector público?, ¿qué efectos labora- les está teniendo la automatización de tareas y la inteligencia artificial en la transformación de sectores productivos?, ¿có- mo pueden ayudar los métodos de ciencia de datos en las distintas fases del ciclo de análisis de las políticas públicas?

Figura 1 Posicionamiento interdisciplinar de la ciencia de datos según estudiamos en este libro.

MatemáticasInformática Estadística Ciencia de datos

Conocimientos específicos

22

---

<!-- Página 23 -->

El libro viene estructurado en torno a una visión de la ciencia de datos como sinergia de disciplinas de tipo estadís- tico-matemático, informático y de conocimientos específicos del campo de aplicación que nos incumba. Así, en el capítulo 2 hacemos una revisión introductoria a las tecnologías del big data. Después, presentamos de forma concisa las metodologías principales de aprendizaje automá- tico y estadística para predicción en presencia de big data. Los siguientes tres capítulos se refieren a aplicaciones especí- ficas: el capítulo 4 cubre aplicaciones en política y administra- ción públicas; después en sanidad, y, finalmente, en ciberse- guridad. Por último, concluimos discutiendo aspectos éticos y sociales del big data y presentando una mirada al futuro de aplicaciones del big data para la mejora de la sociedad.

23

---

<!-- Página 24 -->

CAPÍTULO 2

## Tecnologías del big data

Introducción

En el capítulo anterior introdujimos como tres pilares funda- mentales de los proyectos de big data los aspectos que po- dríamos denominar computacionales, que nos ayudan a re- coger, almacenar, procesar y presentar los datos pertinentes; los relativos a los aspectos analíticos, que ayudan a construir y elaborar modelos para extraer información, predecir y, eventualmente, apoyar la toma de decisiones en relación con el problema de interés; y, finalmente, los correspondientes a la materia relevante en la que se desarrollen que nos incumba, sea, por ejemplo, de epidemiología, de seguridad aérea o de gestión urbana. En este capítulo presentamos los conceptos principales de tipo tecnológico en relación con el campo del big data. En primer lugar, hacemos una breve historia de cómo ha ido evolucionando la recolección y el procesamiento de datos a través del ejemplo de la mercadotecnia. Después intentamos fijar el concepto de big data presentando algo de terminología en relación con los tamaños de los conjuntos de datos que se puedan gestionar. Sin embargo, no solo es el volumen el as- pecto que hoy define este campo con el que presentamos las denominadas “uves” del big data. Ello explicaría los distintos

24

---

<!-- Página 25 -->

tipos de tecnologías que se han desarrollado para su gestión, que revisamos brevemente. Observemos en este punto que, en primer lugar, no podemos ser exhaustivos en su presenta- ción y, en segundo, como en muchos otros aspectos de las TIC, evoluciona muy rápidamente, pudiendo quedar obsole- ta en breve tiempo. Es por ello que presentamos las grandes áreas tecnológicas para después dar algunas pinceladas sobre algunos productos relevantes hoy en día.

Del small al big data

Los datos han venido a ser designados como el petróleo de la sociedad digital. La captura de información a través de apli- caciones móviles y online produce cantidades ingentes de da- tos sobre cómo actuamos, nos sentimos, nos movemos e inte- ractuamos y cómo respondemos a políticas de nuestros gobiernos, por ejemplo, frente a nuevas normativas; y accio- nes de empresas, por ejemplo, frente a promociones de venta. Así, los datos están alcanzando cada vez mayor valor para las organizaciones que intentan vislumbrar cómo aprovecharlos para mejorar las relaciones con los ciudadanos o los consumi- dores dependiendo del contexto de la aplicación, personalizar servicios y productos y automatizar todo tipo de procesos. Además, el crecimiento explosivo de medios, canales y dispo- sitivos digitales asociados al “internet de las cosas” está pro- porcionando a las organizaciones nuevas oportunidades para extraer y ofrecer mayor valor, mejorar las relaciones y expe- riencias de uso e incrementar la satisfacción de sus usuarios. Es interesante repasar una breve historia de la evolución sobre los datos disponibles en alguna disciplina; por ejemplo, la de la mercadotecnia. El inicio del uso sistemático de datos en este campo se suele asociar a los trabajos de Parlin para la edi- torial Curtis, dirigidos a orientar las actividades de publicidad de esa compañía. Algo después, Gallup inicia la investigación basada en cuestionarios, que empieza a popularizarse en la dé- cada de los veinte, comenzando a introducirse conceptos

25

---

<!-- Página 26 -->

psicológicos para mejorar el conocimiento del consumidor. En 1923, A. C. Nielsen funda una de las primeras compañías de investigación de mercados, midiendo ventas de productos en tiendas; en los treinta y los cincuenta comenzó, respectiva- mente, a medir audiencias de radio y de televisión. En 1931 se fundó Burke, que empezó a realizar investigación de pro- ducto para la compañía Procter & Gamble. En la siguiente década se incrementarán los experimentos de campo y el uso de encuestas por teléfono. Los datos de panel comenzaron a hacerse muy popula- res; primero para medir la exposición a los medios, después, en los cuarenta, para registrar las compras de los consumido- res. Cullinan introdujo métricas para la gestión de las relacio- nes con los clientes (CRM), lo que estimuló el uso de datos de clientes de la propia compañía a principio de los sesenta. En 1966 se fundó el Selling Areas Marketing Institute, que se centra en analizar datos de retiradas de almacén. Casher plantea por primera vez, en 1969, la relevancia de los ordena- dores para la investigación de mercados. Al comienzo de la década de los setenta, Claritas empezó a almacenar datos geodemográficos a partir de bases de datos gubernamentales y agencias de crédito, empleando resultados del sociólogo Booth. La introducción del código de barras y de los dispositi- vos de escaneo de productos en puntos de venta en super- mercados en 1972 marcó el inicio de la captura automatizada de datos. Rápidamente, distintas compañías comprobaron la relevancia de tales datos en su investigación, sustituyendo las auditorías periódicas de tiendas por tales datos de escaneo, lo que incluso permitía trazar a clientes individuales a través de las tarjetas de fidelización. La compañía IRI, centrada en me- diciones de anuncios en televisión, desplegó su servicio de escáneres de códigos de barras en los hogares en 1995. El uso de datos internos de consumidores se vio impul- sado por la introducción masiva de los ordenadores a partir de 1981, permitiendo, entre otras cosas, a los distribuidores almacenar datos de sus clientes, lo que condujo a la aparición

26

---

<!-- Página 27 -->

de bases de datos de mercados. En 1990 surge el primer soft- ware de CRM a partir de los sistemas de Siebel para automa- tización de la gestión de recursos humanos. En 1995, tras más de dos décadas de investigación por la DARPA y otras orga- nizaciones, empieza a popularizarse la World Wide Web, lo que lleva a que empezasen a estar disponibles grandes volú- menes de datos en numerosos campos. Así, por ejemplo, se comenzaron a extraer secuencias de datos de los logs de servi- dores para seguir las visitas de páginas a través de cookies. Los datos de clics aportaban medidas sobre la efectividad de la mercadotecnia online. Internet también estimuló el desarrollo de los sistemas CRM. Así, en 1999 Salesforce introduce tales sistemas en la nube. Google se crea en 1998 y rápidamente liderará los sistemas de búsqueda basados en palabras clave y la captura de datos de búsqueda, aunque existían ya otros motores, como Excite, Infoseek o Altavista, desde hacía casi una década. La aparición de contenido generado por usuarios, espe- cialmente las evaluaciones online de productos, los blogs y los vídeos, produjeron un aumento considerable del volumen y la variedad de datos acumulados. El lanzamiento de Facebook en 2004 abrió la era de la disponibilidad de datos provenien- tes de redes sociales. Con la llegada de YouTube en 2005, las ingentes cantidades de vídeo y de texto subido por usuarios se convirtieron en ingredientes básicos para estimular el desa- rrollo de los recomendadores. Twitter, con sus textos simples de 140 caracteres comenzó en 2006. Los teléfonos móviles llevaban desde principios de los noventa; sin embargo, la pre- sentación del iPhone de Apple en 2007, con sus capacidades GPS, marcó el principio de la captura de datos de geolocali- zación masiva. En una sociedad cada vez más interconectada, existen diversas soluciones emergentes que unen datos de usuarios online con canales offline y otros dispositivos digitales como televisiones, tabletas o móviles, con lo que aumentará cada vez más la disponibilidad de datos. Más aún, se habla que hay ya más de 15.000 millones de dispositivos con sensores con

27

---

<!-- Página 28 -->

capacidad para conectarse y transferir datos sobre redes sin in- teracción de humanos, el denominada internet de las cosas. Esto abre las puertas a nuevos productos y servicios en cuyos proce- sos se generarían, de nuevo, datos de forma masiva. Pensemos, por ejemplo, en la revolución cercana de los coches autónomos, en que los coches actuales llevan alrededor de 100 sensores, en el hecho de que seis billones de personas tengan teléfono móvil o en que haya más de 500 millones de los denominados dispo- sitivos wearable ya desplegados en todo el mundo.

Pero ¿cuán grande es el big de big data?

Una parte del gran interés actual en torno al big data se asocia a cuatro grandes compañías que caracterizan buena parte de lo que son la economía y la sociedad en la actualidad: Google, Amazon, Facebook y Twitter. Así, Google recibe más de cuatro millones de peticiones de búsqueda por minuto de los 2.400 millones de usuarios de internet en el mundo; los 1.300 millo- nes de usuarios de Facebook comparten alrededor de 2,5 mi- llones de piezas de contenido por minuto; en la tienda electró- nica de Amazon hay 278 millones de clientes activos sobre los que se registran datos de búsquedas online y comportamiento de compra; se envían 400 millones de tuits al día. Estas y otras compañías han cambiado el paisaje en muchos campos a tra- vés de la generación, la provisión y el uso de ingentes cantida- des de datos. Para enfocar adecuadamente la discusión, descri- biremos y pondremos en contexto las distintas unidades de almacenamiento de información que se manejan. Dejando aparte la computación cuántica, la unidad bási- ca de información es el bit, que puede adoptar los valores 0 o 1. Para formar palabras, números y cadenas de información más complejas los bits se agrupan en tuplas de bits que se denominan bytes (referenciados con el símbolo B). La de - finición de byte ha sufrido una cierta evolución histórica que puede causar confusión. Nosotros adoptaremos aquí la que lo refiere como una unidad de ocho bits.

28

---

<!-- Página 29 -->

Consideramos después múltiplos de bytes, siendo el pri- mero relevante el kilobyte (kB), caracterizado por ser 1.000 bytes —aunque en realidad, por el carácter binario de la in- 10 formación, se suele hablar del kB para designar 1.024=2 bytes—. Los disquetes de tres pulgadas y media, populares a principios de los ochenta, permitían almacenar 264 kB de in- formación. Una velocidad típica actual de subida de conteni- dos en una conexión de internet es de 820 kB por segundo. Una foto de resolución mediana se asocia a unos 100 kB. A partir de aquí solemos hablar en múltiplos de 1.000 de la unidad anterior. Así, un megabyte (1 MB, 1 mega) se co- 3 6 rresponde a 10kB o 10B. El archivo MP3 de Watching the Detectives de Elvis Costello ocupa algo más de 3 MB. El archi- vo PDF de nuestro libro Adversarial Risk Analysis tiene casi 5 MB. Un vídeo en YouTube de aproximadamente tres minutos de nuestra serie It’s a Risky Life tiene casi 200 MB. Los CD, populares durante toda la década de los noventa, tenían nor- malmente 650 MB de capacidad. La siguiente unidad es el gigabyte (1 GB, 1 giga) y se 9 corresponde a 10B. La biblioteca de 15.000 volúmenes del ICMAT se asocia a, aproximadamente, 75 GB. Los ocho vídeos de It’s a Risky Life ocupan 1,6 GB. El disco duro del ordenador en que se escribe este libro tiene 500 GB. Cuando contratamos extensiones de internet de alta velocidad lo ha- cemos en términos de gigas, por ejemplo 20 GB para un mes. Un pen drive USB estándar almacena 16 GB de infor- mación. Después solemos hablar de terabytes (1 TB, 1 tera). Se 12 corresponde a 10B. Por ejemplo, en la bolsa de Nueva York, antes de introducirse los sistemas de trading algorítmi- co (operaciones financieras que deciden y ejecutan sistemas informáticos), se generaba 1 TB diario de información de mercado. Existen ya discos duros externos de unos pocos TB a precio muy asequible. En el mundo big data se suele hablar de petabytes (1 PB, 15 1 peta) correspondiente a 10B. Se dice, por ejemplo, que Google procesa 20 PB de información al día, con lo que un

29

---

<!-- Página 30 -->

peta vendría a asociarse a la cantidad de datos que Google procesa en una hora. En el siguiente escalón de almacenamiento estaría el 18 exabyte (1 EB, 1 exa), correspondiente a 10B y que marca las fronteras de la computación actual. Por ejemplo, en el pro- grama H2020 se explora la computación en exaescala. El trá- fico anual en 2015 se estimaba en 2021 EB. Se calcula, de hecho, que aproximadamente se almacenan en la actualidad más de 5 EB al día. El tamaño de internet, entendido como almacenamiento digital global, se estima en cerca de 500 EB. También se habla del zettabyte (1 ZB, 1 zetta) corres- 21 pondiente a 10B, y se dice que para 2020 se habrán creado 40 ZB de datos; y del yottabyte (1 YB, 1 yotta), correspon- 24 diente a 10B.

Las otras ‘uves’ del big data

En la descripción anterior nos hemos centrado en el gran vo- lumen de datos almacenados por numerosas organizaciones con la intención de mejorar sus procesos de toma de decisio- nes. Sin embargo, el big data, además de por su alta dimen- sión asociado al volumen, marcado por el paso de gigabytes y terabytes a petabytes, se caracteriza por algunas otras “uves” que ahora describimos:

- La velocidad a la que se adquieren los datos, pasán- dose de datos capturados en una sola toma a datos capturados en muy alta frecuencia e, incluso, en strea- ming. Además, tal alta velocidad puede ir acompañada de la necesidad de tomar decisiones con rapidez y, por tanto, aprehender la evidencia muy rápidamente. - La variedad de datos que se capturan. Más allá de los tipos de datos más tradicionales en estadística (nomi- nales, ordinales, cardinales, multivariantes), se emplean datos de texto (por ejemplo, provenientes de blogs, tuits, opiniones de usuarios, redes sociales…), series

30

---

<!-- Página 31 -->

(por ejemplo, provenientes de sistemas de monitoriza- ción de red o de salud…), imágenes y vídeo, con lo que debemos enfrentarnos a información no estructurada. - La veracidad de los datos, en relación con la fiabilidad de su origen y su validez y precisión.

Las dos primeras características, referidas a volumen y velocidad, son importantes desde el punto de vista de la in- fraestructura computacional, relevantes en este capítulo; ne- cesitamos sistemas suficientemente rápidos que nos permitan procesar los datos recibidos y almacenarlos convenientemen- te. Las otras dos son más importantes desde el punto de vista del análisis y se tratarán en el capítulo 3. Mencionemos que, en otras ocasiones, se añaden otras “uves” al entorno big data. Así, por ejemplo, se habla de la visi- bilidad de los datos en relación principalmente con cuestiones sobre datos abiertos, lo que hace referencia a cuestiones sobre seguridad y privacidad de los datos, sobre los que incidimos en capítulos posteriores. Pero quizás la “uve” más relevante sea la referida al valor de los datos, que trasciende a las anteriores y es la más importante desde el punto de vista social. En definitiva, un buen resumen de los problemas con presencia de big data sería el de aquellos en los que la captura, la gestión y el procesamiento de datos no puede hacerse con las metodologías y tecnologías tradicionales, pues no permi- ten extraer su correspondiente valor de manera adecuada. Así, típicamente los conjuntos de datos estructurados de ta- maño pequeño a mediano se han tratado con métodos con- vencionales basados en hojas de cálculo como Excel; con fi- cheros CSV o conjuntos de datos para paquetes estadísticos como SAS, R, STATA o IBM SPSS Modeler. SAS y SPSS escalan razonablemente bien al crecer el tamaño de los datos, por lo que son populares en numerosos sectores de la indus- tria y en oficinas gubernamentales; R tiene la ventaja de ser código abierto y venir apoyado por una comunidad creciente de usuarios. Además, al ir creciendo el número de registros, resulta más efectivo el uso de bases de datos relacionales

31

---

<!-- Página 32 -->

—como MySQL— para la gestión de datos y la realización de consultas. Más allá de las típicas “uves”, para la mayor parte de personas “big data” quiere decir simplemente “cualquier tipo de fichero de datos que no soy capaz de abrir con Excel” (es decir, superior a 2GB).

Tecnologías del big data

Hacemos ya referencia a las principales tecnologías del big data guiándonos por las fases típicas de un proyecto de ex- tracción de conocimiento a partir de datos para apoyar la to- ma de decisiones que incluiría la obtención de los datos, su integración y consolidación en un repositorio, la consecución de información mediante métodos analíticos, su presentación y, finalmente, su uso el para apoyo a la toma de decisiones. En una primera fase típica se procede a obtener los datos desde orígenes múltiples, reformatearlos y limpiarlos y car- garlos en otra base de datos, data mart, data warehouse o data lake, para analizar cierto proceso de cara a tomar decisiones. Existen diversas herramientas para apoyar estas actividades como OpenRefine, Scribe o Flume. Para aplicaciones web grandes y en tiempo real en las que el volumen, la velocidad y la variedad son altas, se suelen preferir bases de datos NoSQL como MongoDB, CouchDB, Neo4J y Riak, pues proporcionan mecanismos para almace- nar y recuperar datos que no requieren relaciones tabulares como las de las bases de datos relacionales y pueden escalarse sobre hardware estándar. Apache Cassandra, un software de código abierto inicialmente desarrollado por Facebook, es un buen ejemplo de sistema de gestión de bases de datos distri- buidas, diseñado para soportar grandes cantidades de datos en clústeres de servidores. En muchas ocasiones la infraes- tructura final de almacenamiento puede rebasar la capacidad de nuestra organización, por lo que apelaríamos a sistemas en la nube.

32

---

<!-- Página 33 -->

Hadoop, originalmente desarrollado en Yahoo!, es un sis- tema para almacenar y manipular datos en clústeres de orde- nadores escrito en Java que ha alcanzado gran popularidad por ser de código abierto. En cierta forma, Hadoop se ha he- cho sinónimo de big data (y es un error, pues hay otros siste- mas de almacenamiento y gestión y hay otras fases relevantes del proceso, en especial la referida a analítica). En su núcleo está su sistema de gestión distribuida de ficheros y el marco de programación MapReduce de Google para el procesa- miento de datos, que permite gestionar de forma concurrente un número casi ilimitado de tareas. Debido a su relevancia, damos un breve ejemplo de MapReduce que, de hecho, se basa en principios de la pro- gramación distribuida de los años ochenta. Consiste esencial- mente en tres etapas:

- Map. Divide los datos en particiones independientes y los envía a una máquina de un clúster. - Ejecuta las operaciones requeridas en cada una de las máquinas y sobre el subconjunto correspondiente de datos. - Reduce. Combina los resultados.

Consideramos como ejemplo el conteo de palabras de un texto, operación que se utiliza, entre muchas otras, para procesar correos electrónicos antes de su eventual clasifica- ción como correo spam o ilegítimo. Supongamos que hay disponibles cuatro máquinas. El texto original que conside- ramos es:

En un chico malo no, no, no Pa’ fuera lo malo no, no, no Yo no quiero nada malo no, no, no En mi vida malo no, no, no

Mapeamos cada verso en una máquina y aplicamos la operación requerida:

33

---

<!-- Página 34 -->

En (1) un (1) chico (1) malo (1) no (3) Pa’ (1) fuera (1) lo (1) malo (1) no (3) Yo (1) no (4) quiero (1) nada (1) malo (1) En (1) mi (1) vida (1) malo (1) no (3)

Y después lo reducimos a:

En (2) un (1) chico (1) malo (4) no (13) Pa’ (1) fuera (1) lo (1) yo (1) quiero (1) nada (1) mi (1) vida (1)

Típicamente, las aplicaciones se escriben en un lenguaje como Pig, que disecciona peticiones sobre porciones de datos almacenadas en centenares de ordenadores de forma parale- la, y luego combina la información de todas ellas para propor- cionar la respuesta a la petición. Motores SQL como Dremel (Google), Hive (Hortonworks) y Spark (Databricks) propor- cionan tiempos de respuesta muy cortos en esos procesos. Para su posterior procesamiento, sin embargo, los datos de muy alta frecuencia a menudo aún se almacenan en bases de datos relacionales con mayor funcionalidad. C++, Fortran y Java son lenguajes de programación rá- pidos y de bajo nivel para apoyar la realización de analítica, apoyados en numerosas bibliotecas de rutinas numéricas. Los programas de Java a menudo se incrustan como applets den- tro del código de las páginas web. R es mucho más lento pero se emplea a menudo por ser de código abierto y de muy alto nivel con funcionalidades comparables a MATLAB (en ma- temáticas) y SAS (en estadística). Perl es un software adapta- do al procesamiento de datos no estructurados de clics (HTML) que fue inicialmente empleado por Amazon. Sin embargo, ha sido sustituido por Python (usado por Dropbox), un lenguaje de programación mucho más intuitivo que facili- ta la implementación de MapReduce. Muchos de los modelos estadísticos y econométricos ac- tuales no son escalables a big data. Los algoritmos MapReduce proporcionan una solución y permiten el procesamiento de datos de forma masivamente paralela, descomponiéndolos en

34

---

<!-- Página 35 -->

cálculos locales que se aplican a parte de los datos distribui- dos en núcleos múltiples en lugar de copiar la totalidad de los datos como entrada a un software analítico. Como ejemplo, la maximización de la verosimilitud se adapta bien a MapReduce pues el logaritmo de la verosimilitud es una suma de términos que se puede distribuir fácilmente, permitiendo las operacio- nes de Map y Reduce, utilizándose en este contexto métodos de descenso del gradiente estocástico para optimizar la log- verosimilitud. En lugar de evaluar el gradiente de todos los tér- minos de la suma, se muestrea un subconjunto de esos térmi- nos en cada paso y se evalúa su gradiente, lo que alivia enormemente los cálculos. Un buen ejemplo es la implementa- ción lm de R para modelos lineales, que no escala a problemas big data, por lo que se han producido las bibliotecas biglm y bigmemory. Otro ejemplo es Apache Mahout, que incluye im- plementaciones en código abierto de algoritmos de aprendizaje automático distribuidos y escalables en las áreas de filtrado co- laborativo, análisis de conglomerados y clasificación. Por lo que respecta a la presentación y visualización de datos destacarían, aparte de las excelentes capacidades grá - ficas de R, Tableau (que permite buscar dentro de bases de datos relacionales, cubos OLAP, bases de datos en la nube y hojas de cálculo y generar distintos gráficos interactivos) y Pentaho BI Suite (de código abierto, con herramientas inte- gradas para generar informes y realizar minería de datos). CartoDB es otra opción especializada en la producción de mapas. Concluimos con algunos proyectos relevantes ad hoc pa- ra big data:

1 - BigDataEuropees un proyecto H2020 que ha de- sarrollado una plataforma big data adaptable de fácil despliegue y uso. Emplea distintos bloques básicos, como Apache Spark, Hadoop HDFS, Apache Flink y otros, de manera que se facilita su integración con

1. https://www.big-data-europe.eu/

35

---

<!-- Página 36 -->

otras tecnologías y aplicaciones a través de su integra- dor big data, que puede operar en una máquina local de desarrollo o escalar a centenares de nodos conecta- dos en enjambre. 2 - Amazon Web Services(AWS) es una colección de servicios de computación en nube ofrecida a través de internet por Amazon y compite con servicios como Microsoft Azure o Google Cloud Platform. Para ex- traer conocimiento de datos, AWS ofrece un conjunto de servicios que abarcan todos los pasos de la cadena del proceso de análisis, incluyendo el almacenamiento de datos, la inteligencia de negocios, el procesamiento por lotes, el procesamiento de transmisiones, el apren- dizaje automático y la organización del flujo de traba- jo de datos. 3 - TensorFlowes una biblioteca de código abierto para aprendizaje automático desarrollada por Goo- gle para satisfacer sus necesidades de sistemas capaces de construir y entrenar redes neuronales para detectar y descifrar patrones y correlaciones. Actualmente se utiliza tanto para la investigación como para el desa- rrollo de producto. 4 - Teradata University Networkes un portal para apoyar el desarrollo de la comunidad académica en materias de data warehousing, inteligencia de nego- cios, bases de datos, big data y apoyo a la toma de decisiones por medio de materiales educativos y software. 5 - Cognos Analyticses el sistema de IBM para facilitar el uso de métodos avanzados analíticos sobre conjun- tos big data que recientemente ha sustituido a Watson Analytics.

2. https://aws.amazon.com 3. https://www.tensorflow.org/ 4. https://www.teradatauniversitynetwork.com/ 5. https://www.ibm.com/watson-analytics?lnk=hmhm

36

---

<!-- Página 37 -->

6 - Kagglees la mayor comunidad de científicos de datos del mundo. En ella las organizaciones y los investiga- dores publican sus conjuntos de datos y sus proble- mas y los miembros de la comunidad compiten para producir los mejores modelos.

Para saber más

En este capítulo hemos presentado la evolución histórica que ha conducido a las principales tecnologías del big data. En cierta forma hay algo de exceso de bombo en torno a este concepto. De hecho, muchas compañías invirtieron tal vez demasiado en la captura y almacenamiento de datos y no tan- to en analítica, en métodos de ciencia de datos. Aquí nos he- mos centrado fundamentalmente en cuestiones relativas a su recolección y gestión. En el siguiente capítulo nos centramos en aspectos relativos a su análisis, tanto en sus aspectos des- criptivos como en los predictivos y prescriptivos, discutiendo cómo extraer de los datos para mejorar la toma de decisiones. Insistimos en que el big data no es una panacea. En este punto es interesante recordar la discusión small data-big data. En muchos problemas de toma de decisiones se dispondrá de escasos datos; en otros, habrá muchos datos para ciertas par- tes del problema y no tantos para otros, por lo que será nece- sario poder disponer de capacidades para trabajar simultá- neamente en ambos contextos. Concluimos con algunas breves referencias en las que ampliar información. Una breve historia más extensa sobre el impacto de los datos en la investigación de mercados puede verse en Wedel y Kannan (2016). Una revisión de las tecno- logías empleadas en big data puede verse en Zomaya y Sakr (2017); insistimos, sin embargo, en que se trata de un entorno enormemente cambiante. Los big data landscape anuales de

6. https://www.kaggle.com/. Si el lector no consigue resolver su problema big data y no encuentra disponible al DataLab del ICMAT, una buena oportunidad puede ser emplear Kaggle.

37

---

<!-- Página 38 -->

Turck y FirstMark permiten vislumbrar los últimos avances de una forma rápida. Mencionemos, para acabar, que no hemos hecho refe- rencia a los datos oscuros (dark data). Con ello se suele desig- nar a los datos adquiridos, pero no empleados, para lograr conocimiento y apoyar la toma de decisiones, típicamente debido a que una organización no tiene capacidad de proce- samiento para analizarlos. Así, por ejemplo se estima que la mayoría de las organizaciones no analizan más que el 1% de sus datos, almacenándolos solo por requisitos legales o por- que se cree que tal vez puedan ser útiles en el futuro cuando se disponga de capacidad para procesarlos, debido a que su almacenamiento es relativamente barato.

38

---

<!-- Página 39 -->

CAPÍTULO 3

## Métodos estadísticos y de aprendizaje

## automático para el tratamiento de big data

Introducción

Como hemos indicado, con frecuencia al hablar de big data se pone el énfasis en los aspectos tecnológicos referidos a la capacidad de recoger y almacenar datos, que ha crecido de manera exponencial en los últimos años gracias al uso ma- sivo de sensores y dispositivos móviles. Sin embargo, una parte esencial de cualquier proyecto de big data consiste en emplear adecuadamente algoritmos para su procesamiento y, en particular, algoritmos que permiten aprender de los datos, de manera que la aplicación que se desarrolla pueda predecir comportamientos futuros y realizar tareas que en- tendemos como inteligentes. Son los aspectos que en la in- troducción se designan como estadísticos y de aprendizaje automático, que designaremos en lo que sigue como machi- ne learning (ML). En general, podemos dividir estos algoritmos en tres grandes bloques: de preprocesamiento, de análisis y de visuali- zación. Se suelen aplicar de manera secuencial y constituyen el ciclo de desarrollo de un proyecto de ciencia de datos aunque, como veremos, dicho ciclo puede recorrerse múltiples veces hasta conseguir el comportamiento adecuado. Revisamos des- pués los aspectos principales de las tres grandes tipologías

39

---

<!-- Página 40 -->

metodológicas de análisis referidas al aprendizaje supervisa- do, al no supervisado y al aprendizaje por refuerzo.

Preprocesamiento, análisis y visualización

Comencemos describiendo la primera fase de preprocesa- miento. Es probablemente la más mecánica y menos valorada en los proyectos de big data, pero puede ocupar hasta un 80% del tiempo total de un científico de datos. Si no se realiza de manera correcta, todos los resultados posteriores quedarán, en gran medida, invalidados. Como se acostumbra a decir, garbage in, garbage out. En esta fase se reciben los datos captu- rados en estado puro. Suelen provenir de fuentes diferentes, pueden encontrarse físicamente en servidores o bases de da- tos con ubicaciones distintas y se presentan en gran variedad de formatos, tanto estructurados (tablas y bases de datos) co- mo no estructurados (texto libre, imágenes, audio, vídeo, etc.). Con frecuencia, la información que resulta realmente útil para elaborar un modelo suele ser un subconjunto relati- vamente pequeño de toda la almacenada, de modo que hay que identificar dónde se encuentra tal información y extraer- la, como mencionábamos cuando hacíamos referencia a ex- traer valor de los datos. Además, rara vez ocurre que la infor- mación se encuentra de manera íntegra y limpia, por lo que una tarea siempre necesaria es proceder a la limpieza de los datos, por ejemplo para uniformar formatos, codificar carac- teres, verificar que no existen valores corruptos, etc. También suele ocurrir que algunas entradas de una base de datos no contienen el valor requerido, encontrándose su campo vacío (null). Esto puede deberse a que dicho dato se ha perdido en la transmisión o, simplemente, a que el formulario de recogi- da de datos no obligaba a recogerlo para su validación y el dispositivo o persona que realizó la entrada dejó tal campo vacío. Existen numerosos métodos para rellenar la informa- ción ausente con criterios estadísticos, operación que se co- noce como “imputación de datos”.

40

---

<!-- Página 41 -->

En una segunda fase de análisis se procede a construir modelos para apoyar las tareas deseadas: predecir precios de venta de inmuebles, predecir los clientes que se darán de baja de un servicio, clasificar imágenes para reconocimiento facial, segmentar los usuarios de una plataforma digital, etc. En esta fase concurren fundamentalmente conocimientos de tipo es- tadístico, matemático y de programación, para tomar los da- tos ya limpios, crear y entrenar un modelo y evaluar su efi- ciencia antes de ponerlo en producción. En función del tipo de problema que afrontamos solemos distinguir entre tres paradigmas: aprendizaje supervisado, aprendizaje no super- visado y aprendizaje por refuerzo, según desarrollamos más abajo. Como parte del ciclo de desarrollo, con frecuencia en el proceso de elaboración de un modelo se vuelve a la fase de preprocesamiento para crear variables nuevas a partir de los datos en estado puro. Si en la primera fase hablamos de ex- tracción de variables (feature extraction), en la segunda trata- mos de combinar estas para elaborar otras variables derivadas o secundarias que puedan resultar informativas de cara a la predicción (feature engineering). Por ejemplo, en un modelo para detectar fraude en pagos con tarjeta de crédito puede resultar útil utilizar la cantidad total retirada en operaciones durante la última hora, pero esa información no está presente en cada transacción, sino que hay que calcularla a partir de operaciones anteriores. Por último, en muchos proyectos se requiere una tercera fase en la que debemos ser capaces de transmitir la informa- ción obtenida en el análisis de datos de manera efectiva. Esta tarea combina aspectos científicos en relación con la elabora- ción rigurosa de gráficas y diagramas con capacidades artís- ticas y de comunicación. Así, en un mundo con cada vez más presencia de datos en todos los niveles, la visualización efecti- va resulta imprescindible para aprehender la realidad subya- cente a los datos. Un excelente ejemplo de recopilación y vi- 7 sualización de datos es el proyecto Data USA, una plataforma

7. https://datausa.io/

41

---

<!-- Página 42 -->

web con herramientas en JavaScript que recoge información de bases de datos públicas y las presenta de forma integrada a disposición de cualquier ciudadano de manera gratuita. Así, cualquier persona puede realizar sus propias visualizaciones de manera interactiva, lo que facilita entender el estado de cualquier aspecto socio-económico de esa nación.

Aprendizaje supervisado, no supervisado y por refuerzo

Como hemos indicado, los tres grandes paradigmas del aprendizaje automático son el supervisado, el no supervisado y el aprendizaje por refuerzo. Aunque los presentemos de manera diferenciada, en muchos problemas reales concurri- rán varios de ellos junto con variantes intermedias. En gene- ral, en una aplicación concreta de ML la elección del modelo vendrá determinada fundamentalmente por la tipología de da- tos disponibles y, en menor medida, por los requisitos de efi- ciencia computacional (la memoria disponible, la necesidad de respuesta en tiempo real, etc.). También será relevante la naturaleza de la aplicación, fundamentalmente cómo de im- portante es que el modelo sea interpretable; es decir, si el ob- jetivo es simplemente conseguir la mejor predicción posible, aunque usemos una caja negra o, por el contrario, debemos ser capaces de interpretar los parámetros del mismo. En el caso supervisado se suministran pares de valores (X, Y) i=1,…,N, donde X son las variables predictivas, Y re- ii presenta las variables cuyos valores queremos predecir y N es el número de casos de los que disponemos. El problema con- siste en ser capaz de predecir el valor de los datos Y dados los valores de X, es decir, aproximar la distribución de probabili- dad condicionada p(Y|X). Si la variable Y es categórica, ha- blamos de un problema de clasificación, mientras que si es continua solemos decir que nos enfrentamos a un problema de regresión. Por ejemplo, si nos proporcionan los precios de venta de 100.000 viviendas, junto con características de cada una de ellas como su ubicación, la superficie o el año de

42

---

<!-- Página 43 -->

construcción, podemos elaborar un modelo de regresión para poder predecir el precio de venta de otra vivienda, conocidas el resto de características. La empresa americana Zillow fue pionera en el uso de estos modelos para sus instrumentos de valoración; hoy en día, casi todos los portales inmobiliarios usan técnicas similares. Un ejemplo típico de clasificación es el asociado a los filtros antispam: las variables predictivas po- drían incluir las palabras incluidas en el mensaje, la dirección del remitente, etc., y la variable a predecir es una etiqueta bi- naria que indica si el correo es no deseado (spam) o legítimo (ham). En el aprendizaje no supervisado se suministran simple- mente los valores de las variables observadas X, pero no dis- ponemos de etiquetas o valores y. Se trata entonces de apren- der cómo es la distribución de dichos datos, es decir, aproximar la distribución de probabilidad p(X) Basados en una aproximación de esta distribución (density estimation) podemos abordar problemas como detectar puntos que no parezcan haber sido generados por la misma distribución, es- to es, datos anómalos (outlier detection), o bien detectar patro- nes de similaridad entre los mismos, agrupándolos en con- juntos de características similares (clustering). Un ejemplo consistiría en emplear los datos de interacción de los usuarios de una web (cuánto tiempo han permanecido en cada página, cuántos clics han hecho y dónde, etc.) para ser capaz de seg- mentar los potenciales clientes de dicha página en categorías como usuario experto, usuario nuevo, no humano (bot), etc. En el aprendizaje supervisado siempre disponemos de una métrica para determinar la bondad de la predicción, pues podemos comparar los valores que predice el modelo con los valores observados. De hecho, como veremos más adelante, los parámetros del modelo se ajustan para optimizar una elec- ción concreta de dicha métrica. Sin embargo, en el aprendiza- je no supervisado no podemos evaluar de manera cuantitativa el rendimiento de los modelos. Quizás por este motivo se han desarrollado mucho más las técnicas para aprendizaje super- visado durante los últimos años. Una entidad bancaria que

43

---

<!-- Página 44 -->

quiera desarrollar un sistema de detección de fraude en pagos con tarjeta electrónica tendrá resultados mucho mejores si dispone de los datos de transacciones (importe, lugar, tipo de comercio, hora, etc.) anotados como fraude/legítimo, que si dispone solo de los datos sin anotar. Por último, el aprendizaje por refuerzo es el paradigma más flexible de ML. En él se simula la forma de aprender en mamíferos, con la que un agente puede interactuar con el me- dio realizando acciones que reciben cierta recompensa y transforman su estado. El objetivo es maximizar la recompen- sa esperada a largo plazo eligiendo en cada momento la ac- ción más adecuada, teniendo en cuenta no solo la recompen- sa que se recibirá en dicho instante como resultado de la acción inmediata, sino también la secuencia de posibles esta- dos y futuras recompensas. Este tipo de problemas requiere un equilibrio entre las denominadas “explotación” y “explo- ración” del conocimiento adquirido: la primera supondría escoger acciones que nos aporten la mayor recompensa in- mediata, mientras que la segunda supone probar otras accio- nes que quizás nos aporten una mayor recompensa acumula- da en el futuro. Quizás el mayor hito reciente de los algoritmos de aprendizaje por refuerzo ha sido en juegos de estrategia y, en particular, en el juego del Go, que por su complejidad se consideraba el caballo de batalla para los algoritmos de IA. El programa AlphaGo, desarrollado por Google Deep Mind, consiguió derrotar por primera vez al campeón mundial en marzo de 2016. El mejor algoritmo actual, AlphaGo Zero, ya no emplea datos de partidas anteriores ni ningún tipo de su- pervisión humana o conocimiento específico. El programa hace tabula rasa, con conocimiento solo de las reglas del jue- go, y explora estrategias alcanzando un nivel superior al de los humanos en pocas horas a base de jugar contra sí mismo. Tras muchas partidas jugadas, la señal de refuerzo (partida ganada o perdida) se propaga para conseguir una evaluación adecuada de la fortaleza de una posición y, por tanto, de la jugada que se ha de efectuar. Los modelos de aprendizaje profundo por refuerzo (Deep RL), que están en la base del

44

---

<!-- Página 45 -->

algoritmo de AlphaGo, tendrán sin duda un importante desa- rrollo en el futuro. En tareas más generales que los juegos de estrategia, uno de los retos principales de la investigación radica en cómo fijar un buen sistema de recompensas para lograr que un agente aprenda a realizar la acción deseada. En un programa de aje- drez, la recompensa ha de ser únicamente por ganar la partida, ya que fijar recompensas por captura de piezas como hito in- termedio puede conducir a estrategias que, a pesar de capturar muchas de ellas, terminen por perder la misma. En problemas complejos, un algoritmo de aprendizaje por refuerzo puede buscar estrategias para resolver la tarea deseada realizando ac- ciones que tengan consecuencias no previstas o incluso peli- grosas. El desarrollo de algoritmos robustos de aprendizaje por refuerzo que reúnan todos los requisitos de seguridad necesa- rios para su puesta en marcha en tareas cotidianas es uno de los campos abiertos más importantes en inteligencia artificial.

Entrenamiento, validación y test

Nos centraremos en este epígrafe en problemas de aprendi- zaje supervisado para describir el ciclo típico de elaboración de un modelo, comentando algunas de las características co- munes de los problemas de aprendizaje estadístico. Los mo- delos estadísticos de tipo paramétrico suelen aproximar la distribución de probabilidad p(Y|X) a través de familias de distribuciones indexadas por parámetros, intentándose fijar el valor de estos parámetros de manera que la distribución ob- tenida explique adecuadamente los datos observados. Este proceso de ajuste se conoce como aprendizaje en el contexto de ML. Para ello hemos de ser capaces de estimar dichos parámetros a partir de un conjunto de datos y luego evaluar el modelo resultante sobre otro conjunto de datos obtenido a partir de la misma distribución. Por este motivo, el conjunto de datos observados suele di- vidirse en tres subconjuntos denominados, respectivamente,

45

---

<!-- Página 46 -->

de “entrenamiento”, de “validación” y de “test”. La manera en que se hace esta división puede depender de la aplicación específica —por ejemplo si se han de tomar en consideración aspectos temporales—, pero pensemos por el momento que el conjunto original se divide de manera puramente aleatoria. Utilizamos el conjunto de entrenamiento para entrenar un modelo de nuestra elección: mostraremos todos los datos de este conjunto al modelo para fijar el valor de sus parámetros libres. Esto supone la optimización de una función de coste que mide cuán distantes están las predicciones del modelo de los datos observados e intenta ajustar los parámetros para que este error sea lo menor posible. Con el modelo entrenado po- demos evaluar su rendimiento sobre otro conjunto de datos, diferente del que hemos utilizado en esta fase, pero proceden- te de la misma distribución.

Figura 2 Dependencia del error con la complejidad del modelo y sobreajuste.

Observemos, sin embargo, que en realidad no tenemos por qué limitarnos a un único modelo, sino que ajustaremos distintos con diferentes arquitecturas o características, todos ellos sobre el conjunto de entrenamiento y realizando prue- bas sobre el conjunto de validación para seleccionar el mejor de ellos (model selection). Por último, el mejor modelo se eva- luará sobre un tercer conjunto de datos no utilizado hasta el

46

---

<!-- Página 47 -->

momento para tener una estimación fiable de su rendimiento final. Un error frecuente en la construcción de modelos es emplear información sobre el conjunto final de test en la ela- boración del modelo (data leakage), lo que puede conducir a obtener resultados mejores de los que se conseguirían cuando el modelo se ponga en producción. Como buena práctica, re- petiremos la división del conjunto de datos original en distin- tos subconjuntos de entrenamiento, validación y test, repi- tiendo todo el proceso para disponer de una estimación más robusta del rendimiento final. Si representamos el error cometido por el modelo en los conjuntos de entrenamiento y de test nos encontraremos mu- chas veces con una situación como la descrita en la figura 2. Empleando modelos más flexibles y expresivos —es decir, con mayor capacidad para ajustar los datos, por ejemplo porque in- cluyen una mayor cantidad de parámetros ajustables— pode- mos llegar a reducir el error de entrenamiento tanto como que- ramos. Sin embargo, suele comprobarse que los modelos tan complejos no generalizan bien; esto es, su predicción es mucho peor sobre nuevos ejemplos de la misma distribución, por lo que crece el error en el conjunto de test. En una situación como esta decimos que el modelo sobreajusta los datos (overfitting). Por este motivo hemos de escoger modelos más parsimoniosos en los que se encuentre un equilibrio entre la capacidad de ajus- te a los datos y la capacidad de generalización.

Figura 3 Frontera de decisión en un problema de clasificación binaria. De izquierda a derecha: infrajuste (λ alto), óptimo y sobreajuste (λ bajo).

Infra ajusteAjuste óptimo Sobreajuste (demasiado simple(demasiado bueno para ser bueno)para ser cierto)

47

---

<!-- Página 48 -->

Una forma de lograr este equilibrio es introducir un tér- mino en la función de coste que penalice la complejidad del modelo, lo que se consigue típicamente añadiendo un térmi- no proporcional al tamaño de los coeficientes con una cons- tante de proporcionalidad. Esta técnica de regularización permite alcanzar el equilibrio mencionado anteriormente: con valores bajos de la constante conseguimos modelos más flexibles aumentando el riesgo de sobreajuste, mientras que valores muy altos de la misma producen modelos demasiado sencillos que no llegarán a ajustar bien los datos de entrena- miento, como se ilustra en la figura 3. El valor óptimo del parámetro de regularización se fija experimentalmente, pro- bando modelos con diferentes valores sobre el conjunto de validación y seleccionando el mejor valor. Por este motivo, tal constante se suele denominar “hiperparámetro”. Existen numerosos algoritmos y modelos de aprendizaje supervisado, de forma que incluso una descripción mera- mente superficial de todos ellos excedería nuestros objetivos en este libro. Nos conformaremos con presentar las caracte- rísticas generales de las principales clases de algoritmos. El lector interesado puede aprender más consultando la infor- mación final del capítulo. Una excepción al comentario ante- rior son los algoritmos de redes neuronales profundas (deep learning), que por su importancia reciente merecen una des- cripción más detallada en el siguiente epígrafe. Para concluir esta discusión, y teniendo en cuenta la gran cantidad de modelos posibles, podemos preguntarnos cuál es el que más nos conviene utilizar. Esta pregunta apa- rentemente inocente puede tener respuestas más o menos elaboradas. Una respuesta sencilla podría ser: si disponemos de suficientes datos de entrenamiento, la mejor elección será probablemente un modelo de redes neuronales profundas. En efecto, sobre datos estándar como imágenes, texto escri- to por humanos, etc., las redes neuronales profundas supe- ran a muchos otros algoritmos en tareas como clasificación de imágenes, detección de objetos, clasificación de texto o traducción automática. Sin embargo, un resultado conocido

48

---

<!-- Página 49 -->

popularmente como el teorema “no free lunch” (Wolpert, 1996) nos recuerda que no existe un único modelo capaz de superar sistemáticamente a otro sobre todas las posibles dis- tribuciones de datos. Es decir, la elección concreta del mejor modelo depende de cómo sean los datos y la tarea a realizar.

Aprendizaje profundo

El conjunto de modelos conocido colectivamente como de aprendizaje profundo (deep learning) supone un claro ejem- plo de rebranding científico y ha marcado el renacer de una disciplina que ha presentado, desde su inicio en los años se- senta del pasado siglo, fases como la actual, de enorme activi- dad, alternadas con otras de menor interés por parte de la comunidad científica especializada. En esencia, los modelos de aprendizaje profundo son modelos muy flexibles que pue- den llegar a tener cientos de miles de parámetros ajustables y son, por tanto, capaces de aprender distribuciones en espa- cios de dimensión alta para realizar tareas complejas. Otra característica es que al estar dichos parámetros distribuidos por capas, la red aprende conceptos en diferentes grados de abstracción de manera jerárquica. El auge actual de este tipo de modelos se debe, fundamentalmente, a dos motivos: la dis- ponibilidad de grandes conjuntos de datos anotados para en- trenamiento y el aumento de la potencia computacional, ade- más de otros factores técnicos que trataremos más adelante. Como hemos comentado anteriormente, un modelo con muchos parámetros ajustables precisa gran cantidad de ejem- plos para su entrenamiento con el fin evitar problemas de sobreajuste. En tareas de clasificación de imágenes, la base de datos de ImageNet contiene 14 millones de estas anotadas por humanos, con varios cientos de imágenes para cada cate- goría típica como “espada” o “melocotón”. De entre ellas, al menos un millón contienen, además, la localización del objeto dentro de la imagen (Bounding Box), necesaria para entrenar modelos de detección de objetos. Cada año, la competición

49

---

<!-- Página 50 -->

ImageNet Large Scale Visual Recognition Challenge (ILSVC) pone a prueba los mejores algoritmos (casi todos basados en redes neuronales, especialmente de unos años a esta parte) pa- ra clasificar imágenes de objetos en 1.000 categorías, entre ellas 90 razas de perros. Los algoritmos actuales superan ya la capa- cidad humana: la red que venció la competición en 2017 (Hu, 2018) tenía un error top-5 (el número de veces que la categoría correcta no se encuentra entre las 5 más probables) de 2,25%, mientras que la capacidad humana se estima que tiene un error top-5 de 5% para la misma tarea (Russakovsky, 2015). Los modelos complejos necesitan grandes cantidades de datos anotados con etiquetas, pero ¿cómo podemos obtener dichos datos? Algunos datos generados por aplicaciones in- corporan las etiquetas de manera automática por el propio dispositivo que los produce: por ejemplo, los tuits contienen datos de geolocalización, lenguaje o edad del emisor, y mucha de la información que se genera en redes sociales es anotada por los propios usuarios sin que estos sean plenamente cons- cientes de ello. Además, existen plataformas donde se gene- ran bases de datos anotadas para tareas específicas; de entre ellas la más conocida probablemente sea Amazon Mechanical 8 Turk. Esta plataforma de crowdsourcing permite a personas de todo el mundo realizar tareas que requieran inteligencia humana para anotar datos, a cambio de una modesta remu- neración por el tiempo empleado. El segundo factor que ha permitido el desarrollo de las redes neuronales profundas han sido los avances constantes en la capacidad de computación, necesarios para ser capaces de procesar las ingentes cantidades de datos necesarias para entrenar dichos modelos, así como el desarrollo de algoritmos que lo posibilitan, en particular los denominados “algoritmos estocásticos de descenso del gradiente”.

8. https://www.mturk.com/. El nombre proviene de un “invento” construido en 1770 en el que un supuesto autómata, ataviado según la tradición otomana, jugaba al ajedrez de manera mecánica, llegando a vencer a estadistas como Benjamin Franklin o Napoleón Bonaparte. Este “precursor” de los modernos programas de ajedrez era en realidad un gran maestro escondido debajo de la mesa, que movía las piezas con un imán.

50

---

<!-- Página 51 -->

Figura 4 Arquitectura esquemática de una red neuronal (perceptrón multicapa).

Sin entrar en detalles matemáticos, podemos dar algunas ideas sobre cómo funciona una red neuronal profunda. En la figura 4 se presenta esquemáticamente la arquitectura de una red con cuatro capas. En la capa de entrada (input layer) se introduce un vector de datos correspondiente a cada ejemplo del conjunto de entrenamiento. Si se tratase de una imagen en color, la capa de entrada tomaría el valor de cada uno de los píxeles en los tres canales RGB (rojo, verde, azul; por sus si- glas en inglés); si fuera un texto, su codificación en un alfabe- to, etc. En cada nodo de la primera capa se calcula una suma ponderada de los valores de la capa de entrada y el resultado se pasa a través de una función de transferencia. Estas opera- ciones están inspiradas en el funcionamiento de las neuronas del sistema nervioso, que captan información de muchas otras neuronas y, en el momento en que la suma de todos los estímulos excede cierto umbral, transmiten el impulso ner- vioso a través de su axón. El proceso se repite en cada capa, que toma como entrada la salida de la capa anterior. Por últi- mo, en la última capa la salida es un único vector de M com- ponentes —si se trata de un problema de clasificación en M 9 clases— que expresa la probabilidad de que la imagen de entrada pertenezca a cada una de las clases. Los parámetros

9. Y análogamente en el caso de regresión.

51

---

<!-- Página 52 -->

ajustables del modelo son las matrices de pesos en cada capa y dichos pesos se ajustan de la siguiente manera: en la propa- gación directa (forward-prop) se emplean los pesos aprendi- dos hasta el momento para predecir un vector de probabilida- des, dicho vector se compara con el valor real de la clase a la que pertenece la imagen y el proceso se repite sobre todos los ejemplos de entrenamiento, llegando a una medida del error promedio en la predicción. En el proceso inverso (back-prop) se actualizan los pesos usando el gradiente de la función ob- jetivo. El ciclo se repite hasta conseguir la convergencia en la función de error y, por tanto, conseguir que la red haya apren- dido a clasificar correctamente diferentes imágenes incu- rriendo en el mínimo error. Una vez la red ha sido entrenada, la predicción es muy rápida sobre cada nuevo ejemplo; sin embargo, el proceso de entrenamiento de redes de grandes dimensiones requiere cálculos intensivos sobre gran cantidad de datos. En los últimos años ha proliferado el uso de bibliotecas de software como TensorFlow, Torch, Keras o Theano para programar modelos de redes neuronales en apenas 20 líneas de código. Estas bibliotecas (frameworks) contienen todas las funciones de alto nivel y están diseñadas para paralelizar la computación en el proceso de entrenamiento, en el que los pesos se actualizan tras procesar un pequeño subconjunto (batch) de los datos de entrenamiento. Dado que la mayor parte de cálculos necesarios consiste en multiplicar matrices o tensores de gran tamaño, desde hace unos años se utilizan tarjetas gráficas de propósito general (GPU) para el entrena- miento de redes profundas, pues contienen miles de peque- ños procesadores que posibilitan un gran paralelismo en la 10 computación.

10. El principal fabricante de tarjetas gráficas es la empresa Nvidia, que ha visto ampliado su negocio desde el mercado de los videojuegos hasta los grandes centros de datos dedicados a la inteligencia artificial (y la minería de bitcoins).

52

---

<!-- Página 53 -->

Algunos campos de aplicación del aprendizaje automático

Aunque en los siguientes capítulos abordaremos el impacto de la ciencia de datos y la IA en diversos ámbitos de la socie- dad, querríamos cerrar este capítulo con una breve enume- ración de los principales campos de desarrollo de esta disci- plina.

Visión artificial

Este campo recoge toda la tecnología desarrollada para ad- quirir, procesar, analizar y entender imágenes de manera au- tomática, habilitando a un sistema informático para desarro- llar tareas propias de esta capacidad humana. La visión artificial es un campo multidisciplinar donde confluyen, entre otras, la óptica, el procesamiento de señales, la electrónica, la estadística y la IA. Algunas de las tareas más comunes en este campo son:

- La clasificación de imágenes en categorías prefijadas. - La descripción en lenguaje natural del contenido de una imagen (image tagging). - La búsqueda de imágenes por contenido. - El reconocimiento facial. - La detección de objetos y su localización en el interior de una imagen. - La reconstrucción de imágenes 3D a partir de imáge - nes 2D. - El reconocimiento óptico de caracteres escritos (OCR). - El análisis de movimiento en vídeo.

Las aplicaciones de estas técnicas son innumerables, in- cluyendo el control de calidad en procesos industriales, el de- sarrollo de apps que proporcionan descripciones sonoras para ayuda a invidentes, la provisión de técnicas para imagen mé- dica y ayuda al diagnóstico en medicina, el procesamiento

53

---

<!-- Página 54 -->

automático de vídeo en cámaras CCTV, el desarrollo de sis- temas de navegación en conducción autónoma, la identifica- ción biométrica por reconocimiento del iris, la realidad au- mentada, el control de cultivos en agricultura de precisión, el procesamiento de imágenes por satélite y un largo etcétera.

Procesamiento del lenguaje natural

Desde el advenimiento de los modelos de lenguaje basados en redes neuronales, uno de los campos que está experimentando mayor desarrollo en los últimos años es el procesamiento del lenguaje natural. Si en el origen de esta disciplina tuvieron más peso los modelos formales de lenguaje, como las gramáticas libres de contexto de Chomsky, cuyo objetivo era capturar la generación de lenguaje mediante un conjunto de reglas, en la ac- tualidad se están imponiendo modelos estadísticos y de ML. En ellos, la representación de la estructura del lenguaje es me- nos interpretable, pero son capaces de realizar tareas cada vez más complejas, entrenando modelos de redes profundas sobre millones de textos. Esta transición está resumida en la famosa frase atribuida a Jelinek, director del grupo de investigación en lenguaje del Thomas J. Watson IBM Research Center y uno de los pioneros en procesamiento del lenguaje natural: “Cada vez que despedimos a un lingüista, mejora el rendimiento de nues- tro clasificador”. Enseñar a una máquina a entender nuestro lenguaje puede ser muy diferente a cómo nosotros mismos lo entendemos. Las tareas más comunes en este campo son:

- La clasificación de textos. - El reconocimiento de entidades nombradas. - La síntesis del habla (text-to-speech). - El reconocimiento del habla (speech recognition). - Los sistemas de diálogo y respuesta a preguntas (Siri, Alexa, etc.). - La traducción automática. - El resumen automático de textos. - El análisis morfológico y sintáctico (POS tagging).

54

---

<!-- Página 55 -->

Las herramientas de procesamiento del lenguaje natural se usan también para el análisis de sentimientos y opiniones en redes sociales, la indexación y la extracción de informa- ción en bases de datos jurídicas y de salud, el diseño de asis- tentes en servicio al cliente; y se integran como un elemento más en un número cada vez mayor de aplicaciones, como por ejemplo en los robots sociales Aisoy. Los primeros dispositi- vos electrónicos para traducir lenguaje hablado en conversa- ciones en tiempo real empiezan a verse ya en el mercado.

Inteligencia de negocio

Dentro de la inteligencia de negocio se engloban todas las estrategias, los productos, las tecnologías y los datos que una empresa utiliza para mejorar su visión sobre los procesos que intervienen en sus áreas de negocio. En sus modelos conflu- yen, además de la ciencia de datos y la IA, conocimientos sobre economía, teoría de juegos, investigación operativa, psi- cología, mercadotecnia o sociología, entre muchos otros. Uno de los ejemplos más famosos fue la competición lanzada por Netflix en 2006 (por entonces apenas conocida en España) para predecir las evaluaciones de sus usuarios sobre algunas películas, conociendo las evaluaciones que habían rea- lizado sobre otras. El concurso otorgaba un suculento premio de un millón de dólares para el algoritmo con mejor eficiencia en su predicción, si conseguía superar al empleado por la com- pañía. Este tipo de algoritmos, llamados “sistemas de recomen- dación”, están en la base del negocio de grandes corporaciones como Amazon, Netflix o Spotify. En la actualidad están siendo adoptados por la mayoría de comercios para afinar los produc- tos que ofrecen a cada uno de sus clientes. La experiencia de la competición de Netflix tuvo un éxi- to considerable y motivó la creación de Kaggle, el portal web más frecuentado por los científicos de datos. En Kaggle se reproduce la experiencia de Netflix y compañías, organismos de investigación y diversas entidades publican sus datos en competiciones para mejorar sus algoritmos predictivos. El

55

---

<!-- Página 56 -->

efecto que estas competiciones han tenido sobre el desarrollo de los algoritmos de aprendizaje supervisado es difícilmente 11 exagerable. Las grandes compañías de telecomunicaciones, de segu- ros o de banca disponen también de sistemas predictivos para estudiar el comportamiento de sus clientes y anticipar cuándo tienen intención de darse de baja de sus servicios. Los deno- minados sistemas anti-churn elaboran ofertas especializadas para retener clientes que manifiestan síntomas de desconten- to con el servicio. La mayor parte de estos sistemas están ba- sados en algoritmos de aprendizaje supervisado sobre datos estructurados; es decir, aprenden sobre el comportamiento de los clientes para elaborar estrategias comerciales adecua- das a sus objetivos. El conocimiento detallado de las preferencias de consu- mo y hábitos de vida de las personas, captados a través de su interacción con dispositivos electrónicos, supone una infor- mación muy valiosa para el desarrollo de todo tipo de aplica- ciones comerciales. Se podría decir que hoy en día el gigante Amazon ya no es una empresa de logística sino, más bien, una empresa de información cuyo principal valor son los datos recopilados sobre sus clientes y sus algoritmos de IA para extraer valor de ellos. Como se comentará en capítulos posteriores, la industria de la publicidad online, a través del llamado “marketing de precisión”, es uno de los principales motores del desarrollo de algoritmos de IA y ciencia de datos, como se manifiesta a través del complejo ecosistema de empresas que intervienen en el mercado de medios.

11. En opinión de David Donoho, galardonado en 2018 con el premio Gauss de la International Mathematical Union, este tipo de competiciones por una tarea común (common task frameworks) han marcado el desarrollo metodológico en ciencia de datos y su carácter práctico está diferenciando esta disciplina de la estadística tradicional.

56

---

<!-- Página 57 -->

Para saber más

Hemos proporcionado una breve introducción a los concep- tos algorítmicos y metodológicos básicos de la estadística y el aprendizaje automático relevantes para predicción y aprendi- zaje en problemas big data. Existe cierto debate sobre la esen- cia de ambas disciplinas y su rol en la era de la ciencia de datos y la IA (véanse Dunson, 2018; Donoho, 2015, para más información) que hemos soslayado aquí adoptando una pos- tura pragmática. Además nos hemos centrado en métodos basados en maximización de la verosimilitud (tal vez junto a un regularizador) sin hacer referencia a métodos bayesianos descritos en Gelman et al. (2013) y French y Ríos Insua (2000), pues aún no están suficientemente desarrollados para problemas de gran dimensión, salvo a través de las aproxima- ciones variacionales. Pueden verse detalles completos sobre los métodos in- troducidos en Hastie et al. (2009), Bishop (2006) y Good- fellow et al. (2018). Además, son numerosos los cursos dispo- nibles en sistemas como Coursera, Udacity o Udemy.También hay excelente documentación en la librería Scikit-learn de ML de Python, donde muchos de estos métodos están imple- mentados. Los aspectos de visualización pueden verse en tex- tos comoel de Cairo (2012). Es evidente el valor que la recopilación, el tratamiento y el análisis de datos puede aportar a la actividad empresarial y política, y por este motivo existe una fuerte demanda para incorporar personal con perfil de científico de datos a las plantillas de las empresas. Pero también es cierto que algunas prácticas pueden vulnerar la privacidad y plantean problemas éticos y legales, como discutiremos en el capítulo 7. En este punto, cerramos este capítulo con una breve reflexión sobre la IA: ¿es su objetivo aprender y reproducir el comportamien- to racional o el comportamiento humano? Esta cuestión va más allá de los temas que podemos tratar en este libro, pero animamos al lector interesado a reflexionar sobre ella.

57

---

<!-- Página 58 -->

CAPÍTULO 4

## Big data para la política y la Administración

Introducción

Como hemos indicado, un rasgo definitorio de nuestra socie- dad en las últimas décadas ha sido el rápido crecimiento en la capacidad de las empresas para explotar las TIC, la IO y la modelización estadística para recopilar y procesar datos de operaciones y de mercado y respaldar sus procesos de toma de decisiones con modelos adecuados. Por el contrario, si bien en muchos países las decisiones gubernamentales suelen venir respaldadas por métodos tradicionales de análisis de po- líticas públicas, son pocos los departamentos y organismos gu- bernamentales que han logrado implantar de forma sistemática y efectiva las aproximaciones big data descritas. Por simple comparación con las aplicaciones comerciales, no es difícil pre- ver el enorme potencial que espera en problemas asociados a examinar la distribución de los distintos sucesos de salud, al diseño racional de infraestructuras, al uso de conocimiento so- bre el comportamiento de los ciudadanos para promover el ahorro energético, al desarrollo de servicios de administración electrónica o la gestión de ciudades inteligentes. Realizaremos, pues, en este capítulo una reflexión sobre la relevancia del big data en la toma de decisiones públicas. En primer lugar revisamos algunos usos en la Administración

58

---

<!-- Página 59 -->

pública; después presentamos algunas cuestiones relativas a la mercadotecnia política y el problema de las fake news; final- mente, en nuestra discusión presentamos algunas iniciativas relacionadas con organizaciones no gubernamentales y la gestión de crisis humanitarias.

Big data para políticas públicas

El análisis de políticas (policy analysis) es un campo esencial- mente multidisciplinario que, tradicionalmente, ha aportado un marco para reflexionar sobre la toma de decisiones sobre políticas públicas que cubre las etapas típicas del ciclo del aná- lisis de decisiones, incluyendo la contextualización del pro - blema, la determinación de las posibles políticas alternativas; la predicción de sus consecuencias; la valoración de sus resul- tados y la elección de la política a implementar. A menudo se presenta como parte de un ciclo ideal de formulación de po- líticas, representado como un continuo con las siguientes eta- pas generales (Dunn, 1994):

- Establecimiento de la agenda. En la que se determinan las prioridades entre las cuestiones de interés público que requieren una acción política o cambios sobre po- líticas implementadas anteriormente. - Análisis. Dirigido a conseguir una mejor comprensión de un tema que se haya incluido en la agenda. El pro- blema se formula y se desarrollan y evalúan opciones de políticas alternativas para gestionarlo. Se recopila evidencia para aclarar los hechos relevantes y los obje- tivos de los distintos grupos de interés y de los ciuda- danos en general. - Toma de decisiones sobre políticas. Apoyados en el aná- lisis, se adopta una decisión final y se especifica la po- lítica elegida. - Implementación de políticas. Una vez seleccionada, tal política debe hacerse operativa. Para ello se movilizan

59

---

<!-- Página 60 -->

los recursos públicos y reglamentos necesarios para su puesta en marcha. - Monitorización. Se dirige a evaluar de manera con- tinua si la política implementada está produciendo los resultados esperados para identificar si esta debe modificarse o deben considerarse nuevos temas en la agenda.

A pesar de su indudable atractivo, dada su claridad y racionalidad implícita a menudo se critica este ciclo porque raramente refleja lo que ocurre en la realidad, lo que conduce a una variedad de formas de conceptualizar el proceso de for- mación de políticas (Forester, 1993, entre otros). Sin embar- go, las etapas señaladas anteriormente siguen siendo útiles en la práctica para orientar las necesidades y pensar en las dife- rentes formas que el análisis de políticas adopta y los métodos utilizados para implementarlas. Además, se han implantado con éxito por diferentes actores en áreas como la localización y el dimensionamiento de parques de bomberos, la toma de decisiones sobre políticas energéticas, la regulación y el con- trol del tráfico aéreo, la planificación de sistemas nacionales de salud, la asignación de recursos educativos o la planifica- ción del personal militar, por nombrar unos pocos. En cualquier caso, una cuestión crítica en la toma de de- cisiones públicas es determinar los criterios utilizados para evaluar las políticas y quién puede influir en dicha elección. Típicamente reflejan los valores políticos y las prioridades del gobierno correspondiente, sobre lo que subyace una concep- ción particular de lo que se entiende por “valor público” en relación con, por ejemplo, los impactos sobre el bienestar so- cial, el medio ambiente o el desarrollo económico de las deci- siones que se adopten. En particular, la componente de bien- estar social puede verse como la agregación del bienestar de los distintos individuos, con lo que es probable que haya que hacer concesiones entre ellos, así como con otros objetivos ambientales y económicos que, a menudo, conducen a con- flictos entre los diferentes actores. Así, el análisis de políticas

60

---

<!-- Página 61 -->

puede tratar de suavizar tales conflictos buscando opciones que conduzcan a una distribución más equitativa, efectiva y eficiente de bienes, servicios, costes y beneficios entre los miembros de la sociedad. En términos más generales, los objetivos subyacentes a las actividades del análisis de políticas y los roles asociados que los analistas desempeñan en dichos procesos pueden va- riar considerablemente. Así, por ejemplo, no todos los analis- tas buscan diseñar y recomendar de manera objetiva y prag- mática las “mejores opciones” a partir de evaluaciones como las que estamos describiendo en este libro, sino que pueden adoptar roles alternativos de mediación en conflictos sociales, en el apoyo al debate sobre valores y argumentos o en la de- mocratización de los procesos de formulación de políticas. Los roles tradicionales del analista pueden entonces complementarse con las aproximaciones analíticas y de big data como se muestra con los siguientes ejemplos:

- Investigar y analizar datos relevantes para la formu- lación de políticas; por ejemplo, a través de todo tipo de aproximaciones analíticas, desde el análisis explo- ratorio de datos a los métodos de análisis de conglo- merados. - Diseñar y recomendar opciones relevantes para su formulación; por ejemplo, a través de modelos de op- timización de gran escala o de modelos del análisis de decisiones. - Asesorar estratégicamente sobre qué opciones políti- cas podrían ser efectivas; por ejemplo, con ayuda de sensores en tiempo real y modelos dinámicos predic- tivos basados en datos de teléfonos móviles o GPS. - Mediar en conflictos entre diferentes valores y opcio- nes políticas; por ejemplo, con metodologías de plani- ficación e-participativa. - Ayudar a democratizar el proceso político; por ejem- plo, por medio de conferencias de consenso o sistemas de información geográfica participativos.

61

---

<!-- Página 62 -->

- Aclarar los valores y argumentos de diferentes actores en el proceso de formación de políticas; por ejemplo, a través de mapas cognitivos o minería de textos y aná- lisis de sentimientos en redes sociales.

Las técnicas mencionadas son solo ejemplos de catego- rías generales y, a menudo, se utilizarán para el análisis de políticas y el apoyo a su formulación a través de las fases del “ciclo de políticas” e incluyen, entre otras, la minería de tex- tos en la fase de establecimiento de la agenda; la construcción de modelos de análisis multicriterio y simulación para la fase de análisis; los métodos de planificación participativa en la fase de toma de decisiones; los modelos de asignación de re- cursos y optimización en tiempo real en la fase de implemen- tación, y, finalmente, distintos métodos de evaluación como la teledetección para la fase de monitorización. Mencionemos, para concluir, algunos ejemplos de analí- tica de políticas. Así, Scharaschkin y McBride (2016) discu- ten la tarea de cómo evaluar si la implementación de una po- lítica aporta una buena relación de coste-beneficio a la Oficina Nacional de Auditoría del Reino Unido, con ejemplos en re- lación con la regulación financiera, la gestión sanitaria y el desarrollo de recursos humanos para el sector público. Algunas áreas en las que es especialmente relevante la analíti- ca de políticas incluyen la planificación urbana, la planifica- ción energética y la gestión ambiental, a través del concepto de ciudades inteligentes. Un caso relevante se describe en Kumar et al. (2016), que analizan grandes bases de datos sobre las tarjetas de viaje de los usuarios del sistema de bicicleta com- partida en Singapur para mejorar las necesidades de dicho servicio y emplean luego las correspondientes predicciones de uso para encontrar la capacidad óptima de expansión del sis- tema mediante un modelo de optimización a gran escala. Zhang et al. (2016) proporcionan un modelo de equilibrio de mercado para biocombustibles en el estado de Iowa, teniendo en cuenta las necesidades de los agricultores involucrados, los productores y los consumidores de biocombustibles. Su

62

---

<!-- Página 63 -->

formulación conduce a un modelo de teoría de juegos de gran escala que, cuando se alimenta con grandes bases de datos relevantes, proporciona producciones y precios de combusti- ble en el equilibrio. MacKenzie et al. (2016) muestran varios modelos de optimización dinámica de gran escala que facili- tan la asignación de recursos para la recuperación ambiental después de un desastre, ilustrándolo con la gestión de las ope- raciones de limpieza después del vertido asociado al acciden- te de la plataforma Deepwater Horizon. El empleo de estas metodologías para la mejora de los servicios de atención médica es también un área muy impor- tante de aplicación, a la que dedicaremos el capítulo 5. Aquí describimos un par de ejemplos de política pública en esta área. Uno de ellos (Aringhieri et al., 2016) estudia el proble- ma de cómo organizar los servicios médicos de emergencia en la ciudad de Milán; para ello, desarrollan un modelo de simulación a gran escala para el envío de ambulancias y un modelo más estratégico de cálculo del tamaño de la flota de ambulancias necesaria para atender la demanda prevista. Brennan et al. (2016) se ocupan de una cuestión importante de salud pública: los efectos del consumo excesivo de alcohol y la evaluación de las políticas para mitigarlos; para ello, es- tructuran y ajustan un modelo a gran escala del comporta- miento relacionado con el alcohol, valorando sus resultados.

De la mercadotecnia política…

En términos generales, para poder implantar políticas debe- mos ser capaces de acceder al poder. Por ello, en esta sección daremos algunas ideas sobre cómo pueden ayudar las metodo- logías y tecnologías aquí descritas a facilitar la acción política. Una cuestión esencial es hacer llegar los mensajes ade- cuados al electorado, dentro de lo que se denomina “mercado- tecnia política” Este no es un problema nuevo y los partidos han utilizado estrategias variadas con métodos tradicionales como mítines, programas de televisión y de radio, llamadas

63

---

<!-- Página 64 -->

por teléfono, anuncios en periódicos o visitas a domicilio. Sin embargo, las redes sociales han abierto una nueva era en este campo y, en realidad, en la mercadotecnia en general —como describimos en el capítulo 2 y remarcaremos en el capítulo 7—, que nos permite lanzar mensajes mejor adaptados a los distintos perfiles de usuarios de redes sociales para intentar convencerles de las bondades de un candidato, de un progra- ma o de una opción política. Un ejemplo interesante proviene de algunas propuestas incluidas en Alfaro et al. (2016). La idea básica que se persi- gue es determinar qué tipo de palabras y mensajes son los más efectivos sobre un electorado. Para ello se pueden utilizar los comentarios que aparecen en blogs y redes como Twitter en relación con dos o más partidos o candidatos. Podemos conseguirlo combinando algoritmos supervisados de apren- dizaje automático y técnicas de aprendizaje no supervisadas para análisis de opinión y minería de opiniones. Una aproximación relacionada está en la base de la polé- mica reciente sobre la desaparecida Cambridge Analytica. Su aproximación se basa en la capacidad de predicción de rasgos personales a través los likes de usuarios en una red social co- mo Facebook. Para ello se emplearon los datos de 58.000 in- dividuos que, de forma voluntaria, dieron información demo- gráfica (género, edad…) y participaron en un conjunto de tests psicométricos aportando sus likes de Facebook entre más de 56.000 opciones. En primer lugar, se introdujo una aproximación de reducción de la dimensionalidad a cien va- riables, basada en la descomposición de valor singular. Después se introdujeron modelos de regresión lineal o logís- tica para predecir el sexo, la raza o la orientación política de los participantes en función de tales variables. De esa manera, resultó posible predecir los perfiles sociodemográficos de los usuarios en una red social a partir de sus opiniones y adaptar los mensajes que se envían a los mismos, aumentando su im- pacto. El gran revuelo mediático de este caso está sin duda ligado al uso sin consentimiento de datos personales por par- te de Facebook para fines políticos. Sin embargo, existen

64

---

<!-- Página 65 -->

dudas razonables sobre la precisión de la predicción de di- chos perfiles (Rathi, 2018) y los directivos de la compañía (quizás de manera interesada), en su comparecencia ante la comisión del Parlamento británico, admitieron que dicha pre- cisión no superaba el 60% en la mayoría de los casos y solo funcionaba razonablemente bien para usuarios con más de 50 likes, que no superaban el 20% del total.

… a las noticias falsas

Un problema muy relacionado con el anterior es el de las fake news. Esencialmente, se refieren a noticias en forma de artícu- lo, imagen o vídeo que son intencional y verificablemente falsas y se lanzan con el objetivo de manipular a la audiencia con cierto propósito, como que voten a un candidato. En realidad, el fenómeno no es nuevo, siendo incluso tan viejo como la di- cotomía comunicación-información; eso sí, con nuevos aliados estratégicos en las TIC y las redes sociales: el acceso a las ma- sas, la viralidad y la redundancia en el engaño, muy centrada en un periodo breve pero intenso de tiempo. Estos rasgos caracte- rizan las noticias falsas en sus formas más avanzadas, potencia- das por los mínimos costes marginales que conllevan. Así, si unimos todo lo anterior en el marco de una nueva lógica política en la que las TIC y las redes sociales se em- plean como recurso principal en numerosos países, nos en- contramos con la necesidad de enfrentarnos con retos que ponen en riesgo las democracias occidentales tal y como hoy las conocemos. En este sentido, si tuviésemos que señalar el punto de inflexión en el que este fenómeno se convierte en una herramienta política estratégica, deberíamos mencionar necesariamente las elecciones presidenciales del año 2008 en Estado Unidos. Desde entonces no ha habido un solo proceso electoral en países avanzados que no se haya visto sujeto a la toxicidad instrumental de las noticias falsas, destacando las elecciones Trump-Clinton, el referéndum del Brexit o el pro- ceso independentista de Cataluña.

65

---

<!-- Página 66 -->

Así, es la dimensión geopolítica de este fenómeno la que es nueva en relación con las técnicas tradicionales de manipu- lación, que son relativamente estándar en la economía y los negocios. De hecho, estos métodos son frecuentes en las es- trategias recientes de publicidad engañosa dirigida, por ejem- plo, a promover decisiones de compra incluso en casos que ponen en peligro nuestra salud, incluyendo estrategias de ba- ja intensidad como las de nudging (Thaler y Sunstein, 2008), provenientes de la economía del comportamiento. Al fin y al cabo, no olvidemos que la propaganda y la mercadotecnia utilizan metodologías y técnicas de persuasión similares. Así, las herramientas de publicidad engañosa han sido empleadas tradicionalmente por grandes corporaciones y bancos para posicionarse en mercados y ganar confianza entre los ahorra- dores. Incluso, en cierta forma, podríamos decir que hubo mucho de publicidad engañosa y noticias falsas en las raíces de la crisis financiera del 2008, con Bankia como ejemplo principal en España. Obsérvese, sin embargo, que a pesar de tener fallos y no ser muy eficiente, nuestro sistema sociopolítico incluye meca- nismos para enfrentarse a la información tóxica, incluyendo las que conciernen a los periodistas. El problema con las no- ticias falsas en su versión más reciente, y teniendo en cuenta su dimensión geopolítica, es que no se dispone de mecanis- mos en tiempo real para afrontar tales retos, principalmente porque incluso aunque los creadores de tales estrategias sue- len ser personas, frecuentemente se realizan a través de siste- mas automáticos contra los que los sistemas de detección tra- dicionales son esencialmente inútiles. Por ello, se vienen produciendo desde tiempos recientes intentos de automatizar la detección de noticias falsas a través de métodos que se clasifican esencialmente en dos familias: aproximaciones lingüísticas, basadas en el hecho de que la ma- yoría de los mentirosos emplean el lenguaje estratégicamente para evitar ser detectados, de forma que con estos métodos se intentan hallar signos de engaño con patrones dentro de men- sajes, empleando clasificadores sobre representaciones de un

66

---

<!-- Página 67 -->

texto por medio de n-gramas o de bolsas de palabras; y apro- ximaciones en red, que intentan aprovechar la información del comportamiento de difusión del mensaje, por ejemplo, en si- tios de microblogs como Twitter, que trata de detectar rumo- res infundados a través de metadatos tales como hiperenlaces u otras propiedades de grafos y así distinguir fuentes creíbles de otras maliciosas. Para ello, se puede incluir la identifica- ción del usuario que genera el contenido, distinguiendo entre personas o bots. Ambas aproximaciones pueden combinarse, conduciendo a modelos híbridos que se benefician de una mejor representación de los datos dentro de modelos de redes neuronales profundas, combinando métodos de procesa- miento del lenguaje natural y de análisis de redes sociales.

Para saber más

En este capítulo hemos ilustrado cómo las tecnologías y me- todologías big data pueden ayudar en el tratamiento de algu- nos problemas de adopción de políticas públicas. El análisis de políticas es un campo multidisciplinario que se describe en más detalle, por ejemplo, en Mayer et al. (2004) o Fischer et al. (2007). El término de “analítica para políticas” es reciente; Daniell et al. (2016) proporcionan una revisión con ejemplos. Nos gustaría destacar aquí, en nuestro país, los trabajos pio- neros que la Agencia Estatal de Seguridad Aérea ha realizado en analítica de políticas para mejorar sus metodologías de gestión de riesgos en seguridad aérea. Para concluir, es interesante mencionar también el im- pacto que puede tener una adecuada gestión del big data en problemas de logística humanitaria y apoyo a las ONG, sien- do un buen ejemplo los trabajos de la organización Data-Pop 12 Alliance, una coalición global impulsada por Pentland en el MIT Media Lab y la Harvard Humanitarian Initiative para promover los aspectos más humanos en la revolución del big

12. https://datapopalliance.org

67

---

<!-- Página 68 -->

data a través de la investigación, la formación y el análisis de datos para cuestiones referidas al cambio climático, el desa- rrollo sostenible, las migraciones y la salud pública, entre otras. Varios de los casos que han tratado se refieren a la ges- tión de desastres. Cada año, los desastres naturales afectan a cientos de millones de personas, siendo además un problema creciente exacerbado por el cambio climático. El despliegue de los equipos de respuesta de emergencia depende de la dis- ponibilidad de información relevante, como la relativa a los movimientos de la población afectada. El análisis de los regis- tros de llamadas, convenientemente agregados y anonimiza- dos, ofrece posibilidades para caracterizar el comportamiento humano durante sucesos críticos, para mejorar el estableci- miento de alertas tempranas y la gestión de mecanismos de emergencia. 13 Uno de los proyectos de la Data-Pop Alliance es OPAL (Open Algorithms), un consorcio sin ánimo de lucro que in- tegra diversas instituciones y compañías de telecomunicacio- nes y tiene por objeto posibilitar el uso de big data recopilado por compañías privadas para el bien común. Para ello propo- nen soluciones tecnológicas que cambian la forma en que las compañías adquieren y almacenan los datos de los usuarios. La privacidad de los datos, la robustez de la anonimización y el carácter abierto de los algoritmos que operan sobre ellos son algunas de sus señas de identidad. Volveremos sobre esta importante cuestión en el capítulo 7.

13. https://www.opalproject.org/

68

---

<!-- Página 69 -->

CAPÍTULO 5

## Big data en sanidad

Introducción

Hemos hecho ya una introducción a las metodologías y tec- nologías principales del big data e ilustramos algunas de las aplicaciones iniciales en el desarrollo e implantación de polí- ticas públicas. Quizás el campo de la sanidad sea uno en los que el big data y las TIC estén cambiando de manera más perceptible las prácticas profesionales y de planificación. En este capítulo haremos un breve recorrido sobre algunos de los avances más significativos en esta importantísima área.

Diagnóstico y prognosis

El diagnóstico en medicina consiste en atribuir una enferme- dad o una afección como la causa más probable asociada a los síntomas presentados por un paciente para poder determinar en consecuencia el tratamiento más adecuado. La prognosis supone emitir una predicción sobre el comportamiento futuro del paciente a partir del estado observado en la actualidad, uti- lizando el conocimiento adquirido sobre la evolución de otros pacientes con características similares. Tanto el diagnóstico co- mo la prognosis conllevan, en principio, el razonamiento bajo

69

---

<!-- Página 70 -->

incertidumbre. Un paciente se presenta en la consulta descri- biendo un cuadro de síntomas y el facultativo le hace una serie de preguntas encaminadas a recabar información rele- vante para tomar una decisión sobre las acciones a recomen- dar. Además, la historia clínica del paciente contiene informa- ción adicional que puede resultar de utilidad para el diagnóstico. Empleando la evidencia acumulada (pero tam- bién su propia experiencia anterior, su conocimiento experto y tal vez el de otros colegas), el médico, al menos intuitiva- mente, valora las probabilidades de que el paciente padezca las distintas afecciones que podrían explicar tal evidencia. En función de su gravedad y de las probabilidades estimadas puede recomendar la realización de pruebas médicas adicio- nales para reducir la incertidumbre. Estas pruebas pueden ser más o menos invasivas o molestas para el paciente, además de comportar un gasto para el sistema de salud; de ahí la impor- tancia de una buena estimación de los riesgos. Con frecuencia, los médicos de atención primaria mane- jan pequeños modelos o reglas aproximadas que les ayudan a estimar mentalmente tales probabilidades. Por ejemplo, en el tratamiento de enfermedades cardiovasculares, uno de los modelos más aceptados es el Frammingham Risk Score (Wilson et al., 1998), adaptado a las características de la po- blación española en el modelo Regicor (Marrugat et al., 2003). Conociendo la edad del paciente y una serie de varia- bles predictivas como la presión sanguínea, el nivel de coles- terol HDL, el género del paciente o si este es fumador o pa- dece diabetes, el modelo devuelve una puntuación que se traduce en una estimación del riesgo de contraer una enfer- medad cardiovascular en los próximos diez años. Otras enfer- medades tienen sus propios modelos, como el CHADS2- VASc para evaluar el riesgo de accidente cerebro vascular (Lip et al., 2010) o el índice Charlson para evaluar la comor- bilidad debida a diversas causas. Desde un punto de vista es- tadístico, llama la atención la simplicidad de tales modelos: esencialmente son lineales con unas pocas variables y no sue- len tener en cuenta ningún tipo de correlación entre ellas.

70

---

<!-- Página 71 -->

La diferencia entre un modelo tan sencillo como los ín- dices epidemiológicos antes mencionados y un modelo de IA, que toma muchos más datos específicos para cada individuo, probablemente radique en el punto de vista y la utilidad de las correspondientes predicciones. Desde una perspectiva ma- cro, es decir, para los responsables de diseñar una política de salud pública, la predicción puede ser más grosera porque juega a su favor la ley de los grandes números: si a partir de cuatro o cinco indicadores básicos se predicen probabilidades de supervivencia, en algunos casos se fallará por exceso y, en otros, por defecto; pero la predicción en relación con toda la población puede ser correcta al compensarse unos errores con otros. En el diseño de estas políticas se tienen en cuenta las cifras globales y quizás por eso los modelos sencillos pro- porcionan reglas de actuación fácilmente implementables cu- yos efectos son medibles y se pueden evaluar mediante indi- cadores globales. Sin embargo, el asunto cambia cuando se ve desde el punto de vista de un paciente individual al que no debería dejar indiferente si el error de predicción es por exce- so o por defecto. Además, si fuéramos dicho paciente, ¿cómo tendríamos que entender si un médico nos dice que en los siguientes diez años tenemos una probabilidad del 50% de adquirir una enfermedad cardiovascular? ¿Quiere decir que si vivimos 1000 veces, en 500 de ellas habremos contraído la enfermedad? Pero solo vamos a vivir una vez… ¿Quiere decir que si hay 1000 personas iguales que nosotros, 500 de ellas habrán contraído la enfermedad? ¡Pero solo hay una persona exactamente igual! La interpretación frecuentista de la pro- babilidad solo tiene sentido cuando se emiten predicciones sobre grandes poblaciones, pero lo pierde cuando se interpre- 14 ta individualmente. En ese caso, hemos de interpretar tal probabilidad de forma bayesiana, como un grado de creencia en que se produzca cierto hecho. Más allá de este tipo de índices sencillos, desarrollados a partir de estudios concretos, desde hace décadas se están

14. Algunos diríamos siempre.

71

---

<!-- Página 72 -->

aplicando en diagnóstico médico sistemas expertos basados en redes bayesianas (Koller et al., 2009; Pearl, 2014), también llamados “modelos gráficos probabilísticos” (PGM). Estos modelos representan las relaciones de dependencia estadísti- ca de unas variables frente a otras y, en consecuencia, factori- zan la densidad de probabilidad conjunta de todas ellas, de modo que el número de parámetros libres del modelo se man- tenga en una cifra razonable y no incremente exponencialmen- te con el número de variables consideradas. Recordemos, co- mo hemos visto en el capítulo 3, que un modelo no ha de tener más parámetros libres que datos de entrenamiento si queremos mitigar el problema de sobreajuste; es decir, si deseamos garan- tizar que el modelo generalice bien la predicción en casos no vistos previamente. Desde un punto de vista estadístico, el uso de redes bayesianas en inferencia estadística representa de ma- nera mucho más rigurosa el proceso de cuantificación de la incertidumbre respecto a una variable (la enfermedad del pa- ciente) conocidas una serie de evidencias (los síntomas que presenta, los datos de su historia clínica, etc.). El problema de construcción y evaluación de una red bayesiana no es en absoluto sencillo, ya que el conjunto de síntomas y enfermedades pueden no ser mutuamente exclu- yentes. Los parámetros libres del modelo son las probabilida- des condicionadas en cada nodo de la red y se fijan incorpo- rando el conocimiento de expertos; o bien siguiendo un proceso de aprendizaje, ajustando dichos parámetros a los datos observados, o combinando ambas fuentes de informa- ción. El diseño de la estructura de la red se suele hacer con un criterio experto de las relaciones de dependencia entre las va- riables, aunque existen también métodos para aprender dicha estructura a partir de los propios datos. Uno de los primeros ejemplos de aplicación de las redes bayesianas al diagnóstico médico fue el sistema Pathfinder I (Heckerman et al., 1992) para el tratamiento de las enferme- dades asociadas a los nódulos linfáticos. Este sistema experto incluye el diagnóstico de 60 tipos de enfermedades linfáticas que, en este caso, sí se consideraron mutuamente excluyentes,

72

---

<!-- Página 73 -->

tomando como datos de entrada 100 propiedades morfológi- cas de los nódulos obtenidas a partir de estudios de anatomía patológica, y 30 variables con datos clínicos, inmunológicos o de biología molecular relevantes para el diagnóstico. Este tipo de modelos expertos en medicina basados en razonamiento estadístico han recibido mucha atención durante las últimas décadas. Sin embargo, si se dispone de un número suficientemen- te grande de casos correctamente diagnosticados para formar un amplio conjunto de entrenamiento, los modelos basados en aprendizaje profundo que veremos más adelante pueden conseguir resultados más precisos en el diagnóstico, compa- rables o incluso superando la capacidad humana. La diferen- cia fundamental estriba en que, en modelos como Pathfinder, las variables predictivas han sido seleccionadas de manera externa por un patólogo —por ejemplo, el tamaño promedio de las células o la rugosidad de la membrana— y esta selec- ción es la que alimenta como entrada al modelo. Hoy en día se tiende a aplicar modelos end-to-end basados en redes neu- ronales, que toman como entrada la imagen entera sin apenas procesamiento y, a partir de ella, predicen qué tipo de enfer- medad existe. Los modelos de redes neuronales profundas abstraen sus propias variables predictivas como parte de su arquitectura, aunque dichas variables intermedias no sean fá- cilmente interpretables, como sí lo eran las 100 propiedades morfológicas escogidas por el patólogo. Apreciamos aquí otra característica básica del razona- miento probabilístico: la diferencia entre predicción e infe- rencia. La predicción se ocupa solo de evaluar la precisión del diagnóstico, evaluado sobre conjuntos de validación suficien- temente amplios, sin importar la interpretación de las caracte- rísticas que han conducido a dicha predicción y, por tanto, sin capacidad de poder actuar sobre ellas. Los modelos de apren- dizaje profundo conducen a buenos resultados para las tareas de predicción, consiguiendo normalmente rendimientos supe- riores a cualquier otro modelo si se dispone de suficientes da- tos para su entrenamiento. Como vimos en el capítulo 3, esto

73

---

<!-- Página 74 -->

se debe a su gran flexibilidad para aprender distribuciones de probabilidad complejas en alta dimensión. Sin embargo, estos modelos funcionan como cajas negras y no permiten, en ge- neral, extraer conclusiones o recomendaciones sobre cómo actuar sobre las variables para obtener una variación de las probabilidades predichas en el sentido deseado. Los modelos basados en redes bayesianas permiten hacer inferencia: son interpretables y aportan una representación adecuada del co- nocimiento experto y su incertidumbre asociados a una situa- ción. Dependiendo de la misma se habrá de favorecer la pre- dicción o la inferencia. Si la tarea que nos incumbe consiste en tomar una imagen médica de una escisión tumoral y clasificar correctamente el tipo de tumor, el modelo con mayor preci- sión en la predicción será el más útil, sin importar cómo se ha llegado a dicha conclusión. Por el contrario, si la tarea consiste en razonar sobre una serie de propiedades de un paciente (concentración de colesterol, triglicéridos, hemoglobina, etc.) y su relación con la probabilidad de desarrollar una afección determinada, no nos basta con que la predicción sea adecua- da, sino que desearemos entender el papel de cada variable para actuar sobre ellas con ayuda del tratamiento adecuado. La revolución de la IA está teniendo efectos drásticos sobre el mercado de trabajo a través de la automatización de las tareas más mecanizables. No parece que sea ese el caso de los profesionales de la atención sanitaria, pero es cierto que la inclusión progresiva de elementos de IA en la práctica médica modificará las tareas de los facultativos, que podrán delegar algunas de ellas a sistemas inteligentes y concentrar su atención en realizar las de mayor nivel. Probablemente no veremos en un futuro muy cercano robots médicos cuando vayamos a nuestro centro de salud; sin embargo, una parte importante del filtrado en atención primaria se puede realizar ya a través de chatbots, sistemas de diálogo automático que, a través de un chat en el teléfono móvil, orientan al paciente a través de preguntas y respuestas, proporcionando informa- ción y recomendando las mejores medidas a adoptar. Es evi- dente que un profesional de la salud llega mucho más lejos

74

---

<!-- Página 75 -->

que cualquier sistema automático al evaluar esa información difícilmente cuantificable, usando lo que podríamos llamar su “ojo clínico”: el paciente tiene mala cara, no me está diciendo la verdad porque viene con un familiar, etc. El sentido común y los aspectos psicológicos y emocionales de la medicina ha- cen imprescindible el contacto y la atención humana. Sin em- bargo, la capacidad de razonar a partir de casos observados, gestionando simultáneamente multitud de factores y cono- ciendo toda la literatura y estudios clínicos realizados es evi- dente que son tareas que pueden realizar sistemas de IA y que, cada vez, aportarán más una asistencia en la ayuda a la toma de decisiones por parte de los profesionales médicos. En algunas ocasiones, un sistema de IA podrá reempla- zar una consulta médica. Pongamos un ejemplo: descubrimos una mañana una manchita un poco rara en la piel y nos gus- taría saber si es un lunar inofensivo o, por el contrario, un melanoma que requiera tratamiento médico. En la actualidad pediríamos cita en el sistema de atención primaria y, en unos pocos días, acudiríamos al centro de salud a ver al médico de familia. En casos muy obvios, el médico diagnosticará tras ver la mancha; sin embargo, en muchos otros, y principalmente para tener la certeza, nos derivará al dermatólogo, que nos dará cita para dentro de cierto tiempo, pongamos un mes. Tras pasar por su consulta, mirará la mancha y nos dirá de qué se trata. Los tumores cutáneos afectan a 76.000 personas en España y se han duplicado en los últimos 30 años. La ma- yor parte de la gente no acude al dermatólogo para revisar sus lunares y, sin embargo, la detección temprana de melanomas es esencial para su tratamiento eficaz. En muy poco tiempo dis- pondremos de una aplicación en el móvil en la que podremos hacer una foto del lunar y nos dirá inmediatamente su estima- ción sobre qué se trata. El equipo del doctor Esteva en Stanford, en colaboración con el grupo del profesor Thrun, ha desarro- llado un clasificador basado en las mismas redes convolutivas profundas que ganan las competiciones de ImageNet (en par- ticular, la red Inception v3). El clasificador logra resultados de diagnóstico más precisos que los dermatólogos humanos

75

---

<!-- Página 76 -->

(Esteva et al., 2017) y realiza una predicción end-to-end to- mando como entrada los píxeles de la foto y proporcionando como salida la etiqueta de la enfermedad.

Ampliando la base estadística

El modelo para clasificación de tumores cutáneos se entrenó con 130.000 imágenes correctamente catalogadas mediante anatomía patológica. Este número es 100 veces menor que los 14 millones de imágenes catalogadas en 1.000 categorías 15 de la base de datos ImageNet, pero 100 veces mayor que el estudio más amplio en tumores cutáneos realizado hasta la fecha. Pone de manifiesto la necesidad, ya mencionada, de disponer de conjuntos de datos correctamente anotados lo más amplios posibles para el entrenamiento de modelos de aprendizaje automático, especialmente en imagen médica. Efectivamente, cuanto mayor sea el número de casos en un estudio, tanto más fiables serán sus conclusiones. Como hemos visto en el capítulo 3, el rendimiento de los clasificado- res crece con el tamaño del conjunto de entrenamiento, espe- cialmente en el caso de modelos muy flexibles como las redes profundas. En otros sectores, como hemos discutido a lo largo de otros capítulos, las compañías recopilan datos de forma muy ingeniosa, con frecuencia ofreciendo servicios gratuitos a los usuarios a cambio de datos con los que entrenar sus mode- los. En el caso de los datos de salud, se requiere de manera necesaria una cooperación entre instituciones públicas para compartir pruebas diagnósticas e historias clínicas del mayor número posible de pacientes. Esto conlleva retos en varias di- recciones. En primer lugar, un importante reto técnico se debe

15. Sin embargo, no se comienza el modelo con una red desde cero, sino que de partida se toma una red profunda ya entrenada en clasificación con 15 millones de imágenes y, manteniendo los mismos pesos, se recalculan solo los pesos de las capas más superficiales para la tarea específica (clasificación de tumores). Esto se conoce como “aprendizaje por transferencia” (transfer learning) y permite aprovechar el trabajo previo en la abstracción de características de bajo nivel para la interpretación de imágenes.

76

---

<!-- Página 77 -->

a la inexistencia de un formato estándar para las historias clí- nicas a nivel global; a pesar de los esfuerzos y millones de lí- neas de código escritas por Microsoft, Google y, más recien- temente, Apple, ninguna compañía ha conseguido estandarizar el formato para el intercambio de historias clínicas (EHR, Electronic Health Records) y la situación sigue siendo una torre de Babel con muchos sistemas que no se entienden en- tre sí. En España, al tener un sistema sanitario público más o menos centralizado, la situación es ligeramente mejor, pues el proyecto Historia Clínica Digital del Sistema Nacional de Salud ha conseguido, en el momento de escribir estas líneas, que las comunidades autónomas, con la excepción de Cataluña, compartan algún documento de la historia clínica. Los documentos compartidos, en número superior a 200 mi- llones, son principalmente la historia clínica resumida, mien- tras que los resultados de pruebas de laboratorio o imágenes médicas son solo compartidos, de momento, por seis de ellas (HCDSNS, 2019). Además, las dificultades no son puramente técnicas, sino también de índole económica, legal o política. Sin embargo, existe una percepción creciente de la importancia de compar- tir datos médicos sobre una base amplia, no solo para garan- tizar la atención médica de personas desplazadas respecto de su residencia habitual, sino para posibilitar la realización de estudios estadísticos sobre enfermedades específicas. En el caso del cáncer, por ejemplo, que concentra una proporción importante de recursos, la iniciativa Genomic Data Commons 16 del NIH estadounidenseagrupa ya más de 30.000 genomas secuenciados para acceso público de los investigadores. Otros estudios específicos han conseguido reunir diferentes centros para crear una base de datos lo más grande posible y la han puesto al servicio de la comunidad investigadora a través de competiciones, en algunos casos con cuantiosos premios para los equipos con mejores resultados. Un ejemplo es la compe- tición lanzada en la plataforma Kaggle para la detección de

16. https://gdc.cancer.gov/

77

---

<!-- Página 78 -->

cáncer de pulmón a partir de imágenes de tomografía axial de la cavidad pulmonar, siendo el objetivo la predicción de que el paciente fuera diagnosticado con cáncer de pulmón en el año siguiente a la realización de la prueba, con datos verifica- dos mediante anatomía patológica. En la ella participaron 400 equipos y fue patrocinada por Amazon AWS, NVIDIA y parte de la Data Science Bowl, una competición anual en ciencia de datos que ha dedicado sus últimas tres ediciones a problemas en biomedicina.

Aprendizaje profundo para diagnóstico por imágenes

Como se ha mencionado, uno de los impactos más inmedia- tos de la IA y la ciencia de datos se está produciendo en las especialidades de radiología y anatomía patológica gracias a la mejora en las tareas de clasificación y segmentación de imágenes con ayuda de redes convolutivas, un tipo de redes neuronales profundas adaptadas al procesamiento de imáge- nes. La labor de un patólogo consiste fundamentalmente en estudiar imágenes al microscopio de muestras obtenidas por biopsia y determinar si se corresponden a tejido sano o no y, en el segundo caso, clasificar el tipo de tumor. También sue- len determinar si los bordes de una escisión están libres de tejido tumoral y, por tanto, han de localizar dentro de cada imagen qué tejido es sano y cual no. Estas tareas se conocen como “clasificación de imágenes” y “segmentación de obje- tos en visión artificial”. Los algoritmos actuales basados en redes convolutivas profundas presentan ya, en tareas de reco- nocimiento más convencionales como las del ImageNet Large Scale Visual Recognition Challenge (ILSVRC), rendimientos superiores a la capacidad humana. Usando estos modelos con una base de datos suficiente- mente grande de imágenes médicas correctamente cataloga- das, y aplicando aprendizaje por transferencia, se están de - sarrollando clasificadores automáticos para apoyar la labor de los patólogos y radiólogos. Por ejemplo, para la detección

78

---

<!-- Página 79 -->

de metástasis de cáncer de mama en nódulos linfáticos, cinco hospitales holandeses han coordinado recursos para reunir 17 mil imágenes y organizar el Camelyon Grand Challengepa- ra resolver un problema de segmentación de imágenes para el reconocimiento de tejido tumoral. La importancia de auto- matizar la realización de esta tarea puede cambiar el trata- miento quirúrgico de esta enfermedad. En la actualidad, tras la detección de un tumor y una operación para extraer la zona afectada, se envían los resultados de la biopsia a un patólogo para determinar si los bordes están limpios y todo el tumor ha sido correctamente extraído. En caso contrario, ha de reali- 18 zarse una segunda intervención. Una empresa suizaha de- sarrollado un escáner histológico que permite al cirujano ob- servar un tejido recién resecado y determinar en tiempo real durante la intervención si todo el tumor ha sido extraído antes de cerrar la herida. Ante la imposibilidad de tener un patólo- go presente en cada operación, un software de IA aplicando resultados similares a los de la competición anterior haría esta tarea. Es importante señalar que esto no sustituirá las pruebas patológicas, pero dotará al cirujano de mayor control e infor- mación sobre el resultado de la operación mientras esta se desarrolla y logrará que la intervención sea menos invasiva para el paciente. Junto a los ya mencionados estudios sobre diagnóstico automático de cáncer de la piel sobre fotografías y de detec- ción de metástasis de cáncer de mama sobre imágenes histo- lógicas, otros ejemplos recientes de aplicación del aprendizaje profundo a diagnóstico por imágenes incluyen:

- La distinción entre zonas de radionecrosis y tumores cerebrales en imágenes por resonancia magnética. - La detección y medida de aneurismas cerebrales. - El diagnóstico de edemas, enfisemas y otras enferme- dades en imágenes de radiografía torácica.

17. https://camelyon17.grand-challenge.org/ 18. https://samantree.com/product/

79

---

<!-- Página 80 -->

Naturalmente, las empresas no permanecen ajenas a es- tos desarrollos y están ya convirtiendo la patología computa- cional en una realidad: desde pequeñas startups nacidas de la 19 labor de investigadores como PathAIhasta grandes corpo- 20 raciones como Google, NVIDIA o Phillips, entre otras.

Sensores portátiles, redes sociales y salud pública

El desarrollo de sensores de tamaño reducido y bajo consu- mo, junto a su interconectividad, está dado lugar a una serie de dispositivos destinados a ser llevados en todo momento como una prenda más de vestir, a veces incluso como exten- sión de nuestro cuerpo. Son los denominados dispositivos portátiles (wearables). Su versión más conocida son las pulse- ras y relojes de actividad que monitorizan constantemente nuestros hábitos de actividad física, desde el número de pasos que damos hasta las horas de sueño, nuestro ritmo cardíaco o las calorías consumidas, pero las posibilidades son mucho más amplias (figura 5). Los dispositivos portátiles pueden medir la actividad muscular con un electromiógrafo incorporado a la ropa (Finni, 2007), la actividad física y los patrones de sueño a través de un acelerómetro instalado en el reloj (Yang, 2010), el estrés con un sensor electrodérmico en una pulsera (Sandulescu, 2015) o el ciclo menstrual monitorizando la temperatura (Rollason, 2014). Además, se pueden medir los niveles de atención mental con un pequeño número de elec- trodos EEG sin necesidad de gel (Poltavski, 2015) o los nive- les de interacción social, muy importantes para la depresión y otras enfermedades mentales, a través de sensores de proxi- midad mediante conexión bluetooth (Eagle, 2009).

19. https://www.pathai.com/ 20. https://www.usa.philips.com/healthcare/solutions/pathology

80

---

<!-- Página 81 -->

Figura 5 Dispositivos portátiles y propiedades que son capaces de medir.

AcelerómetroCintas para la cabeza Altímetro

Cámara digital Parches Electrocardiograma

Electromiograma

ElectroencefalogramaCámaras

Electrodermatógrafo

Posición GPS Relojes inteligentes Micrófono

Oxímetro

Bluetooth proximidadSensores insertados en la ropa

Presión

Termómetro

Estos dispositivos proporcionan información personali- zada en tiempo real, con alertas orientadas a objetivos, y tie- nen una larga vida útil debido a su bajo consumo. En la actua- lidad, muchos de ellos precisan de un smartphone para el procesamiento de los datos pero, en un futuro próximo, toda la funcionalidad de cálculo se integrará en los propios dispo- sitivos. Hay además otros en fase de desarrollo o en proceso de aprobación por la FDA, la agencia americana responsable de la regulación de alimentos y medicamentos. Algunos que ya empiezan a anunciarse en el mercado incluyen:

- Sensores en la espalda para ergonomía y corrección postural. - Sensores de calidad en el aire incorporados a inhala- dores.

81

---

<!-- Página 82 -->

- ECG y monitorización continua del ritmo cardiaco para detección de fibrilación atrial. - Gafas inteligentes con cámara incorporada y servicio de asistencia para invidentes. - Parches digitales desechables para la monitorización continua de temperatura en bebés. - Sensores para registrar la exposición a radiación ul- travioleta. - Electrodos para aliviar el dolor crónico. - Parches cutáneos que detectan cambios en la tempe- ratura para la detección temprana no invasiva del cán- cer de mama. - Lentillas con sensores para medir la glucosa en las lá- grimas, para el seguimiento de la diabetes. - Dispositivos digitales ingeribles: píldoras fabricadas en torno a sensores del tamaño de un grano de pi- mienta que se activan al contacto con los jugos gástri- cos y emiten información (esencialmente una confir- mación de que el paciente ha tomado la medicación).

La lista parece no tener fin y, más allá de la evidente de- mostración del ingenio humano y el afán de las compañías por conquistar nuevos mercados, cabe hacerse una serie de preguntas. La primera de ellas es si las mediciones de estos dispositivos son realmente fiables (al nivel de los estándares de instrumentación médica) o, por el contrario, han de ser considerados como meros gadgets electrónicos, poco más que juguetes para el mercado de consumo. En segundo lugar, es razonable que cuestionemos si el empleo que los usuarios ha- cen de la información recibida es positivo o negativo para su salud y les acerca a los objetivos para los que los adquirieron. Igualmente, podemos preguntarnos por el uso que hacen las compañías fabricantes de la información recopilada de todos los dispositivos conectados, almacenada en sus servidores. Respecto a la fiabilidad de las medidas, cabe distinguir entre dispositivos de monitorización de la actividad, como pulseras y relojes inteligentes, y otros sensores destinados a

82

---

<!-- Página 83 -->

pacientes con enfermedades crónicas. Los primeros están di- rigidos fundamentalmente a promover un cambio de hábito para llevar una vida más saludable, fin que persiguen a través de objetivos, gamificación e interacción con redes sociales. Sin embargo, está comprobado que las personas que com- pran principalmente este tipo de gadgets son de por sí las que tienen hábitos más desarrollados de actividad física y alimen- tan su actividad con información para cuantificar cada pe- queño esfuerzo o avance, como describe el movimiento 21 Quantified Self. Además de existir variaciones considera- bles entre las medidas de actividad realizadas por diferentes dispositivos, la evidencia de los pocos estudios científicos rea- lizados hasta la fecha no es concluyente sobre sus potenciales beneficios: el 50% de los compradores abandonan el disposi- tivo durante el primer año de uso y no está comprobado que dichos dispositivos mejoren la calidad del sueño. En los dis- positivos orientados a medir parámetros fisiológicos para mo- nitorizar pacientes crónicos, el nivel de precisión de las medi- das está sujeto a un fuerte control por parte de la FDA americana, que también regula las aplicaciones que se distri- buyen en los marketplaces de Apple y de Android. Cabe espe- rar, por tanto, que se comercialicen dispositivos y aplicacio- nes que mantengan unos estándares mínimos de fiabilidad. Sin embargo, la fuerte presión de las compañías tecnológicas, al igual que las farmacéuticas, siempre nos hace albergar al- guna duda, dado el inmenso mercado e intereses económicos alrededor del mismo. Como ejemplo, la FDA ha permitido a Apple incluir en su smartwatch dos funcionalidades para me- dir el ritmo cardiaco y alertar de anormalidades en el pulso, pero impone que dicha funcionalidad no debe ser utilizada por personas menores de 22 años ni pacientes que hayan su- frido fibrilación atrial: su uso está aprobado fundamental- mente para personas sanas. Las Google Smart Lenses, lenti- llas que miden el contenido de glucosa en las lágrimas para control de diabetes, por ejemplo, son un proyecto que no se

21. http://quantifiedself.com/

83

---

<!-- Página 84 -->

ha continuado debido a que el contenido de glucosa en lágri- mas presenta baja correlación con la glucosa en sangre. La app para medición de la fase del ciclo menstrual que se co- mercializa en el marketplace de Android por 80 dólares al año ha sido aprobada por la FDA y por las autoridades europeas en febrero de 2018, pero ha recibido numerosas denuncias de embarazos no deseados que ponen en duda los niveles de efi- cacia de control de la natalidad declarados por la compañía. ¿Qué podemos afirmar entonces respecto a la efectivi- dad de estos dispositivos? Al estar en una fase inicial de de- sarrollo, son muchos los proyectos y compañías que luchan por conseguir convertirse en el estándar en cada sector y, naturalmente, muchos de ellos están en fase de perfecciona- miento. Independientemente de la fiabilidad de las medidas, los especialistas alertan del riesgo de autodiagnóstico reali- zado a partir de la información adquirida a través de estos dispositivos, fenómeno que ya se da en pacientes que acu- den a la consulta con una enfermedad autodiagnosticada tras búsquedas en internet, a veces incluso con petición ex- presa de que el profesional les recete el medicamento que ellos han determinado. Pero quizás el verdadero interés de la información reco- pilada por los dispositivos móviles no reside tanto en el uso individual que cada usuario hace de ella, sino en las posibili- dades de estudios científicos y el avance en el conocimiento que abre su tratamiento colectivo. En salud pública, el tener acceso a tanta información personalizada sobre los hábitos de actividad, sueño y parámetros fisiológicos —aunque dicha in- formación sea ruidosa por mediciones imperfectas— supone un recurso muy valioso para monitorizar el estado de salud de la población. Podemos, de hecho, citar los siguientes ejem- plos de estudios concretos:

- Se está desarrollando un proyecto de crowdsourcing gracias a la instalación de GPS y sensores para medir la calidad del aire en inhaladores, facilitando estudios de incidencia del asma en función de la polución, que

84

---

<!-- Página 85 -->

utilizan datos sobre la frecuencia de uso del inhalador, la posición y la calidad del aire en ese punto. - La iniciativa PPD-ACT, promovida por un consor- cio de más de 30 investigadores en siete países, tiene como objetivo el estudio de la predisposición genética a la depresión posparto e incluye una app para reca- bar información a través de preguntas y el envío de un kit para recopilar muestras de saliva. - El proyecto Epi Watch de la Universidad Johns Hop - kins recopila información sobre episodios de epilepsia medidos a través del acelerómetro y giroscopio de un smartwatch, con una app con juegos para evaluar el impacto tras un episodio y trazar la influencia de la medicación y el ritmo cardiaco.

Otros proyectos de recopilación de información a través de dispositivos digitales para estudios clínicos están enfoca- dos a la enfermedad de Parkinson (mPower), la diabetes (GlucoSuccess), la Hepatitis C (C Tracker) o el tratamiento del autismo (Autism & beyond). Todos ellos se integran den- tro de la plataforma Research Kit de Apple, que está apostan- do fuertemente por consolidar su posición en el mercado de las TIC aplicadas a la salud. Al aumentar en varios órdenes de magnitud la base estadística para estos estudios, por las faci- lidades introducidas para la recogida de datos, es evidente que muchos de ellos tendrán un alto impacto en nuestra ca- pacidad de generar nuevo conocimiento. Un aspecto que —probablemente debido al rápido desa- rrollo requerido por el mercado de consumo— no está te- niendo suficiente atención en los dispositivos wearables es el referido a la seguridad en el almacenamiento y tratamiento de la información. Suele hacerse sin encriptación, permitiendo el acceso físico; pero, además, siendo dispositivos conectados, dichos datos podrían ser comprometidos para realizar cual- quier actividad de espionaje, seguimiento, etc. Aunque la in- formación de cada usuario en las bases de datos de los fabri- cantes se haga de manera anónima sin incluir datos personales,

85

---

<!-- Página 86 -->

es importante resaltar que la mera sustitución del nombre por un código de usuario no suele proporcionar una anonimiza- ción robusta (De Montjoye, 2015) y permite identificar al individuo, lo cual tiene especial repercusión al ser los datos de salud particularmente sensibles. Rizando el rizo, unos investi- gadores han demostrado que las mediciones del acelerómetro y giroscopio de una pulsera de actividad son suficientes para reconstruir el movimiento de la mano al insertar un código pin de seguridad (Wang et al., 2016). También se están explorando en el ámbito de la salud las posibilidades que abre el análisis de la información escrita a través de procesamiento de lenguaje natural. Hace unos años, Google puso en marcha el servicio Google Flu Trends, que escaneaba las búsquedas con términos relacionados con la gripe para así adelantarse a los brotes estacionales (Ginsberg, 2009) y facilitar las campañas de vacunación. Algunas inicia- tivas similares se están empleando para la detección de movi- mientos sísmicos y monitorizar las redes sociales como flujo continuo e incesante de información (nowcasting). Las pre- dicciones de Google Flu Trends ya no se hacen públicas des- de 2015 al descubrirse, tras algunos estudios, que tenían ten- dencia a sobrestimar el número de casos, pero la colaboración con grupos de investigación para afinar las predicciones sigue vigente. En general, la información contenida en el lenguaje natural que producen las redes sociales es altamente ruidosa, pero en los próximos años se espera que mejoren las herra- mientas capaces de extraer, filtrar y analizar la información relevante para estudios en epidemiología y salud pública, co- mo ya se está haciendo en otros sectores. Otras aplicaciones del PLN en el ámbito de la salud se referirían a la realización de predicciones de reingreso a partir de los informes de alta, lo que permite planificar recursos en los hospitales, o los ya citados chatbots para filtros de atención primaria. Por último, aunque no está directamente relacionado con big data, sino con TIC en general, querríamos mencionar algunos de los avances que se están desarrollando en teleme- dicina, que permiten que la atención sanitaria llegue a zonas

86

---

<!-- Página 87 -->

remotas usando los avances en comunicaciones digitales. Un ejemplo de programa piloto es el desarrollado por Novartis y el servicio de salud de Ghana en colaboración con empresas globales de telecomunicaciones, universidades y ONG. El pilo- to abarcó 30 comunidades rurales conectando a 35.000 perso- nas con un centro de consulta telefónica atendido por profesio- nales, proporcionando acceso digital durante las 24 horas del día. El éxito de este programa piloto ha propiciado su extensión al resto del país y demuestra que disponemos ya de la tecnolo- gía necesaria para acercar la atención médica a zonas remotas. La telemedicina puede ser clave para ampliar la cobertura de salud universal, uno de los principales requisitos de los denomi- nados Objetivos de Desarrollo Sostenible de la ONU. Pero no solo en atención primaria; también se realizan ya cirugías lapa- roscópicas con robots conectados a internet controlados por un cirujano a miles de kilómetros del paciente, usando una tecno- logía inicialmente concebida para operar a astronautas en el es- pacio. Este tipo de intervenciones abren inmensas posibilida- des, aunque ahora mismo se encuentran limitadas por la ausencia de una normativa al respecto dadas las dudas sobre qué legislación se aplicaría en caso de que algo saliera mal.

Para saber más

Una discusión breve y certera sobre cómo las tecnologías vin- culadas al big data y la IA están influyendo en la medicina clínica puede leerse en la prestigiosa revista New England Journal of Medicine (Obermeyer, 2016). A pesar de que el aprendizaje profundo es relativamente reciente, su impacto y nivel de actividad en imagen médica ha sido tan grande que ya existen varias revisiones de la literatu- ra (por ejemplo, Shen et al., 2017) donde el lector interesado encontrará además una discusión sobre las implicaciones de estos algoritmos en anatomía patológica. Desde el punto de vista de la implantación de disposi - tivos móviles y tecnología digital en la práctica médica, es

87

---

<!-- Página 88 -->

interesante consultar el informe realizado por la consultora Cello Health (Mannu, 2015). Aunque se trata de un informe preparado para analizar las necesidades de la industria farma- céutica en relación con las tecnologías digitales, contiene datos recopilados de una encuesta realizada a 1.000 profesionales en ocho países. Una discusión técnica más rigurosa desde el pun- to de vista científico se puede consultar en Piwek, (2016). A pesar de haber cubierto un buen número de desarro- llos recientes dejamos también numerosos temas en el tintero, lo cual es una evidencia más del vertiginoso ritmo y la ampli- tud de aplicación de las TIC, la ciencia de datos y la IA en ciencias de la salud. Por ejemplo, apenas hemos mencionado la investigación genómica, que hace un uso intensivo de datos de expresión genética y la IA para el desarrollo de nuevos fármacos especialmente diseñados para un individuo especí- fico a partir de su respuesta esperada (medicina genómica personalizada). En los mecanismos para garantizar la seguri- dad e integridad de los datos médicos compartidos no hemos mencionado los muchos proyectos encaminados a aplicar las cadenas de bloques (blockchain) en el ámbito sanitario, ni tampoco el papel que, respecto de las nuevas fuentes de in- formación, jugarán las mutuas y aseguradoras médicas.

88

---

<!-- Página 89 -->

CAPÍTULO 6

## Big data y ciberseguridad

Introducción

Como hemos indicado, un rasgo definitorio de nuestra socie- dad, y también en gran medida origen del fenómeno big data que nos interesa en este libro, es su casi ubicua digitalización. Esta se refleja en los sistemas de información, que almacenan datos confidenciales sumamente valiosos; en las redes socia- les, que reflejan una parte importante de nuestra actividad personal privada; en los sistemas ciberfísicos, que controlan industrias, vehículos o infraestructuras críticas, o en los servi- cios electrónicos de compra, de banca o de administración, por mencionar unos pocos ejemplos. En este estado de cosas, todo tipo de organizaciones, desde las grandes corporaciones a los gobiernos, pasando por las pymes conectadas y las familias, pueden quedar fuertemente impactadas por ciberataques. De hecho, los efectos económicos de estas amenazas son considerables y, en consecuencia, la ci- berseguridad se ha convertido en una cuestión de importancia máxima, tanto técnica como financieramente: se percibe de ma- nera creciente como una amenaza global como, por ejemplo, se destaca en la Estrategia de Seguridad Nacional 2019. Realizaremos pues, en este capítulo, una reflexión sobre la relevancia del big data para ayudar a resolver uno de los

89

---

<!-- Página 90 -->

mayores problemas sociales al que nos enfrentamos en la ac- tualidad: el referido a la ciberseguridad. Tras contextualizar la cuestión desde una perspectiva económica, haremos una bre- ve revisión crítica de los marcos actuales para promover la ciberseguridad. Después presentamos tres casos reales de aplicaciones de big data en ese campo.

Ciberseguridad: algo de contexto

Numerosas fuentes de información explican cómo los cibera- taques están aumentando en frecuencia, impacto y sofistica- ción. Por ejemplo, se estima que tal tipo de ataques produje- ron globalmente unos costes de cerca de 450 billones de dólares en 2016, causando un impacto sobre el PIB global (0,8% en 2014) similar en magnitud al del tráfico de drogas (0,9%) o al del crimen internacional tradicional (1,2%) (McAfee, 2017). Existen incluso mercados negros florecien- tes en la dark web en los que se intercambian herramientas de ataque o información robada, lo que crea incentivos para que personas y organizaciones suficientemente capacitadas y ha- bilidosas desarrollen nuevos productos y servicios para per- petrar ciberataques. Aunque algunos expertos critican que, en cierta forma, se esté dando un bombo excesivo al potencial disruptivo de un ciberataque a escala global, la ciberseguri- dad es un problema muy relevante debido a la cada vez ma- yor persistencia, frecuencia y variedad de las ciberamenazas. Tal diversidad puede clasificarse de acuerdo con la moti- vación, la capacidad y las restricciones de los potenciales ata- cantes, así como por su potencial para explotar, descubrir o crear vulnerabilidades en los sistemas objetivos de los ataques. Las amenazas más temibles provienen de las unidades ciber- militares de las potencias globales, aunque estas vienen cierta- mente restringidas por sus posibles repercusiones militares, económicas y políticas en el contexto internacional. Otro ori- gen de amenazas, ligado en ocasiones a movimientos sociales, es el de los hacktivistas, un perfil muy amplio que incluye a

90

---

<!-- Página 91 -->

hackers que tratan de demostrar sus habilidades con actividades que bordean en ocasiones el terrorismo. Los atacantes internos constituyen otra importante fuente de amenazas —de hecho, la mayor—, pero, en principio, también son los más fáciles de ges- tionar a través de un buen programa interno de ciberseguridad adaptado a los estándares. Además, hay grupos cibercriminales centrados en obtener beneficios económicos con docenas de hackers como empleados y potentes recursos económicos para realizar ataques, tanto dirigidos como no dirigidos. Un tipo muy relevante de ataque se realiza con ayuda de malware, término con el que normalmente designamos al soft- ware desarrollado con el objetivo de atacar a un sistema de in- formación. El concepto de “amenaza persistente avanzada” ha surgido recientemente para designar ataques muy sofisticados consistentes en operaciones pacientemente orquestadas que buscan permanecer escondidas hasta que consolidan un cami- no para alcanzar su objetivo final. Algunos casos importantes incluyen la Operación Aurora, dirigida en 2007 contra Google para obtener datos confidenciales sobre sus algoritmos y sobre disidentes chinos, o Shamoon, que destruyó cerca de 30.000 ordenadores de Aramco en el año 2012. También hay ataques con importantes consecuencias físicas como el Stuxnet de 2010, que ralentizó la industria nuclear iraní durante un tiem- po, o el ataque contra la industria siderúrgica alemana en 2014 que, como consecuencia, tuvo que parar sus operaciones de forma generalizada. Otra tendencia notable en los últimos años han sido los ataques indiscriminados basados en ransomware, como Wannacry y NotPetya en 2017, que afectaron a miles de organizaciones, grandes y pequeñas, durante varias horas. Además, este será un problema cada vez más importan- te, pues numerosos elementos como los coches, los aviones, los sistemas médicos, los sistemas de inversión, abundantes infraestructuras críticas o los sistemas de votación van estan- do cada vez más influidos por las TIC, habiendo cada vez más sistemas interconectados a través del internet de las cosas. Exploramos aquí como las metodologías y tecnologías de big data pueden ayudar en la resolución de estos problemas.

91

---

<!-- Página 92 -->

Previamente describimos algunas metodologías estándar de ciberseguridad.

Metodologías para la ciberseguridad

El análisis de riesgos es una disciplina fundamental para la ciberseguridad. Con ella, las organizaciones pueden evaluar los riesgos que afectan a sus activos y qué contramedidas adoptar para reducir la probabilidad de que se materialicen y así mitigar su impacto en caso de que se produzcan. Existen numerosos marcos para discriminar los riesgos de ciberseguri- dad y apoyar la asignación de sus recursos, incluyendo los re- cogidos en ISO 27005, NIST SP 800-30, CORAS, CRAMM, EBIOS, ISAMM, Magerit, MEHARI o ISO 31000, entre al- gunos otros. Análogamente, hay diversos marcos de control de cumplimiento como ISO 27001, Common Criteria, ISO 27002, SANS Critical Security Controls, las leyes de protec- ción de datos como la reciente RGPD, ISO 27031 o Cloud Security Alliance Cloud Control Matrix que, esencialmente, proporcionan guías sobre la implantación de mejores prácticas en ciberseguridad, incluyendo descripciones de las medidas de seguridad a adoptar para proteger los activos de una organiza- ción frente a las ciberamenazas a las que están expuestos. Resulta interesante hacer una breve descripción del mar- co disponible más extenso, el NIST SP 800-30. Abarca pro- cesos referidos a las distintas funciones de la ciberseguridad que comprenden la identificación de amenazas (principal- mente desde una perspectiva táctico-estratégica de evalua- ción y gestión de riesgos), la protección frente a ellas (princi- palmente a través de actividades preventivas que incluyen, entre otras, el control de accesos y el uso de tecnologías de protección), su detección (por medio, entre otros, de la moni- torización continua de la seguridad y de procesos de detec- ción de sucesos y anomalías) y la respuesta y recuperación frente a las mismas (incluyendo su planificación y los corres- pondientes procesos de comunicación).

92

---

<!-- Página 93 -->

Aunque tienen sus virtudes —en especial los excelentes y muy detallados catálogos de amenazas, activos y contrame- didas que incluyen y facilitan las tareas iniciales de ingeniería de seguridad— falta mucho por realizar en relación con el análisis de riesgos en este campo: un estudio detallado de las principales metodologías arriba mencionadas muestra cómo a menudo se basan en matrices de riesgos para la gestión, lo que presenta inconvenientes bien documentados, por ejem- plo en Cox (2008), como serían las asignaciones ambiguas de probabilidades, impactos y riesgos y la promoción de evalua- ciones erróneas y poco coherentes que pueden conducir, fi- nalmente, a asignaciones de recursos inadecuadas. Más aún, con contadas excepciones como la de la metodología IS1 del gobierno británico, tales metodologías no tienen en cuenta explícitamente la intencionalidad de algunas de las ciberame- nazas, una cuestión clave a la hora de predecir cuáles de ellas pueden dirigirse contra un sistema. Dada la variedad de ame- nazas, así como la complejidad específica de los factores que afectan a los sistemas críticos, creemos que, desde el punto de vista de la modelización, no se emplean métodos ni procesos de gestión de riesgos suficientemente detallados ni sofistica- dos en muchos casos. En lo que sigue ilustraremos algunos ejemplos de apro- ximaciones algo más sofisticadas apoyadas en big data.

Big data para ciberseguridad

Monitorización masiva de redes

Comenzamos considerando el problema de la monitorización de redes. Dentro del protocolo NIST antes aludido nos en- contraríamos en el proceso de detección y, dentro del mismo, en las fases de monitorización continua y detección de ano- malías. Con las actividades que describimos tratamos de de- terminar y predecir si se producen cambios relevantes en el comportamiento de los elementos de una red o si se van a

93

---

<!-- Página 94 -->

alcanzar niveles críticos para algunas de las variables de esta- do de dichos elementos. Dada la importancia de tales actividades, se han desarro- llado distintos sistemas de monitorización que, periódica- mente y con alta frecuencia, recogen información sobre los sistemas interconectados de una organización para facilitar su monitorización. Por la creciente relevancia de las TIC, pode- mos enfrentarnos a organizaciones con varios centenares de miles de dispositivos interconectados de los que obtenemos decenas de variables cada pocos minutos. Tenemos, pues un ejemplo de problema en el que se capturan volúmenes muy altos de datos a muy alta velocidad. Además, hay cierta varie- dad en los datos a tratar pues, por ejemplo, algunas de las medi- das que se recogen son continuas, como puede ser el porcenta- je de uso de un disco, y otras son discretas, como el número de peticiones activas concurrentes a un sistema de base de datos. Esto plantea tremendos retos al procesamiento de datos para hacer las predicciones requeridas y apoyar la toma de decisio- nes en tiempo real para paliar problemas de seguridad en la red con suficiente antelación. Entre otras cosas, resulta virtualmen- te imposible que equipos de analistas humanos traten las series individualmente. Se crea así la necesidad de desarrollar un mar- co automatizado para realizar su análisis y un sistema que im- plemente tal marco. Además, muchos de los métodos estándar de análisis de series temporales no resultan útiles en nuestro contexto de monitorización masiva en tiempo real, bien porque no permiten tratar una cantidad tan enorme de datos de alta frecuencia, bien porque no pueden automatizarse debido a la versatilidad de las series a las que debemos enfrentarnos. Necesitamos, pues, un marco con los siguientes requisi- tos funcionales, además del estándar en ciencia de datos que requiere que la metodología sea precisa (en el sentido de que debe alcanzar buen comportamiento predictivo):

- Automático. Dada la gran cantidad de series tempora- les a monitorizar, la intervención de personas debería reducirse al mínimo.

94

---

<!-- Página 95 -->

- Escalable. El marco debería ser escalable en tiempo y memoria. Ha de ser suficientemente rápido como para poder tratar series temporales de muy alta fre- cuencia. Además, debido a la enorme cantidad de se- ries temporales a monitorizar, debería resumir y re- presentarlas en unos pocos parámetros, evitando así almacenar toda(s) la(s) serie(s). - Versátil. Debe permitir, tanto en el caso discreto como el continuo, tratar series con características diferentes como son la posible presencia de fases de crecimiento lineal, elementos de estacionalidad o estallidos en la actividad asociada a las series, siempre de forma au- tomática. Además, los rasgos de las series tempora- les pueden cambiar en el tiempo, por lo que el marco debe ser capaz de adaptarse dinámica y rápidamente a tales variaciones.

El interés del problema viene demostrado por el hecho de que dos grandes como Facebook y Twitter disponen de sistemas relacionados como son, respectivamente, Prophet y Anomaly Detection. Sin embargo, tales y otros sistemas no se adaptan específicamente a las necesidades del problema de monitorización de la seguridad en redes al que nos referimos. Por ello, en Naveiro et al. (2019) se propone un marco con alta capacidad predictiva completamente automatizable basa- do en una aproximación bayesiana que distingue entre series discretas y continuas. Para las series continuas se emplea una versión modificada de un tipo especial de modelos dinámicos lineales que incorpora información relativa a la presencia de estallidos regulares originados por procesos físicos tales como backups o compresiones, especialmente relevantes en este do- minio de monitorización. Una ventaja importante de los mode- los empleados es que pueden construirse empleando distintos bloques que capturan los rasgos específicos (tendencias, esta- cionalidad) de las series temporales. Debe introducirse tam- bién un método automático para identificar los modelos co- rrespondientes. Además, estos modelos resumen los aspectos

95

---

<!-- Página 96 -->

relevantes de la serie en unos pocos parámetros, posibilitando su escalabilidad espacial. Finalmente, el cálculo de las distri- buciones predictivas es relativamente rápido haciendo la aproximación escalable en el tiempo. Para el segundo tipo de series se emplean cadenas de Markov en tiempo discreto. Describimos brevemente el uso del sistema correspon- diente. Asociados a cada una de las series hay dos valores de referencia que designamos alerta (W) y crítico (C) referi- dos a niveles de observación tales que, en caso de ser exce- didos, deberían conducir a emitir señales de aviso y de nivel crítico, respectivamente. Por ejemplo, para un disco de al- macenamiento podríamos monitorizar su uso y hacer W = 0,9 y C = 0,95, significando que si alcanzamos un nivel de saturación del 95% del disco, su comportamiento podría degradarse e incluso colapsarse, produciendo una pérdida de servicio con los consiguientes costes económicos. Los umbrales dependerán del tipo de dispositivo y de su rele- vancia global. Obsérvese que empleamos un sistema de alarmas en dos niveles para tratar de obtener información más rica sobre fallos potenciales del dispositivo monitoriza- do. En el ejemplo indicado, W = 0,9 nos permite incremen- tar la atención antes de que sea demasiado tarde por alcan- zarse el nivel crítico. Realizamos entonces dos tipos de predicciones:

- A corto plazo. Nos permiten, por un lado, identificar el comportamiento anómalo de una serie cuando los valores observados no quedan dentro de los intervalos predictivos; esto se relaciona con cuestiones de segu- ridad y es útil para mostrar comportamientos críticos lo antes posible o detectar intrusos en el sistema. Por otro, nos permite lanzar alarmas cuando los intervalos predictivos cubren los umbrales W y/o C. - A largo plazo. Nos permite predecir estados críticos con tiempo suficiente cuando los umbrales W y/o C aparecen en los correspondientes intervalos predic - tivos.

96

---

<!-- Página 97 -->

La figura 6 representa una posible traza del sistema en la que se marcan el nivel de alerta y el nivel crítico. En ella se han marcado los instantes en los que los niveles críticos caen en los intervalos predictivos, así como los instantes en los que las observaciones quedan fuera de tales intervalos.

Figura 6 Traza de un sistema monitorizado.

15Datos originales Crítico Alerta

10

5

0

11:00 16:00 21:00

Gestión de ciberriesgos en la cadena de suministro

Los terremotos, las crisis económicas, las huelgas, los ataques terroristas y otros sucesos pueden producir interrupciones significativas en las operaciones de una cadena de suministro, afectando de forma significativa a los resultados de una orga- nización. Como ejemplo, Ericsson perdió 400 millones de euros tras el incendio en una planta de su proveedor de semi- conductores en el año 2000. Tales disrupciones pueden tener también efectos negativos a largo plazo. Para su tratamiento ha surgido la disciplina de la gestión de riesgos en la cadena de suministro (GRCS) que proporciona estrategias para re- ducir las probabilidades de que se produzcan tales disrupcio- nes y, en caso de que tengan lugar, su impacto sea lo menor posible. Como en otras aplicaciones de gestión de riesgos, la

97

---

<!-- Página 98 -->

GRCS incluye procesos de identificación, evaluación, control y monitorización de riesgos. Debido a la proliferación de los ciberataques, una cues- tión de interés reciente, potenciada por la creciente interco- nectividad de las organizaciones, se refiere a la inclusión de los ciberriesgos en la GRCS. Un ejemplo importante de su re- levancia es el caso del ciberataque a Target a través de su pro- veedor de aire acondicionado, mediante el que se robaron cerca de 70 millones de tarjetas de crédito en el año 2013. Por ello, han surgido distintos productos comerciales para la ges- tión de ciberriesgos en la cadena de suministros como Bitsight o Security Scorecard, aunque sus fundamentos son dudosos. Dentro del protocolo NIST antes aludido nos encontraría- mos, por un lado en el proceso de detección y monitorización continua y, por otro, en el proceso de identificación en rela- ción con la parte de evaluación de riesgos. Como ejemplo consideremos una compañía interconec- tada con sus proveedores. La compañía puede sufrir ataques directos; ataques indirectos a través de sus proveedores que se transfieran a la compañía; y, finalmente, ataques a los provee- dores que no se transfieren pero tienen consecuencias sobre la compañía por la no disponibilidad de un servicio o de un producto. Por ejemplo, en caso de que uno de los proveedores de la compañía quedase infectado por algún tipo de malware, el atacante podría escanear la red de la compañía y enviar emails infectados a la misma, que quedaría más probable- mente infectada, pues el software recibido se originaría desde una fuente legítima. Para la gestión de estos ciberriesgos, la compañía puede recoger grandes cantidades de datos de internet, típicamente a través de los denomimados “sistemas de inteligencia de amenazas”, que esencialmente se encargan de obtener infor- mación heterogénea de ingentes fuentes sobre la compañía y los proveedores sobre:

- Vectores de ataque, que aportan indicios sobre ataques potenciales como las IP de los dispositivos que estén

98

---

<!-- Página 99 -->

infectados por botnets o la información de login robada a través de las mismas. - El entorno de seguridad de las empresas, como el nú- mero de menciones negativas en blogs hacktivistas. - La postura de seguridad, como la cadencia de parcheo de aplicaciones en ellas.

Este es un proceso típico de ETL (extracción, transfor- mación y carga) pero, además, incluye métodos no triviales de preprocesamiento, por ejemplo a la hora de clasificarse como negativa una entrada en un blog. Obsérvese que este es un problema de clasificación, con la especificidad de que de- bemos tratar con texto para realizarla. A partir de los datos antes mencionados intentamos determinar:

- La probabilidad de que los proveedores de la compa- ñía sean atacados. - La probabilidad de que la compañía sea atacada, bien directamente, bien a través de los proveedores. - Los impactos que tales ataques podrían inducir sobre la compañía.

Dadas las reticencias de estas a proporcionar datos rela- tivos a los que designaríamos ataques suficientemente dañinos, empleamos métodos de juicios de expertos estructurados pa- ra mitigar su falta. Las probabilidades se estiman y predicen mediante modelos de regresión logística; los impactos se pre- dicen mediante modelos econométricos y de ingeniería. Todos ellos se van actualizando mediante la fórmula de Bayes a medida que se van recibiendo datos. En conjunto, en cada paso temporal (por ejemplo, diariamente) el sistema funcio- naría como sigue:

- Escaneamos la red para obtener datos en relación con los vectores de ataque, la postura y el entorno de se- guridad de la compañía y sus proveedores; los proce- samos y consolidamos.

99

---

<!-- Página 100 -->

- Estimamos a partir de ellos las probabilidades de ata- que y sus impactos. - Agregamos la información anterior para estimar los riesgos. - Lanzamos las alarmas, si es necesario, cuando estos riesgos son demasiado altos o han variado ostensible- mente. - Presentamos los resultados. - Hacemos las predicciones de riesgo para el siguiente periodo.

En la figura 7 se muestra la traza de cuatro índices de riesgos en los periodos de 0 a 100 (probabilidad de ataque a través de dos proveedores, de ataque directo y probabilidad total de ataque). A partir del periodo 100 se muestran las pre- dicciones a través de los correspondientes intervalos predicti- vos. Se observa, por ejemplo, que el segundo proveedor indu- ce más riesgo que el primero.

Figura 7 Trazas de índices de riesgo.

1,0

0,8

0,6 p

0,4

0,2

0,0 0 20 40 30 80 100 120

t

100

---

<!-- Página 101 -->

Clasificación adversaria

Como mencionamos en el capítulo 3, los problemas de clasi- ficación son de los más relevantes en ciencia de datos dentro del aprendizaje supervisado. Tienen aplicaciones en numero- sos campos como la detección de spam, la visión por ordena- dor o la genómica. Sin embargo, hasta hace relativamente poco tiempo se ha ignorado una cuestión muy relevante en ciberseguridad: la presencia de adversarios que pueden manipular activamente los datos disponibles para engañar al clasificador con objeto de obtener cierto beneficio. Por ejemplo, alguien que envía spam intenta hacer creer al clasificador que el mensaje envia- do es un correo legítimo, para poder obtener ventajas ven- diendo la información obtenida de la víctima. Además, en tales contextos, al ir mejorando los algoritmos de clasifica- ción, los adversarios van adaptando sus ataques al determinar los rasgos empleados por el clasificador para detectar spam. La presencia de adversarios adaptativos se ha mencionado también en áreas como la detección de fraude o en el desarro- llo de sistemas de seguridad biométricos, entre otros, dando lugar a un campo muy activo en la actualidad que se denomi- na “de aprendizaje automático adversario”. Dentro del pro- tocolo NIST antes aludido podríamos emplear estos métodos en la fase de protección para el control de accesos y el desa- rrollo de tecnologías de protección. Dalvi et al. (2004) proporcionaron una aproximación pionera para mejorar un algoritmo de clasificación en presen- cia de adversarios, tomando como base un algoritmo Naive Bayes que tenga en cuenta las ganancias y pérdidas asociadas a acertar y errar en las clasificaciones. Para ello, presentan el problema de aprendizaje adversario como un juego entre un clasificador C y un adversario A. En primer lugar, C calcula su clasificador óptimo suponiendo que los datos no han sido modificados, como se describió en el capítulo 3; después, A, que se supone conoce tal clasificador, calcula su ataque ópti- mo frente al mismo; luego C implementa su clasificador

101

---

<!-- Página 102 -->

óptimo frente a este ataque, y así sucesivamente. Sin embar- go, como indican los propios autores, se hace una hipótesis muy fuerte: todos los parámetros de ambos jugadores son compartidos y conocidos por todos los participantes. Aunque esta condición, denominada “de conocimiento común”, es estándar en la denominada teoría de juegos (no cooperativa), no es, de hecho, realista en escenarios de ciberseguridad co- mo los que consideramos, en los que los participantes tratan de esconder información. A pesar de ello, esta hipótesis ha permeado la mayoría de aproximaciones posteriores a este problema de clasificación adversaria. Como alternativa surge la posibilidad de emplear méto- dos del análisis de riesgos adversarios. Para ello suponemos que estamos apoyando a C, que conoce los elementos de su problema, pero tiene incertidumbre sobre los elementos del problema de A (sus creencias y preferencias). Entonces po- demos modelizar esta incertidumbre mediante distribuciones sobre tales creencias y preferencias y resolver el problema del atacante para encontrar los ataques más probables y, en fun- ción de ellos, encontrar el mejor clasificador frente a ataques, haciéndolos más efectivos y robustos.

Para saber más

En este capítulo hemos ilustrado cómo las tecnologías y me- todologías big data pueden ayudar en el tratamiento de algu- nos problemas de ciberseguridad. Un buen reflejo del proble- ma aparece en los Global Risk Maps anuales que realiza el Foro Económico Mundial. El NIST, en su estándar SP 800- 30, presenta un marco muy completo de gestión de la ciber- seguridad, aunque adolece de promover métodos de gestión de riesgos basados en matrices de riesgos. . Brutlag (2000) es una referencia clásica en el problema de detección de anomalías. El marco aquí descrito usa fuerte- mente los modelos dinámicos lineales y puede verse en Naveiro et al. (2018a).

102

---

<!-- Página 103 -->

Existen ya diversos sistemas comerciales para GCRCS como Bitsight o Security Scorecard, pero adolecen de funda- mentos rigurosos. La aproximación aquí descrita está imple- mentada en Blueliv y se presenta en más detalle en Redondo et al. (2018). Una revisión reciente de la literatura sobre clasificación adversaria puede verse en Biggio et al. (2018). La mayoría de estos trabajos se basa en teoría de juegos no cooperativa, apo- yada en el concepto de equilibrio de Nash y variantes, como se detalla en Menache y Ozdaglar (2011). Una aproximación al- ternativa al análisis de conflictos está en el análisis de riesgos adversarios que se describe en Banks et al. (2015). Naveiro et al. (2018b) proporcionan una aplicación a detección de spam.

103

---

<!-- Página 104 -->

CAPÍTULO 7

## La otra cara del big data

Introducción

En los capítulos anteriores hemos introducido los conceptos fundamentales que facilitan el análisis de big data y descrito cómo sus aplicaciones en muy diversos campos están permi- tiendo avances hasta hace poco inimaginables. Sin embargo, no es menos cierto que esta transformación digital también conlleva aspectos menos deseables, incluso peligrosos. Muchas de estas cuestiones requerirían un amplio debate en nuestra sociedad que solo ahora está empezando a tomar for- ma. De hecho, durante los últimos años se nos ha privado de este debate, por una parte por la rapidez de implantación de las nuevas tecnologías muy superior a la capacidad de re- flexión de la sociedad sobre sus consecuencias y, por otra, porque los motores de dicho cambio se han esforzado, en ge- neral, en que tal debate no tenga lugar. En este capítulo trata- remos los aspectos menos edificantes de esta revolución tec- nológica: la otra cara del big data.

104

---

<!-- Página 105 -->

¿Quién almacena nuestros datos? ¿Qué datos? ¿Con qué fin?

En sus inicios, navegar por internet era una actividad casi anónima. Es cierto que los proveedores de servicios estaban obligados a identificar la dirección IP de una máquina que se conectaba y vincularla con el titular del contrato, pero los na- vegadores eran programas relativamente sencillos destinados a desplegar el código html (texto, imágenes, etc.) que descar- gaban de la página a la que se estaba accediendo. Para entender lo que ocurre hoy en día, invitamos al lec- 22 tor a visitar el sitio Webkaypara obtener ejemplos de todo lo que un sitio web puede averiguar de manera automática so- bre nosotros. Para empezar, el navegador revelará la dirección IP, a partir de la que se puede identificar de manera muy aproximada la ubicación por medio de una llamada a la API de geolocalización de Google. Además de la IP, se transmiti- rán la versión de nuestro navegador, el hardware de la máqui- na, el sistema operativo que estamos usando y la lista crece si tenemos sesión abierta en Google, Facebook o alguna otra red social. Aparentemente resulta información inocua, pero su verdadero valor y potencial es que nos identifica casi de manera única: en la región del Puerto de Santa María, desde donde se están escribiendo estas líneas, es muy probable que no haya otra persona con un ordenador con sistema operativo Linux Ubuntu 18.04, navegador Firefox 63.0 y un procesa- dor con ocho núcleos. La configuración conjunta de todos estos elementos identifica de manera única nuestro ordena- dor, aunque volveremos más adelante sobre este tema al ha- blar de anonimización robusta. Cierto es que esta identifica- ción única no está asociada aún a nuestro nombre, pero cualquier sitio web puede saber si nuestro ordenador es el mismo que visitó el sitio la semana pasada. Además, los nave- gadores no solo están capacitados para recopilar esta sencilla información, sino que pueden hacer un seguimiento mucho

22. http://webkay.robinlinus.com/

105

---

<!-- Página 106 -->

más detallado de nuestra actividad: cómo movemos el ratón, cuánto tiempo ha pasado desde cada suceso, dónde centra- 23 mos nuestra atención al navegar, etc.. Todo lo mencionado hasta ahora es un mero comienzo: la información que revela el propio navegador sin interven- ción de los sitios visitados. Pero, además, muchos de estos si- tios están muy interesados en recopilar información sobre sus visitantes, tarea que realizan a través de las conocidas cookies. Estas son pequeños programas que se instalan en el ordena- dor la primera vez que se visita una página y cuya tarea es intercambiar información con la misma, recordar preferen- cias o visitas pasadas. Gracias a ellas nuestra ciudad aparece automáticamente la siguiente vez que entramos en un sitio de predicción del tiempo o los productos que almacenamos en el carrito de compra siguen ahí días después de que los pusiéra- mos allí. Muy útil. El problema es que muchas páginas web tienen acuerdos comerciales para instalar en nuestro ordenador cookies de terceros, es decir, programas que enviarán información a otros sitios que nada tienen que ver con el sitio visitado. El objetivo habitual será recopilar una información lo más deta- llada posible sobre nuestro perfil, nuestros gustos y activida- des, de cara a personalizar las ofertas publicitarias que recibi- mos mediante la denominada “mercadotecnia de precisión”. De este modo recibiremos ofertas incansables de zapatillas de deporte tras visitar una web de productos deportivos, incluso tras haber comprado las zapatillas… Sin embargo, hay oca- siones en que las cookies de terceros pueden extraer sin nues- tro consentimiento información altamente sensible, como las contraseñas almacenadas en nuestro navegador o el texto que se escribe en formularios web antes incluso de enviarlo. A diferencia de las cookies de análisis de tráfico en webs más o menos inofensivas, ya que solo tratan información agregada, estos programas están diseñados para extraer información

23. Como experiencia ilustrativa, sugerimos una visita a https://clickclickclick. click/, una iniciativa pedagógica del VPRO Medialab.

106

---

<!-- Página 107 -->

personal y venderla a terceros. De hecho, un estudio reciente de la Universidad de Princeton (WebTAP, 2019) reveló que 500 de los sitios web más visitados estaban recopilando todo tipo de información personal sobre sus visitantes y vendiendo la información a terceros. Como ejemplo, Google accedió a pagar 22,5 millones de dólares en 2012 por desactivar la pro- tección del navegador Safari contra cookies de terceros. En este orden de cosas, conviene recordar que con la entrada en vigor del Reglamento General de Protección de Datos (RGPD) en la Unión Europea en 2018 queda regula- do el uso de cookies: “Las personas físicas pueden ser asocia- das a identificadores en línea […] como direcciones de los protocolos de internet, identificadores de sesión en forma de ‘cookies’ u otros identificadores […]. Esto puede dejar huellas que, en particular, al ser combinadas con identificadores úni- cos y otros datos recibidos por los servidores, pueden utilizar- se para elaborar perfiles de las personas físicas e identificar- las”. En otras palabras: cuando las cookies puedan identificar a un individuo, se les considerará datos personales. En el mundo de la ciencia de datos, capturar informa- ción es un producto de gran valor. Las empresas son muy conscientes de ello. Pero no tanto los usuarios. Así, las empre- sas suelen recurrir a trucos para recopilar tal información, ofreciendo servicios cuyo verdadero fin es pagar por nuestros datos. Las tarjetas de fidelización en supermercados que mencionamos en el capítulo 2 son los primeros ejemplos de esto: nos ofrecen pequeños descuentos a cambio de recopilar toda la información sobre nuestra lista de la compra (figura 8). El efecto es aún más acusado con las apps en los teléfonos móviles: para acceder a una hamburguesa gratis o al sorteo de algún regalo, nos pedirán que instalemos la aplicación y abra- mos una cuenta de usuario. Estas apps recopilarán todo tipo de información sobre nosotros (a veces incluso nuestra lista de contactos), la mayor parte de las veces sin que seamos conscientes. Como ejemplo, en 2017 la compañía fabricante de los robots aspiradores Roomba anunció que tenía inten- ción de vender la información recopilada por sus robots a

107

---

<!-- Página 108 -->

terceros (Google, Amazon, etc.), con gran entusiasmo por parte de sus accionistas pero creando un importante revuelo: tal información eran planos detallados de cada casa, con la ubicación de muebles y objetos. No sabíamos que al meter un robot para que quitara el polvo de casa ¡estábamos introdu- ciendo un espía! Quizás uno de los ejemplos más conocidos en nuestro país de aplicaciones móviles que realizan tareas ocultas al usuario que las instala en su teléfono se desveló en el año 2018, poco después de la entrada en vigor del mencio- nado RGPD. En ese momento, se descubrió que la Liga Profesional de Fútbol estaba empleando la geolocalización y el micrófono de los móviles que habían instalado su app para detectar bares y establecimientos que estuvieran proyectando partidos sin haber pagado la correspondiente licencia.

Figura 8 Las tarjetas de fidelización de supermercados están comprando tus datos. XKCD: A webcomic of romance, sarcasm, math, and language.

Fuente: https ://xkcd .com/2006/

108

---

<!-- Página 109 -->

Hemos visto pues algunas de las formas mediante las que las empresas acceden a nuestros datos de manera más o menos escondida y con fines distintos a los anunciados. Sin embargo, resulta casi paradójico que la mayor cantidad de datos de la que disponen grandes compañías como Google, Amazon o Facebook es información que les proporcionamos nosotros de manera voluntaria, aunque sigue siendo cierto que apenas somos conscientes de los diversos usos que se pueden hacer y hacen de ella.

El verdadero negocio de los gigantes de internet

En la era de internet nos hemos acostumbrado a que muchas cosas sean gratis: comprábamos periódicos en el kiosco hasta que empezamos a leer contenidos en sus versiones en línea (y el periódico dejó de ser una fuente de información para con- vertirse en un catálogo comercial); comprábamos navegado- res GPS para el coche hasta que Google Maps empezó a ofrecer el mismo servicio de manera gratuita; en la universi- dad teníamos varios ordenadores y un equipo de informáti- cos encargados de gestionar el correo electrónico corporativo con buzones de capacidad muy limitada hasta que Google nos ofreció gestionar nuestro servicio con buzones ilimitados de manera gratuita. Nadie puede resistirse a la atracción de lo gratuito. Uno se pregunta, sin embargo, dónde está el pro- ducto detrás de tanta gratuidad, ¿cómo ganan dinero estas compañías? Y aquí viene a la memoria la frase del mítico ju- gador de póquer Amarillo Slim: “Mira a tu alrededor, si no sabes identificar al pardillo en la mesa, entonces el pardillo eres tú”. En internet, como no sabes cuál es el producto, en- tonces el producto eres tú. Para Google, Facebook y el resto de gigantes de internet no somos usuarios, sino productos: los destinatarios de sus campañas de publicidad. Así pues, el modelo de negocio es un intercambio en el que nos ofrecen un gestor de correo electrónico, una platafor- ma para conversar con amigos, para encontrar a tus viejos

109

---

<!-- Página 110 -->

compañeros de clase, un navegador GPS para no perdernos en la ciudad, una carpeta en la nube para almacenar nuestros ficheros…, todo ello a cambio de recopilar una cantidad de datos tan inmensa que probablemente hace que Google nos conozca mejor que nosotros mismos: qué coche te quieres comprar, dónde vas a ir de vacaciones, cuántos hijos tienes, qué camino tomas para ir a trabajar, a quién vas a votar, cómo te sientes hoy, esa pasión oculta que no has confesado a na- die… pero has buscado en internet, a qué hora te acuestas y con quién, etc. Aunque los hemos mencionado en capítulos anteriores, conviene entender los fundamentos básicos del mercado pu- blicitario digital. A diferencia de los anuncios tradicionales en televisión, que solo permitían segmentar el público objetivo por franja horaria o asociado a ciertos programas de televi- sión, la publicidad digital presume de su precisión al impactar a la persona escogida en el lugar idóneo y el momento ade- cuado. De este modo, se obtiene una eficiencia mayor de la inversión en publicidad. Cada vez que cargamos la página de nuestro diario favorito para leer las noticias del día, el corres- pondiente banner publicitario que veremos depende de una compleja subasta (RTB, Real Time Bidding) en la que distin- tos algoritmos pujan por mostrarnos su anuncio en función de cuanto piensen que nuestro perfil se adapta al producto que desean vender. Todo esto ocurre en la fracción de segun- do que tarda el navegador en cargar la página; obviamente, estos algoritmos emplean toda la información que puedan adquirir sobre quien está al otro lado del ordenador para afi- nar los modelos: más información implica modelos más pre- cisos y, típicamente, mayor rendimiento de la inversión en publicidad. Cuando introducimos una búsqueda en Google se pone en marcha otra subasta, en función de las palabras de búsqueda, en la que los anunciantes pujan para que su página web aparezca en lo más alto de los resultados de búsqueda (SEM, Search Engine Marketing), una vez más en función de nuestra ubicación y otras variables. El resultado depende de la puja, pero también de un factor de calidad que Google

110

---

<!-- Página 111 -->

asigna a cada empresa en función de cuánto se adecúe su actividad a las palabras buscadas, según un algoritmo que so- lo él conoce. El elemento diferenciador que aupó a Google a su posición de liderazgo fue el algoritmo PageRank, que el público identificó de inmediato como mucho más útil de cara a buscar contenido en internet. Las páginas de anunciantes se mostraban en un principio de manera claramente diferencia- da de los resultados de la búsqueda, pero hoy en día apenas se nota la diferencia. A su vez, se ha desarrollado toda la indus- tria de posicionamiento en buscadores (SEO, Search Engine Optimization). Google ha probado muchos productos y lí- neas de negocio diversificando sus inversiones, pero, en reali- dad, la que mejor le ha funcionado es la de la publicidad: así, Google es la mayor agencia de publicidad del mundo. Facebook o Twitter también siguen el mismo modelo de ne- gocio: nos ofrecen una plataforma para que voluntariamente les entreguemos una cantidad inimaginable de datos persona- les gracias a los cuales pueden afinar campañas de publicidad muy orientadas a su público objetivo. Pero entonces, ¿cuánto deberían valer nuestros datos personales? La pregunta es muy relativa y probablemente tenga dos respuestas bien diferenciadas para el que cede los datos y para el que los adquiere. Para el ciudadano medio, a tenor del comportamiento observado durante los últimos años, el valor que concedemos a nuestros propios datos es más bien pequeño, pues prácticamente los hemos regalado a cambio de nada a las grandes compañías. Para los gigantes de internet podemos hacer un cálculo sencillo basado en dividir el beneficio del sector publicitario digital en Estados Unidos durante 2016 (83.000 millones de dólares) entre el número de usuarios en el país (280 millones) lo que arrojaría una cifra media de 296 dólares per cápita. 24 En la economía digital nadie da duros a cuatro pesetas, o como nos recordaba Milton Friedman: “There ain’t no such

24. Para los lectores más jóvenes: duro es la forma coloquial de referirse a una moneda de cinco pesetas.

111

---

<!-- Página 112 -->

thing as a free lunch”. Veamos pues brevemente los modelos de negocio de las plataformas digitales a través de tres ejemplos y de ese modo entenderemos mejor cómo monetizar nuestros datos (Li et al., 2018).

- Una plataforma de comercio electrónico, como Amazon Marketplace, pone en contacto consumido- res y vendedores a través de su web. Los vendedo- res pagan a Amazon el 30% del valor de sus ventas; a cambio, tienen la posibilidad de acceder al mercado global, pero también a la información que Amazon les proporciona sobre sus consumidores. Amazon re- copila de los consumidores el historial de visitas, su localización, los datos de las transacciones, etc., lo que le permite construir perfiles muy ajustados de nues- tros hábitos de consumo. Con esos perfiles ofrece a las empresas asesoría en estrategias de precios (dy- namic pricing), logística (dónde instalar un nuevo al- macén) y publicidad muy dirigida al público objetivo. Aproximadamente la mitad de las ventas de Amazon son de terceros y, solo en la comisión del 30% sobre estas ventas, su beneficio anual se estima en 3.000 mi- llones de dólares (Amazon 10K report), solo en el sec- tor de ventas al por menor. Sin embargo, su oferta de servicios en la nube (Amazon Web Services), aunque represente menor facturación, supera ya a las ventas al por menor en volumen de beneficios, siendo la ten- dencia ascendente. - Booking.com es un portal de viajes que ofrece 28,9 millones de alojamientos a través de su web en más de un millón de localidades en 230 países. Su modelo de negocio consiste en poner en contacto a propieta- rios de alojamientos y hoteles con clientes, cobrando a los primeros una comisión sobre ventas del 15%. Los consumidores se benefician de la rapidez en la reserva y de descuentos en alojamientos; los propietarios tie- nen acceso a un mercado muy rápido para dar salida a

112

---

<!-- Página 113 -->

excedentes perecederos y cubrir plazas de manera ágil y dinámica. El portal recopila información del histo- rial de búsquedas, transacciones, opiniones y localiza- ción de consumidores. Proporciona a los propietarios estrategias de precios, predicción de demanda y mar- keting de precisión, demostrando un estudio reciente que ayuda a incrementar su beneficio en un 7%. Solo en comisiones, el beneficio de Booking en 2017 fue de 12 millones de dólares, una cantidad nada desdeñable para una compañía que no posee un solo hotel. De hecho, en la sede central de Booking en Ámsterdam el 90% de los empleados son ingenieros informáticos. - Finalmente, Waze es una plataforma de crowdsour- cing que proporciona vías de intercambio de infor- mación entre conductores, que instalan su app de manera gratuita. Ofrece información en tiempo real sobre accidentes, estado de la carretera, etc., generada y compartida por otros usuarios; calcula rutas ópti- mas y estima tiempos de recorrido. En el año 2013, Google compró Waze por 1.100 millones de dólares. Una vez más, el modelo de negocio se basa en propor- cionar a terceros información sobre desplazamientos. Por ejemplo, usar datos de tráfico para que las compa- ñías de medios decidan su estrategia de colocación de vallas publicitarias, enviar publicidad a los usuarios en función de su localización o para acceder a un restau- rante cercano, entre muchas otras.

Las principales empresas hoteleras son Airbnb y Booking; no tienen un solo alojamiento en propiedad. La principal empresa de movilidad es Uber; no posee un solo vehículo. La principal empresa del sector de venta al por me- nor es Alibaba; no dispone de inventario. La principal empre- sa de contenidos digitales es Facebook; no genera su conteni- do. Son empresas de datos. Recopilan, limpian, analizan y desarrollan aplicaciones para poner en contacto productores de servicios con consumidores.

113

---

<!-- Página 114 -->

Prácticamente nadie en el entorno empresarial duda ya del inmenso valor que tiene la adquisición de datos, aunque la sociedad en su conjunto no sea aún muy consciente de ello. El desarrollo de tecnología requiere una inversión constante pa- ra que no se quede obsoleta. Sin embargo, el valor de los da- tos puede aumentar en el futuro gracias a procesos de fusión e hibridación, que permiten extraer nuevo valor de ellos al combinarse con otras fuentes de datos para realizar nuevas funciones.

Big brother is watching: ciencia de datos al servicio del poder político

Queda claro, pues, que las empresas emplean muchos de nues- tros datos como lo que miramos en internet, por dónde nos desplazamos, qué restaurantes, productos o canales de televi- sión nos gustan o, incluso, llegan a escuchar lo que estamos diciendo. A muchas personas les parecerá una invasión inad- misible de su privacidad. A otras muchas seguramente les im- porte bien poco, pues al final el único objetivo es comercial: vender sus productos o evaluar sus inversiones en publicidad. Cuando una empresa conecta el micrófono de mi móvil no está realmente interesada en lo que digo, tan solo quiere saber qué canal de televisión estoy mirando. ¿Por qué? Porque una parte importante de la actual industria publicitaria se basa en pagar por los anuncios en función de la contribución que cada uno haya tenido en conseguir que adquieras el producto (en su jerga, en tu “conversión”). Se denominan “modelos de atribu- ción” y en un mundo donde cada vez más nos esforzamos por- que todo sea medible, conocer y predecir el efecto concreto de un anuncio de televisión o un banner en internet tiene un im- pacto considerable en la economía digital. Pero las cosas no acaban aquí. La capacidad que proporcionan las nuevas tecno- logías para conocer y controlar masivamente una población entera no puede pasar (y no ha pasado) desapercibida a toda organización interesada en el poder político.

114

---

<!-- Página 115 -->

El espionaje y la represión de aquellos que no piensan como nosotros ha existido desde siempre. Sin embargo, lo que cambia con las nuevas tecnologías de procesamiento in- teligente de información es la escala de vigilancia, que puede llegar de manera efectiva a cualquier individuo en cualquier momento a través de los dispositivos digitales (teléfonos, alta- voces y televisiones inteligentes, wearables, etc.). George Orwell terminó de escribir 1984 en 1948; en ella dibujaba una distopía futurista en la que un estado opresor controlaba a la población a través de telepantallas. Curiosamente, en el mismo año Claude Shannon publicó su Teoría matemática de la comu- nicación y Norbert Wiener su Cibernética o el control y comuni- cación en animales y máquinas. Ambas teorías han tenido una influencia considerable en el desarrollo de la IA. En 1948, sin embargo, la computación estaba aún en pañales: Alan Turing se unía al proyecto Mark 1 de la Universidad de Manchester para construir uno de los primeros ordenadores capaces de ejecutar programas por medio de tarjetas perforables. El orde- nador ocupaba una habitación entera y se empleó para cálcu- los relacionados con la hipótesis de Riemann, un problema matemático sobre la distribución de números primos. Se esta- ban sembrando las semillas que han dado lugar a las ciencias de la computación y la IA. Hoy en día, tras setenta años de vertiginoso desarrollo, la hipótesis de Riemann sigue sin haber sido demostrada, pero disponemos ya de la tecnología necesa- ria para implementar una sociedad orwelliana. Quizás estemos 25 ya viviendo en ella y no seamos del todo conscientes…. Entre 1950 y 1989, la policía política de la antigua RDA, la infame Stasi, perfeccionó los métodos de vigilancia y con- trol políticos llegando a ocupar unas 250.000 personas entre empleados e informantes, penetrando en prácticamente cual- quier actividad de la vida pública de aquel país. Para una po- blación de 17 millones suponía un espía por cada 70 habitan- tes. Con los métodos de supervisión existentes en la actualidad,

25. “Winston Smith: Does Big Brother exist? / O’Brien: Of course he exists. / Winston Smith: Does he exist like you or me? / O’Brien: You do not exist”.

115

---

<!-- Página 116 -->

empleando técnicas de IA, tratamiento de imágenes y proce- samiento del lenguaje natural, se pueden vigilar miles de mi- 26 llones de ciudadanos con apenas varios miles de empleados. Así, en tiempos de la Stasi espiar a una persona era un proce- dimiento más o menos laborioso: hacía falta acceder física- mente a su domicilio para intervenir su teléfono, personal para seguir sus desplazamientos y hacer fotos, etc. Hoy en día todo resulta mucho más fácil en el mundo digital. Y para faci- litar aún más la tarea, nosotros mismos proporcionamos mu- cha información sobre nuestra actividad a través del correo electrónico y las redes sociales. Al abrir una cuenta en Facebook, Twitter o Gmail firmamos un acuerdo con las co- rrespondientes condiciones de servicio. Sí, ese mensaje tan largo en letra muy pequeña que nadie lee… En dicho acuerdo se regula el uso que la empresa hará de nuestros datos, entre los que no se contempla la cesión a terceros. Sin embargo, en 2013 Edward Snowden, un empleado de la NSA, reveló en The Guardian y The Washington Post que la agencia poseía un programa clandestino, llamado PRISM, que recopilaba infor- mación de los usuarios de empresas como Microsoft, Google, Skype, Yahoo, Apple, Youtube o Dropbox, que recibían a cambio millones de dólares. Podríamos pensar que, al fin y al cabo, lo hacían a petición de su Gobierno y para cuestiones de seguridad nacional; además, si uno no tiene nada que es- conder, no tiene por qué importarle. Sin embargo, el mal uso de algoritmos de IA y ciencia de datos en redes sociales puede tener efectos notables en elecciones y en la propagación de ideas en la sociedad, como mencionamos en el capítulo 4 y describimos en detalle más adelante. Uno de los aspectos más controvertidos referidos a segu- ridad y TIC es la combinación entre cámaras de videovigilan- 27 cia y los avances en IA para reconocimiento facialo análisis

26. Los archivos de la Stasi fueron destruidos tras su disolución en 1989 y, curiosamente, un proyecto de inteligencia artificial pretende reconstruir todos los documentos en papel destruidos por la trituradora. 27. El reconocimiento facial es también un problema de aprendizaje supervisado en el que las redes neuronales convolutivas han alcanzado una eficiencia notable.

116

---

<!-- Página 117 -->

de imagen y vídeo. La ubicuidad de cámaras CCTV en las ciudades hace posible cubrir prácticamente cualquier ángulo; los algoritmos que poseemos permiten el procesamiento au- tomatizado de imágenes y vídeos para detectar una determi- nada persona, ya sea por sus rasgos faciales o, incluso, por su modo de caminar (gait analysis). Esta tecnología, ya en uso en aeropuertos y centros de alta seguridad en Europa, está im- plantada en el acceso a residencias y zonas urbanas en China (donde se estima que existen 200 millones de cámaras de vi- gilancia). Incluso los agentes de policía patrullan ya con gafas inteligentes que les permiten identificar cualquier persona que tenga ficha en su base de datos (Mozur, 2018).

Experimentos sociales en la era digital: el caso de Cambridge Analytica

En el año 2012 un grupo de investigadores de Facebook y de Cornell University decidieron realizar un experimento psico- lógico de dimensiones hasta entonces nunca vistas, cuyo re- sultado publicaron en la prestigiosa revista PNAS (Kramer et al., 2014). Como lector de estas líneas hay una alta probabili- dad de que tengas una cuenta en Facebook, pero quizás no te hayas parado a pensar que los mensajes que aparecen en tu página no son todos los que genera tu red de amigos, sino que se seleccionan con ayuda de un algoritmo que solo Facebook conoce. El experimento social consistía en modificar dicho algoritmo sobre un total de 700.000 individuos, de modo que a una parte se les mostraban mensajes negativos generados por sus amigos, mientras que a los otros se les mostraban 28 mensajes positivos. Todos los mensajes eran reales, modifi- cándose solo el filtro que los selecciona. El resultado quizás no es sorprendente: aquellos que recibían mensajes negativos tenían una mayor tendencia a enviar, a su vez, mensajes

28. Catalogar un mensaje como positivo o negativo es una tarea que se conoce como “análisis de sentimientos”. Es un problema relativamente sencillo de aprendizaje supervisado en procesamiento de lenguaje natural.

117

---

<!-- Página 118 -->

negativos, mientras que los que recibían mensajes positivos enviaban con mayor frecuencia mensajes positivos. Sin em- bargo, lo que resulta llamativo es que un ingeniero informáti- co, modificando unas pocas líneas de código, era capaz de propagar estados de ánimo sobre una población entera. El experimento recibió muchas críticas porque los usuarios de Facebook no habían sido informados ni dieron su consenti- miento para participar en él… aunque esto quizás no debería ya sorprendernos a estas alturas del capítulo. Pero… un momento. Si podemos propagar estados de ánimo, también podríamos propagar ideas y filtrar unas res- pecto a otras. Era evidente que las redes sociales tenían la capacidad de influir en elecciones y procesos democráticos. Como comentamos en el capítulo 4, Cambridge Analytica era una empresa que ofrecía servicios de asesoría electoral usan- do minería y análisis de datos fundada por Steve Bannon, el gurú de la alt-right. Entre muchas otras, la empresa prestó sus servicios a la campaña presidencial de Donald Trump en 2016, así como a la plataforma Leave.eu a favor del Brexit en el referéndum del mismo año. La compañía usaba datos de usuarios de Facebook captados a través de una app que cap- turaba la información de las 270.000 personas que la instala- ron y de todos sus contactos, llegando a recopilar los de 87 millones de usuarios. Con unos pocos likes, páginas visitadas y su comportamiento comercial se pueden elaborar modelos psicológicos de cada usuario que después se utilizan para ela- borar propaganda electoral personalizada (behavioural micro- targetting, en palabras de la empresa). En realidad no es más que la mercadotecnia de precisión que hemos mencionado en la sección anterior, pero el producto en este caso sería un candida- to electoral. El escándalo adquirió tintes tragicómicos cuando, en una grabación con cámara oculta para Channel 4, se mos- traba al CEO de la empresa vendiendo sus servicios a un supuesto candidato de Sri Lanka. El ejecutivo asesoraba a los potenciales clientes sobre trampas, sobornos y campañas de descrédito de oponentes políticos, para lo cual proporciona- ría bellas muchachas ucranianas (Bridge, 2018). Cuando el

118

---

<!-- Página 119 -->

escándalo Cambridge Analytica saltó en marzo de 2018, tras las declaraciones de un exempleado, Facebook perdió en un mes 37.000 millones de dólares en capitalización bursátil y la pro- porción de usuarios que confiaban en la compañía bajó al 41% al conocerse sus prácticas de monetización de datos personales. Un compungido Mark Zuckerberg comparecía poco después ante el Senado de los Estados Unidos para explicar el papel de Facebook en el uso ilegal de datos para perfilado con fines elec- torales. Una vez más, en la nueva economía digital se volvía a 29 demostrar que vale más pedir perdón que pedir permiso.

Círculos viciosos y sesgos en el sistema

En 2016 Cathy O’Neil, científica de datos y ex quant en la banca de inversión, publicó un libro con impacto considera- ble en la comunidad de especialistas en ciencia de datos. Su Weapons of Math Destruction alerta sobre las cuestiones éticas asociadas al uso que los algoritmos de IA están teniendo en la sociedad, donde un número cada vez mayor de decisiones se toman a partir de los resultados de un modelo de aprendizaje automático. Hasta hace poco, en la industria bancaria una persona que iba a pedir un préstamo al banco se entrevistaba con el director de la sucursal, que evaluaba, teniendo en cuenta el his- torial financiero y su conocimiento de la persona, la posibilidad de que dicho crédito no fuera devuelto, decidiendo en conse- cuencia. Quizás era un proceso sujeto a fallos de apreciación, pero era más humano que los sistemas actuales en los que al- gunos modelos predictivos entrenados sobre datos pasados to- man decisiones de manera automática sin conocer a la persona más que a través de un puñado de datos. El problema es que, por ejemplo, una de esas variables predictivas podría ser el có- digo postal: el algoritmo aprende que los habitantes de cierto

29. Otro ejemplo es la implantación en 2018 de patinetes eléctricos: la compañía Lime comenzó a colocar miles de patinetes en las ciudades sin apenas conocimiento de las autoridades locales ni normativa sobre su circulación.

119

---

<!-- Página 120 -->

distrito tienen mayor probabilidad de créditos fallidos y, en consecuencia, el modelo decide que han de pagar una prima mayor por existir mayor riesgo de impago o, directamente, se les deniega el crédito. El resultado es que se aumenta la brecha de desigualdad social, dando lugar a un círculo vicioso que re- troalimenta y confirma el modelo predictivo. Sucede algo pare- cido con las primas de seguros médicos: aceptamos pagar una prima mayor en función de la edad porque entendemos que el gasto médico crece a una edad más avanzada. Sin embargo, ¿resulta ético vincular la prima del seguro médico al lugar don- de vivimos? Como se acostumbra a decir, en la determinación de nuestra esperanza de vida, mucho más que nuestro código genético, influye nuestro código postal. En Minority Report, el film futurista dirigido por Spielberg en 2002, Tom Cruise encarna al jefe de una policía precrimen. Algunas facetas de la película que por entonces eran ciencia ficción hoy son realidades, como por ejemplo las predicciones de crimen basadas en big data que ya se están utilizando en ciudades como Los Ángeles. PredPol es un software comercial para que cualquier fuerza policial en cualquier lugar del mun- do pueda usar esta tecnología, entre los que ya se encuentran Suzhou (China), Kent (Reino Unido) y los Países Bajos, ade- más de varios estados en los Estados Unidos. Es sin duda inte- resante el mensaje de que gracias a este sistema se puede enviar policía al lugar adecuado en el momento justo, antes de que se cometa un crimen. Sin embargo, el sistema ha recibido tam- bién fuertes críticas por promover estereotipos raciales o por entrenar el modelo sobre datos sesgados. Una vez más, vemos la profecía que se autocumple: los datos de entrenamiento para el modelo, es decir, los crímenes pasados, vienen ya sesgados porque la policía se ha concentrado en determinadas zonas donde muchos de estos crímenes están vinculados a la margi- nalidad, mientras que los crímenes financieros en zonas aco- modadas no se detectan con la misma facilidad. Como resulta- do del modelo, se enviará mayor fuerza policial a determinadas zonas y se detectarán más crímenes en ellas, confirmando y reforzando la predicción del modelo.

120

---

<!-- Página 121 -->

Entrenar sobre datos sesgados es uno de los problemas de la aplicación de modelos de aprendizaje estadístico en la vida real. Desde un punto de vista científico, el problema no es de los modelos, que aprenden correctamente a reproducir los datos a los que se han enfrentado, sino del uso que hace- mos de ellos, que puede ampliar las desigualdades y sesgos ya existentes en su aplicación sistemática. En el procesamiento del lenguaje natural, desde hace pocos años se usa el aprendi- zaje profundo para la codificación eficiente de palabras (word embedding). A través de una red neuronal que aprende sobre cientos de miles de textos escritos se asigna a cada palabra un vector en un espacio lineal de dimensión en torno a 300, de forma que solo por la mera codificación el sistema aprende propiedades semánticas como sinónimos y analogías del esti- lo “París es a Francia lo que Berlín es a Alemania”. Unos in- vestigadores descubrieron recientemente (Bolukbasi et al., 2016) que los algoritmos de word embedding más populares, Word2vec y Glove, aprendían analogías como “hombre es a ingeniero informático como mujer es a ama de casa”, así co- mo muchas otras analogías con sesgo de género que no debe- rían existir: cirujano-enfermera, fútbol-voleibol o brillante- cariñosa. De nuevo, la culpa no es de los algoritmos, sino de los siglos de textos escritos con evidente desigualdad de géne- ro que se emplean para aprender la codificación de las pala- bras. Sin embargo, el riesgo de utilizar algoritmos automáti- cos para procesar textos escritos que piensen de esta manera es algo que evidentemente no podemos permitir. Por suerte, son problemas que se pueden corregir con un par de trucos matemáticos de álgebra lineal (gender debiasing), pero para ello se necesitan conocimientos técnicos avanzados y acceso al código fuente de los algoritmos. En resumen, en la mayor parte de las aplicaciones de los algoritmos de aprendizaje automático en numerosos ámbitos de la sociedad hay un desconocimiento de su funcionamiento y entrenamiento, por lo que el riesgo de funcionamiento in- adecuado es alto si simplemente nos limitamos a seguir sus recomendaciones. Además, muchos de estos algoritmos que

121

---

<!-- Página 122 -->

se emplean en la toma de decisiones en el ámbito público no son accesibles para verificar la ausencia de fallos en el código o la presencia de hipótesis incorrectas como las que se han descrito en esta sección.

Mirando al futuro (positivamente)

Querríamos concluir este capítulo un tanto sombrío con una mirada positiva hacia el futuro, mencionando algunos de los principales actores en los aspectos éticos del big data y la IA, así como algunas consideraciones generales. En primer lugar, la principal herramienta para entender las implicaciones sociales de la tecnología es la educación. Los especialistas han de salir de su nicho tecnológico y poner medios para que la sociedad comprenda cómo funcionan los algoritmos en torno a la ciencia de datos. Pero también los ciu- dadanos debemos hacer un esfuerzo por entender el mundo digital —ciertamente complejo—, por lo menos en medida su- ficiente como para protegernos frente a abusos, hacer un uso seguro de él e, idealmente, intentar entender las consecuencias políticas y económicas globales de estas tecnologías. En Europa, la regulación del RGPD que ha entrado en vigor en 2018 es un importante paso adelante para acotar las prácticas salvajes de venta de datos personales, pero su impacto se verá muy redu- cido si no viene acompañada de una campaña de educación. Pues al final, en la práctica, todo será igual que antes con un clic más, el de nuestro consentimiento para almacenar cookies antes de entrar en un sitio web por primera vez. No hemos abordado en este capítulo otro aspecto con- trovertido: los efectos en el mercado laboral de la automatiza- ción que trae consigo la IA. Es difícil cuantificar sus efectos concretos, pero parece evidente que muchos trabajos desapa- recerán, especialmente aquellos más mecánicos y fácilmente automatizables, y otros nuevos serán creados. Es por tanto una amenaza pero también una oportunidad. Siendo prag- máticos, en lugar de discutir sobre su conveniencia, sería más

122

---

<!-- Página 123 -->

conveniente empezar a prepararnos para ello. Hoy en día son escasos los que reivindican el trabajo manual en agricultura, y la revolución industrial que trajo consigo la mecanización de las labores agrícolas no se discute como algo positivo o nega- tivo, sino como algo que simplemente ocurrió. Debemos, además, seguir con atención el papel que las nuevas TIC desempeñen en el terreno político. En países con regímenes totalitarios, los efectos positivos que tiene la comu- nicación en redes sociales para la conquista de libertades civi- les se ven contrarrestados con las posibilidades de control y vigilancia que dichas tecnologías ofrecen a los gobiernos. La comunidad hacker tiene un rol importante en el poder tecno- lógico como contrapeso de los gobiernos y hemos de recordar que solo gracias a denuncias y filtraciones individuales han trascendido a la opinión pública programas abusivos e ilega- les, haciendo posible el debate sobre los mismos. La sociedad está cambiando muy rápidamente y debemos estar alerta pa- ra que no se erosionen con dichos cambios los derechos y li- bertades civiles que tantos siglos hemos tardado en construir.

Para saber más

Hemos hecho un recorrido sobre los aspectos más controver- tidos de la revolución digital. Para aprender más sobre cada una de estas cuestiones recomendamos a los lectores visitar los sitios web de las siguientes organizaciones. 30 El Center for Information Technology Policyde Prin - ceton es un centro interdisciplinar que se ocupa de estudiar el impacto de las TIC en ciencias sociales y políticas públicas. 31 Su blog Freedom to Tinkeres un buen recurso para perma- necer informado sobre estas cuestiones. 32 La Electronic Frontier Foundationes una importante organización sin ánimo de lucro cuyo objetivo es promover la

30. https://citp.princeton.edu/ 31. https://freedom-to-tinker.com 32. https://www.eff.org

123

---

<!-- Página 124 -->

privacidad, la seguridad en las comunicaciones y la libertad de expresión en el mundo digital. En su página web se proponen acciones de movilización para influir sobre la regulación y las normativas que afectan al mundo digital, en contra de la vigi- lancia masiva. Además, hay tutoriales y consejos para comuni- 33 caciones seguras y algún software para evitar el cookie tracking en el navegador. El blog Deeplinks es un buen lugar para man- tenerse informado sobre tecnología y derechos civiles. Mathbabe.org es el blog personal de Cathy O’Neil, cuyo primer post reza nada menos que “me gustaría tener algún día una respuesta a la pregunta: ¿Qué puede hacer un matemáti- co para que este mundo sea un lugar mejor?”. ORCAA (O’Neil Risk Consulting and Algorithmic Auditing) es su proyecto de auditoría tecnológica que ha creado su propio sello para certificar que los algoritmos utilizados por empre- sas y administraciones están libres de sesgos. 34 AI Nowes un instituto de investigación multidiscipli- nar de la Universidad de Nueva York que tiene por objeto estudiar las implicaciones sociales de la IA, centrando su acti- vidad en cuatro líneas: derechos y libertades, aspectos labora- les de la automatización, sesgos e inclusión y seguridad en infraestructuras críticas. Sus informes anuales proporcionan 35 un buen resumen de la actualidad sobre estas cuestiones.

33. El lector interesado en proteger su navegador frente a cookies de terceros puede instalar una extensión elaborada por la Electronic Frontier Foundation (https://www.eff.org/es/node/99095). 34. https://ainowinstitute.org/ 35. En relación con el RGPD se puede consultar https://gdprexplained.eu/ o alguno de los múltiples artículos en internet que explican la nueva normativa.

124

---

<!-- Página 125 -->

CAPÍTULO 8

## A modo de conclusión

Hemos completado nuestra breve singladura por el mar del big data. A través de ella hemos revisado los conceptos funda- mentales de sus metodologías y tecnologías. También he- mos descrito algunas aplicaciones importantes en tres áreas de gran relevancia social en relación con la política y la Administración, la sanidad y la ciberseguridad, mos- trando el potencial impacto positivo de estas disciplinas. Por último, hemos intentado equilibrar nuestro plantea- miento mostrando también algunos de sus riesgos poten- ciales. A modo de resumen nos gustaría concluir con algunas ideas centrales que han dirigido nuestra exposición:

- Es posible que los análisis big data hayan sido de al- guna manera sobrevendidos por las consultoras TIC. Por ejemplo, hemos podido leer expresiones falsas del estilo “el diluvio de datos convierte en obsoleto el método científico” (Anderson, 2008), como si solo necesitásemos recopilar grandes cantidades de datos y, a través de soluciones automatizadas, obtener algún tipo de modelo para tratar cualquier problema que podamos imaginar.

125

---

<!-- Página 126 -->

- Aunque los datos son importantes, debemos reco- nocer que en muchos problemas no habrá tantos. E incluso si los hubiere, aún existe una clara nece- sidad de incluir juicios de expertos y tecnologías analíticas de más bajo nivel en los procesos de toma de decisiones y de simulación de políticas que per- mitan ahorrar dinero antes de implantar soluciones más costosas. - Debemos insistir en que el big data no se refiere solo a tecnología, a Hadoop o Spark, sino que requiere además metodologías científicas de la estadística y del aprendizaje automático, parte de lo que hoy llamaría- mos “ciencia de datos”, y conocimientos sobre la ma- teria en la que se hace un proyecto big data. - De las cinco “uves” que describimos en el capítulo 2 en relación con el big data, normalmente se suele incidir en el aspecto del volumen, las grandes canti- dades de datos, pero quizás es mucho más importante remarcar el aspecto del valor que aportan tales datos. Acumular datos meramente suele ser inútil e inefi- ciente. - Desde el punto de vista tecnológico debemos espe- rar, como no puede ser de otra manera, una evolución permanente en un fenómeno que apenas acaba de co- menzar. - Desde una perspectiva metodológica debemos espe- rar también una importante evolución en lo que se refiere al uso de métodos bayesianos, hoy por detrás de los métodos de máxima verosimilitud en este tipo de problemas. También, debemos esperar mejoras en la integración coherente de estas metodologías en sis- temas de ayuda a la toma de decisiones. - Por lo que respecta a las aplicaciones, por el momen- to han predominado las ideas de negocio, pero hay un enorme potencial en las aplicaciones en el ámbito social para beneficio de las administraciones y las or- ganizaciones no gubernamentales.

126

---

<!-- Página 127 -->

- Finalmente, desde el punto de vista ético, será necesa- ria una mayor concienciación de la población respecto al valor de los datos y una mejor regulación de los aspectos de privacidad.

En todo caso, el futuro ya está aquí. Aprendamos pues a surfear en este mar para el beneficio de nuestra sociedad.

127

---

<!-- Página 128 -->

---

<!-- Página 129 -->

## Bibliografía

alfaRo, C.; Cano-monteRo, J.; Gómez, J.; moGueRza, J. M. y oRteGa, F. (2016): “A multi-stage method for content classification and opinion mining on weblog comments”, Annals of Operations Research, 236(1), pp. 197-213. anDeRson, C. (2008): “The end of the theory: The data deluge makes the scientific method obsolete”, Wired, junio. aRinGhieRi, R.; CaRello, G. y moRale, D. (2016): “Suppor- ting decision making to improve the performance of an Italian Emergency Medical Service”, Annals of Operations Research, 236(1), pp. 131-148. aRRoyo GuaRDeño, D.; Díaz viCo, J. y heRnánDez enCinas, L. (2019): Blockchain, Madrid, CSIC/Los Libros de la Catarata. Banks, D.; Ríos, J. y Ríos insua, D. (2015): Adversarial Risk Analysis, Nueva York, Chapman and Hall/CRC. BiGGio, B. y Roli, F. (2018): “Wild patterns: Ten years after the rise of adversarial machine learning”, Pattern Re - cognition, 84, pp. 317-331. Bishop C. M. (2006): Pattern recognition and machine learning, Nueva York, Springer. B olukBasi, T.; C hanG, K. W.; zou, J. Y.; saliGRama, V. y kalai, A. T. (2016): “Man is to computer program- mer as woman is to homemaker? debiasing word em- beddings”, Advances in Neural Information Processing Systems, pp. 4349-4357.

129

---

<!-- Página 130 -->

BRennan, A.; meieR, P.; puRshouse, R.; Rafia, R.; menG, Y. y hill-maCmanus, D. (2016): “Developing policy analytics for public health strategy and decisions—the Sheffield alcohol policy model framework”, Annals of Operations Research, 236(1), pp. 149-176. BRiDGe, M. (2018): “Cambridge Analytica sends ‘girls’ to en- trap politicians”, The Times, 20 de marzo. BRutlaG, J. D. (2000): “Aberrant Behavior Detection in Time Series for Network Monitoring”, LISA, vol. 14, nº 2000, pp. 139-146. CaiRo, A. (2012): The Functional Art: An introduction to infor- mation graphics and visualization, Indianápolis, New Riders Publishing. Cox, L. A. (2008): “What’s Wrong with Risk Matrices?”, Risk Analysis, 28, pp. 497-512. Dalvi, N.; DominGos, P.; mausam, sanGhai, S. y veRma, D. (2004): “Adversarial classification”, Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining, pp. 99-108. Daniell, K. A.; moRton, A. y Ríos insua, D. (2016): “Policy Analysis and Policy Analytics”, Annals of Operations Research, 1, pp. 1-15. D e montjoye, Y. A.; RaDaelli, L. y sinGh, V. K. (2015): “Unique in the shopping mall: On the reidentifiability of credit card metadata”, Science, 347(6221), pp. 536-539. Donoho, D. (2015): “50 years of Data Science”, en http://cour- ses.csail.mit.edu/18.337/2015/docs/50YearsDataScience.pdf Dunn, W. (1981): Public policy analysis: an introduction, 2ª ed., Englewood Cliffs, Prentice-Hall. Dunson, D. (2018): “Statistics in the big data era: Failures of the machine”, Stats. & Prob. Letters, 136, pp. 4-9. eaGle, N.; pentlanD, A. S. y lazeR, D. (2009): “Inferring friendship network structure by using mobile phone da- ta”, Proceedings of the National Academy of Sciences, 106(36), pp. 15274-15278. esteva, A.; kupRel, B.; novoa, R. A.; ko, J.; swetteR, S. M.; Blau, H. M. y thRun, S. (2017): “Dermatologist-level

130

---

<!-- Página 131 -->

classification of skin cancer with deep neural networks”, Nature, 542(7639), p. 115. finni, T.; hu, M.; kettunen, P.; vilavuo, T. y ChenG, S. (2007): “Measurement of EMG activity with textile electrodes embedded into clothing”, Physiological measu- rement, 28(11), p. 1405. fisCheR, F.; milleR, G. J. y siDney, M. S. (eds.) (2007): Handbook of Public Policy Analysis: Theory, Politics and Methods, Florida, CRC Press. foResteR, J. (1993): Critical Theory, Public Policy, and Plan - ning Practice: Towards a Critical Pragmatism, Albany, NY, State University of New York. Gelman, A.; steRn, H. S.; CaRlin, J. B.; Dunson, D. B.; vehtaRi, A. y RuBin, D. B. (2013): Bayesian data analy- sis, Nueva York, Chapman and Hall/CRC. GinsBeRG, J.; moheBBi, M. H.; patel, R. S.; BRammeR, L.; smolinski, M. S. y BRilliant, L. (2009): “Detecting in- fluenza epidemics using search engine query data”, Nature, 457(7232), p. 1012. GooDfellow, I.; BenGio, Y. y CouRville, A. (2016): Deep learning, vol. 1, Cambridge, MIT Press. Gómez-ullate , D. (2017): “La otra cara del Big Data”, El País, 23 de enero. hastie, T.; tiBshiRani, R. y fRieDman, J. (2009): The elements of statistical learning, Nueva York, Springer. HCDSNS (2019): Historia Clínica Digital del Sistema Nacional de Salud, Informe de Situación, enero. heCkeRman, D. E.; hoRvitz, E. J. y nathwani, B. N. (1992): “Toward normative expert systems: Part I the pathfin- der project”, Methods of Information in Medicine, 31(02), pp. 90-105. hu, J.; shen, L. y sun, G. (2018): “Squeeze-and-excitation networks”, Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 7132-7141. kolleR, D.; fRieDman, N. B aCh, F. (2009): Probabilistic gra- phical models: principles and techniques, Cambridge, MIT Press.

131

---

<!-- Página 132 -->

kRameR, A. D.; GuilloRy, J. E. y hanCoCk, J. T. (2014): “Experimental evidence of massive-scale emotional con- tagion through social networks” Proceedings of the National Academy of Sciences, 201320040. kumaR, A.; nGuyen, V. A. y teo, K. M. (2016): “Commuter cycling policy in Singapore: a farecard data analytics based approach”, Annals of Operations Research, 236(1), pp. 57-73. li, W.; niRei, M. y yamazana, K. (2018): “Value of data: There’s no such thing as a free lunch in the digital economy”, Sixth IMF Statistical Forum, Washington DC, noviembre. lip, G. Y.; nieuwlaat, R.; pisteRs, R.; lane, D. A. y CRijns, H. J. (2010): “Refining clinical risk stratification for pre- dicting stroke and thromboembolism in atrial fibrillation using a novel risk factor-based approach: the euro heart survey on atrial fibrillation”, Chest, 137(2), pp. 263-272. lópez De mántaRas, R. y meseGueR González, p. (2017): Inte- ligencia artificial, Madrid, CSIC/Los Libros de la Catarata. maCafee (2014): Net Losses: Estimating the Global Cost of Cybercrime, Washington DC, Center for Strategic and International Studies. maCkenzie, C. A.; BaRouD, H. y BaRkeR, K. (2016): “Static and dynamic resource allocation models for recovery of interdependent systems: application to the Deepwater Horizon oil spill”, Annals of Operations Research, 236(1), pp. 103-129. maRRuGat, J. et al. (2003): “Estimación del riesgo coronario en España mediante la ecuación de Framingham calibra- da”, Revista española de cardiología, 56(3), pp. 253-261. mayeR, I. S.; van Daalen, C. E. y Bots, P. W. G. (2004): “Perspectives on policy analyses: a framework for un- derstanding and design”, International Journal of Techno- logy, Policy and Management, 4(2), pp. 169-191. menaChe, I. y ozDaGlaR, A. (2011): “Network games: Theo- ry, models, and dynamics”, Synthesis Lectures on Commu- nication Networks, 4(1), pp. 1-159. mozuR P. (2018): “Inside China’s Dystopian Dreams: A.I., Sha- me and Lots of Cameras”, The NewYork Times, 8 de julio.

132

---

<!-- Página 133 -->

naveiRo, R.; ReDonDo, A. y Ríos insua, D. (2019): “Large Scale Automated Forecasting for Monitoring Network Safety and Security”, Applied Stochastic Models in Business and Industry, Nueva York, Cornell University. naveiRo, R.; ReDonDo, A.; Ríos insua, D. y RuGGeRi, F. (2018): Adversarial classification through adversarial risk analysis, Nueva York, Cornell University, arXiv: 1802. 06678. oBeRmeyeR, Z. y emanuel, E. J. (2016): “Predicting the futu- re—big data, machine learning, and clinical medicine”, The New England Journal of Medicine, 375(13), p. 1216. peaRl, J. (2014): Probabilistic reasoning in intelligent systems: networks of plausible inference, Elsevier. piwek, L.; ellis, D. A.; anDRews, S. y joinson, A. (2016): “The rise of consumer health wearables: promises and barriers”, PLoS Medicine, 13(2), e1001953. poltavski, D. V. (2015): “The use of single-electrode wireless EEG in biobehavioral investigations”, Mobile Health Technologies, Nueva York, Humana Press, pp. 375-390. Rathi , R. (2018): “Effect of Cambridge Analytica’s Facebook ads on the 2016 US Presidential Election”, Towards Data Science, 13 de enero. ReDonDo, A.; toRRes, A.; Ríos insua, D. y DominGo, J. (2018): Assessing supply chain cyber risk management, Datalab, ICMAT-CSIC, informe técnico. Rollason, J. C.; outtRim, J. G. y mathuR, R. S. (2014): “A pilot study comparing the DuoFertility® monitor with ultrasound in infertile women”, International journal of women’s health, 6, p. 657. Russakovsky, O. et al. (2015): “Imagenet large scale visual recognition challenge”, International Journal of Computer Vision, 115(3), pp. 211-252. sanDulesCu, V.; anDRews, S.; ellis, D.; Bellotto, N. y mozos, O. M. (2015): “Stress detection using wearable physiological sensors”, International Work-Conference on the Interplay Between Natural and Artificial Computation, Cham, Springer, pp. 526-532.

133

---

<!-- Página 134 -->

sChaRasChkin, A. y mCBRiDe, T. (2016): “Policy analytics and accountability mechanisms: judging the ‘value for money’ of policy implementation”, Annals of Operations Research, 236(1), pp. 39-56. shen, D.; wu, G. y suk, H. I. (2017): “Deep learning in me- dical image analysis” Annual Review of Biomedical Engineering, 19, pp. 221-248. thaleR, R. H. y sunstein, C. R. (2008): Nudge: Improving Decisions about Health, Wealth, and Happiness, New Haven, CT, Yale University Press. wanG, C.; Guo, X.; wanG, Y.; Chen, Y. y liu, B. (2016): “Friend or foe?: Your wearable devices reveal your per- sonal pin”, Proceedings of the 11th ACM on Asia Conference on Computer and Communications Security, ACM Digital Library, pp. 189-200. weBtap (2019): Princeton Web Transparency & Accounta - bility Project. weDel, M. y kannan, P. K. (2016): “Marketing analytics for data-rich environments”, Journal of Marketing, 80, pp. 97-121. wilson, P. W.; D’aGostino, R. B.; levy, D.; BelanGeR, A. M.; silBeRshatz, H. y kannel, W. B. (1998): “Prediction of coronary heart disease using risk factor categories”, Circulation, 97(18), pp. 1837-1847. west, M. y haRRison, J. (2006): Bayesian forecasting and dynamic models, Nueva York, Springer Science & Business Media. wolpeRt, D. H. (1996): “The lack of a priori distinctions between learning algorithms”, Neural computation, 8(7), pp. 1341-1390. yanG, C. C. y hsu, Y. L. (2010): “A review of accelerometry- based wearable motion detectors for physical activity monitoring”, Sensors, 10(8), pp. 7772-7788. zhanG, l.; hu, G.; wanG, L. y Chen, Y. (2016): “A bottom- up biofuel market equilibrium model for policy analy- sis”, Annals of Operations Research, 236(1), pp. 75-101. zomaya, A. Y. y sakR, S. (eds.) (2017): Handbook of Big Data Technologies, Berlín, Springer.

134

---

<!-- Página 135 -->

---

<!-- Página 136 -->

¿QUÉ SABEMOS DE?

# Big data

La captura de datos a través de apli- caciones y teléfonos móviles produce cantidades ingentes de información sobre nuestro día a día online. Es por ello comprensible que dichos datos tengan cada vez más valor, ya que se utilizan para mejorar las relaciones con los ciuda- danos o clientes, personalizar servicios y productos y auto- matizar todo tipo de procesos. Descubrir que estamos cediendo nuestra información personal despierta a menudo el pánico general, pero hasta las actividades más rutinarias —como consultar el tiempo o pasar el robot aspirador— su- ponen la apertura de una ventana a nuestra privacidad; la misma que también hace posible que una aplicación traduz- ca un texto sin mucho esfuerzo o que nuestro móvil nos re- suelva una duda preguntándole a viva voz. En este libro se explican, de manera accesible, los conceptos básicos del big data y la ciencia de datos, algunos de sus beneficios y riesgos, y se promueve un uso responsable de la tecnología.

David Ríos Insua es AXA-ICMAT Chair en ICMAT-CSIC y numerario de la Real Acade- mia de Ciencias. Es premio DeGroot de la ISBA. Sus temas de interés incluyen la in- ferencia bayesiana, la ciencia de datos, el análisis de decisiones y el análisis de ries- gos, y sus aplicaciones a seguridad y ciberseguridad. David Gómez-Ullate Oteiza es investigador distinguido en la Univer- sidad de Cádiz, donde se ocupa de la transferencia de conocimiento al sector industrial. En la actualidad dirige pro- yectos en el sector aeronáutico, biomédico y seguros aplican- do técnicas de visión artificial y procesamiento de lenguaje natural.

I S B N : 9 7 8 - 8 4 - 0 0 - 1 0 5 3 4 - 1