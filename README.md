# TOMÁS MUÑOZ JIMENEZ

## MCOC2020-P0

# ENTREGA1

## MI COMPUTADOR : 
* Nombre del modelo :                MacbookAir 7,2
* Año de adquisición :               2018
* Tipo :                             Notebook

* PROCESADOR :
  * Nombre del procesador :            Dual-Core Intel Core i5
  * Velocidad del procesador :         1,8 GHz
  * Velocidad Máxima :                 2,7 con turboBoost
  * Cantidad de procesadores :         1
  * Generación del procesador :        5ºta
  * Cantidad total de núcleos :        2
  * Número de hilos :                  4
  * Arquitectura :                     X86

* TAMAÑO DE LAS CACHÉS :
  * Caché de nivel 2(por núcleo) :     256 KB
  * Caché de nivel 3 :                 3 MB

* MEMORIA :
  * Total :                            8 GB
  * Tipo de memoria :                  DDR3
  * Velocidad :                        1600 MHz

* RED/WIFI :
  * Proveedor internet :               VTR Banda ancha S.A
  * Dirección IP wifi :                192.168.50.57
  * Dirección IP router :              192.168.50.1
  * Tipo de tarjeta :                  AirPort Extreme  (0x14E4, 0x117)
  * Dirección MAC :                    14:c2:13:0b:2e:34

* GRAFICOS :
  * Modelo de chipset :                Intel HD Graphics 6000
  * Tipo :                             GPU
  * VRAM (dinámico, máximo) :          1536 MB

* OTROS :
  * Unidad de estado sólido SSD :      128 GB
 
# ENTREGA 2 

## DESEMPEÑO MATMUL  
  ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/grafico%20corridas.png?raw=true)
  
  * ¿Como difiere del gráfico del profesor/ayudante? :
  
    * Para el caso del gráfico de tiempo transcurrido, existen diferencias notorias al principio de este, especialmente para el primer punto (N=3) de algunas    corridas. Esta diferencia es que en el gráfico obtenido por el alumno se demora más que el obtenido por el profesor/ayudante. Luego de el primer punto el gráfico comienza a ser practicamente igual, claramente aumentando el tiempo a medida que aumenta el tamaño de la matriz.
    * Para el caso del gráfico de memoria utilizada, los gráficos son practicamente iguales, por lo que no se presentan diferecias entre el gráfico del alumno, con el del profesor/ayudante.
    
  * ¿A qué se pueden deber las diferencias? :
  
    * En mi caso, la diferencia del gráfico tiempo transcurrido, se pueden deber a que el computador del profesor/ayudante es mucho más potente que el computador del alumno, por lo que al ejecutar el codigo, este presente demoras en comenzar a correr. 
    
  * El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser? :
  
    * Esto se debe a que en el gráfico de uso de memoria, esta se calculo mediante una formula, asumiendo que cada componente usa 8 bytes, por lo que independiente de la matriz, siempre se utilizará la formula para el calcula de la memoria, por lo que siempre será lineal.
    * Por otro lado, en el gráfico de tiempo transcurrido, este no es lineal, ya que va a depender de varios factores que serán distintos para cada computador, memoria, procesadores, nucleos, etc.
    
  * ¿Qué versión de python está usando? :
  
    * Python 3.8.1 
    
  * ¿Qué versión de numpy está usando? :
  
    * 1.18.5
    
  * Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar :
  
    * En mi caso, mi computador (macbookAir) tiene sólo un procesador, es decir, dos nucleos, cómo podemos ver en las siguientes imagenes, en la ejecución del codigo se utiliza el único procesador que tiene el computador.
  
    * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/Captura%20de%20Pantalla%202020-08-07%20a%20la(s)%2022.47.18.png?raw=true)
    
    * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/Captura%20de%20Pantalla%202020-08-07%20a%20la(s)%2022.46.58.png?raw=true)
  
  
  # ENTREGA 3 

## DESEMPEÑO MIMATMUL 
  
  * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/filename.png?raw=true)
  
  * ¿Como difiere del gráfico del profesor/ayudante? :
  
    * Para el caso del gráfico de tiempo transcurrido,las diferencias que existen son mínimas, ya que el gráfico es identico al del profesor/ayudante, con excepcion al principio, ya que en mi caso, mi computador no presenta ese gran bumps inicial, si no que tiende a ser aumentar "linealmente" desde el principio.
    * Para el caso del gráfico de memoria utilizada, los gráficos son practicamente iguales, por lo que no se presentan diferecias entre el gráfico del alumno, con el del profesor/ayudante.
    
  * ¿A qué se pueden deber las diferencias? :
  
    * En este caso, la minima diferencia del gráfico tiempo transcurrido, se puede deber a la rapida reacción del procesador de mi computador para correr el codigo, talvez porque en el momento de correr el codigo no se tenía nada abierto en el computador que interrumpa este.
    
  * El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser? :
  
    * Esto se debe a que en el gráfico de uso de memoria, esta se calculo mediante una formula, asumiendo que cada componente usa 8 bytes, por lo que independiente de la matriz, siempre se utilizará la formula para el calcula de la memoria, por lo que siempre será lineal.
    * Por otro lado, en el gráfico de tiempo transcurrido, este no es lineal, ya que va a depender de varios factores que serán distintos para cada computador, memoria, procesadores, nucleos, actividades realizando en el momento, etc
    
  * ¿Qué versión de python está usando? :
  
    * Python 3.8.1 
    
  * ¿Qué versión de numpy está usando? :
  
    * 1.18.5
    
  * Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar :
  
    * En mi caso, mi computador (macbookAir) tiene sólo un procesador, es decir, dos nucleos, cómo podemos ver en las siguiente imagen, en la ejecución del codigo se utiliza el único procesador que tiene el computador.
    
    * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/Captura%20de%20Pantalla%202020-08-10%20a%20la(s)%2022.02.50.png?raw=true)
  
  # ENTREGA4 :
  
  ### Comentarios :
  
  * Lo primero, fue realizar tres casos en esta entrega, en donde cada caso constaba de 4 archivos de python con sus respectivos graficos, el caso 1 se realizo mediante numpy, mientras que los casos 2 y 3 fueron realizados mediante scipy.
  
  * Como se pueden observar en los graficos subidos en el repositorio, las funciones "numpy.linalg.inv"  y "scipy.linalg.inv" son relativamente iguales en terminos de desempeño, practicamente los graficos son iguales y las diferencias que presentan son minimas. En terminos de procesador, en mi caso las dos funciones usan el único procesador presente en mi computador, llegando a usar incluso más del 100% de él en su máximo. Tambien hubieron "bumbs" en terminos de procesador, ya que muchas veces variaba el porcentaje de utilizacion del procesador, variando entre 60% hasta 130%.
  
  * En terminos de memoria, es evidente que mientras más pesados sean los tipos de datos, más bytes se utilizaran en la ejecución del codigo y por lo tanto más tiempo se demorara en la ejecucion de esta.
  
  * Por otro lado, la funcion overwrite_a=True de scipy resultó en una ganancia de desempeño, la cual fue muy mínima. Si bien ayudo en tiempo, en terminos de procesador resulto usando mas del 100% al igua que sin la funcion overwrite, por lo la ayuda fue diminuta.
  
  * En las siguientes imagenes, se pueden observar desempeños de mi procesador en la ejecucion del codigo, en donde se aprecian las variaciones de procentaje mencionadas anteriormente :
  
   * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/Captura%20de%20Pantalla%202020-08-12%20a%20la(s)%2023.55.16.png?raw=true)
   
   * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/Captura%20de%20Pantalla%202020-08-12%20a%20la(s)%2023.55.21.png?raw=true)
  
    
  * ¿Qué algoritmo de inversión cree que utiliza cada método? 
      
    * El metodo utilizado de inversion de matriz es linalg.inv importado mediante from scipy import linalg, es decir, un metodo de algebra lineal que proporcionan implementaciones eficientes de bajo nivel. Estas bibliotecas son multiprocesos, por lo que dependen del procesador del computador.
      * Fuente : https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg
      
    * ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? (Ver clase 10 Agosto)
    
      *
      
  # ENTREGA5 :
  
  ### ALGUNOS COMENTARIOS DE LA TAREA : 
  
  * Como se puede apreciar en el gráfico, y como es de esperarse, el método de resolver Ax=b resulta en una pequeña ganancia de desempeño al aumentar el tamaño de la matriz con el solver de numpy. En un principio, la resolución de Ax=b, para matrices de tamaño pequeño, resulta un poco más rápido con python puro, pero ya al ir aumentando el tamaño de la matriz, comienza a obtener ventaja el método con numpy, para luego, tamaños muy grandes, encontrar un balance entre el método de python puro y el solver de numpy.
  
  
  * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/ENTREGA5.png?raw=true)
  
  # ENTREGA6
  
  ### ALGUNOS COMENTARIOS DE LA ENTREGA : 
  
  * En esta entrega, para el desempeño Ax=b con diferentes solvers de numpy y principalmente scipy, se utilizaron en mi caso, 4 solvers de scipy, 1 solver de numpy, y un comando de scipy llamado Inv. 
  
  * los solvers utilizados de scipy fueron :
     * solver de scipy con symmetric
     * solver de scipy con overwrite
     * solver de scipy con check_finite
     * solver de scipy 
     * scipy con metodo Inv
     * solver de numpy
     
  * lo que realiza simmetric es convertir la matriz A en una matriz simetrica y definida positiva
  * overwrite permite sobreescribir datos, lo que podría convertirse en una mejora de rendimiento.
  * check_finite lo que realiza es chequear que las matrices de entrada contengan sólo números finitos
  * por otro lado, el solver de scipy y numpy sin ningun parametro, resuelve el sistema de manera normal. sin embargo, si la matriz de datos es de algún tipo particular, la cadena de datos asume automaticamente eso.
  
  * Como se puede apreciar en el grafico y como es de esperarse, (solo en algunos casos), el solver scipy sin parametro, es el metodo de resolucion más lenta para una matriz de tamaño menor a 10. para matrices de tamaño alto(matrices mayor a 1000) se observa que el a pesar de que todos los solvers tienden a un equilibrio en terminos de demora, los más lentos son el metodo de INV de scipy y tambien en menor medida, sigue apareciendo el solver de scipy sin parametro. Por otro lado, el solver que se mantuvo más constante, y relativamente más rapido fue el solver de scipy con parametro symmetric, lo cual era de esperarse que se obtuviera una ganancia de desempeño(minima). Tambien el solver que reacciono más rapido para matrices muy pequeñas(menor a 10) fue el solver de numpy.
  * Finalmente se concluye, en base a las diferentes corridas que el alumno hizo antes de presentar el trabajo, que el metodo de symmetric, puede generar una ganancia de desempeño, independiente el tamaño de la matriz, y que a matrices de tamaño elevadas, el metodo de INV de scipy es el que más demora.
   
  ### FOTOS DEL DESEMPEÑO DE MI PROCESADOR, NUCLEOS, MEMORIA ETC
  
   * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/Captura%20de%20Pantalla%202020-08-17%20a%20la(s)%2010.31.56.png?raw=true)
   
   * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/Captura%20de%20Pantalla%202020-08-17%20a%20la(s)%2010.33.19.png?raw=true)
 
  ### GRAFICO : 
   
  * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/ENTREGA6.png?raw=true)
  
  # ENTREGA 7
  
  # MATRICES DISPERSAS Y COMPLEJIDAD COMPUTACIONAL 
  
  ## COMPLEJIDAD ALGORITMICA DE MATMUL :
  
  ### GRAFICO MATRIZ LLENA:
  
   ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/MATMUL%20M%20LLENA.png?raw=true)
  
  ### GRAFICO MATRIZ DISPERSA:
  
   ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/MATMUL%20M%20DISPERSO.png?raw=true)
  
  ## PREGUNTAS:
  
   * Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.
   
   * ¿Cual parece la complejidad asintótica N→∞  para el ensamblado y solución en ambos casos y porqué?
   
   * ¿Como afecta el tamaño de las matrices al comportamiento aparente?
   
   * ¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?
   
  
  ## COMPLEJIDAD ALGORITMICA DE SOLVER :
  
  ### GRAFICO MATRIZ LLENA:
  
   ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/SOLVE%20M%20LLENA.png?raw=true)
 
  ### GRAFICO MATRIZ DISPERSA:
  
   ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/SOLVE%20M%20DISPERSA.png?raw=true)
  
   ## PREGUNTAS:
  
   * Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.
   
   * ¿Cual parece la complejidad asintótica N→∞  para el ensamblado y solución en ambos casos y porqué?
   
   * ¿Como afecta el tamaño de las matrices al comportamiento aparente?
   
   * ¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?
  
  
  ## COMPLEJIDAD ALGORITMICA DE INV :
  
  ### GRAFICO MATRIZ LLENA:
  
   ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/INV%20M%20LLENA.png?raw=true)
  
  ### GRAFICO MATRIZ DISPERSA:
  
   ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/INV%20M%20DISPERSA.png?raw=true)
  
   ## PREGUNTAS:
  
   * Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.
   
   * ¿Cual parece la complejidad asintótica N→∞  para el ensamblado y solución en ambos casos y porqué?
   
   * ¿Como afecta el tamaño de las matrices al comportamiento aparente?
   
   * ¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?
  

  
  
  
  
  
  
