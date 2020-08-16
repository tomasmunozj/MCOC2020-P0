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
   
  * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/entrega6.png?raw=true)
  * ![alt text](https://github.com/tomasmunozj/MCOC2020-P0/blob/master/entrega_6.png?raw=true)
  
  
  
  
  
  
