# Recomendador

Nombre: Edgar Negrin Gonzalez  
Correo: alu0101210964@ull.edu.es

* Ejemplo de uso:

python3 main.py ./matriz/matriz1.txt -M pearson -V 3 -P media 

Salida:

Matriz de utilidad  

5       3       4       4       4.86  
3       1       2       3       3  
4       3       4       3       5  
3       3       1       5       4  
1       5       5       2       1  

--------------------------------------------  

Similaridades con Persona 0  
Persona0: 1.0  
Persona1: 0.92  
Persona2: 0.8  
Persona3: 0.5  
Persona4: 0.12  

Similaridades de los 3 vecinos con Persona 0  
Persona1: 0.92  
Persona2: 0.8  
Persona3: 0.5  
    
.
.
.


# Descripción del código

Para la realización de este recomendador se ha creado una clase la cual se encargara de todas las operaciones, desde cargar el fichero hasta imprimir los resultados.


**Atributos**
Los atributos que se han creado para la creación de esta clase son:

* matrix: Matriz utilidad donde se añadiran las predicciones.
* vecinos: Número de vecinos que se van a calcular.
* medias: Medias de cada persona.
* vacios: Personas e items que se encuentra vacio(Tuplas).
* similitud: Matriz de similitud.
* similitudSorted: Matriz de similitud ordenada.
* similitudVecinos: Similitud de vecinos de cada persona.


Se ha creado un metodo para cada una de las posibles metricas disponibles(Pearson, Coseno, Euclides).

* **pearson**: metodo que calcula la similitud haciendo uso de la metrica de Pearson comienza recorriendo la matriz, por cada iteración calculamos la similitud entre 2 personas(2 filas).

Debemos obtener los indices de los items que tienen metricas ya que con ellos realizaremos una iteración que calculara los sumatorios expuestos en la ecuación que se nos ha facilitado(3 sumatorios). A continuación debemos calcular las operaciones restantes fuera del sumatorio, el valor resultado(similitud de las dos personas normalizado) de la operación y por último se almacena en un atributo matriz en la posicion correspondiente a las personas de las que se esta calculando su similitud.

* **coseno**: metodo que calcula la similitud haciendo uso de la metrica del coseno comienza recorriendo la matriz de la misma manera que Pearson.

Se realiza todo de la misma manera salvo las operaciones, en esta metrica no haremos uso de la media para realizar el calculo. Seguimos la ecuación proporcionada para el calculo de la similitud, normalizamos el resultado y lo almacenamos de igual que anteriormente.

* **euclidea**: metodo que calcula la similitud haciendo uso de la metrica de Euclides.

Se realiza todo de la misma manera salvo las operaciones y la nomalizacion(debemos invertir al normalizar para no tener problema con la ordenación ya que a menor distancia mejor deberia ser la similitud), seguimos la ecuación proporcionada para el calculo de la similitud y lo almacenamos de igual que anteriormente(normalizando).



Se ha creado un metodo para cada una de las posibles predicciones (Simple y haciedo uso de la media).

* **prediccionSimple**: comienza recorriendo los elementos vacios(sin medicion) para cada uno de ellos calcularemos sus vecinos mas proximos dependiendo del numero de vecinos que el usuario pase.
Continuamos recorriendo cada uno de los vecinos mas cercanos para realizar las operaciones pertinentes haciendo uso de las similitudes calculadas anteriormente, en este caso son dos sumatorios(seguimos la ecuacion que se nos proporciono). Por último añadimos ese resultado a la matriz de utilidad.

* **prediccionMedia**: se realiza de la misma forma que la simple salvo el calculo de los sumatorios y sumar al resultado final la media de la persona a la que estamos calculando el item.




**similitudSort**: metodo que se encarga de realizar una ordenación de la matriz de similitud para poder usarla a la hora de calcular los vecinos. Para ello recorremos las filas de la matriz similitud enumerando los elementos para tener costancia de que similitud pertenece a cada persona y ordenamos haciendo uso de *sort*.


**vecinosProximos**: metodo del que se hablo anteriormente es el encargado de calcular los vecinos mas proximos dependiendo del número de vecinos(siempre mayor a 2). Este metodo filtra los vecinos para que no exista ninguno que no tenga la valoracion del item.
A partir de la lista modificada y ordenada extraemos los vecinos más cercanos y los añadimos a un atributo para podemos mostrarlos posteriormente.


**showInfo**: metodo para mostrar en consola la matriz de utilidad resultado, las similitudes con cada una de las personas, los vecinos más cercanos que se calculan para cada persona y las predicciones realizadas de cada item.


**loadFile**: metodo encargado de cargar la matriz original, en este metodo también establecemos las medias de cada una de las personas y las valoraciones que estan vacias(almacenamos la persona y el item) para calcularlas posteriormente.


**NOTA**: para el calculo de la media se han usado todos los items valorados por cada persona.