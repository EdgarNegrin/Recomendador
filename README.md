# Recomendador

* Ejemplo de uso:

python3 main.py matriz1.txt -M pearson -V 2 -P media 

Salida:

Matriz Predicciones

5       3       4       4       4.85
3       1       2       3       3
4       3       4       3       5
3       3       1       5       4
1       5       5       2       1

Similaridades con Persona 0
Persona0: 1.0
Persona1: 0.84
Persona2: 0.61
Persona3: 0.0
Persona4: -0.77

Similaridades de los 2 vecinos con Persona 0
Persona1: 0.84
Persona2: 0.61
    
    .
    .
    .


# Descripción del código

Para la realización de este recomendador se ha creado una clase la cual se encargara de todas las operaciones, desde cargar el fichero hasta imprimir los resultados.



Se ha creado un metodo para cada una de las posibles metricas disponibles(Pearson, Coseno, Euclides).

* El metodo que calcula la similitud haciendo uso de la metrica de Pearson comienza recorriendo la matriz, por cada iteración calculamos la similitud entre 2 personas(2 filas).

Debemos obtener los indices de los items que tienen metricas ya que con ellos realizaremos una iteración que calculara los sumatorios expuestos en la ecuación que se nos ha facilitado(3 sumatorios). A continuación debemos calcular las operaciones restantes fuera del sumatorio, el valor resultado(similitud de las dos personas) de la operación se almacena en un atributo matriz en la posicion correspondiente a las personas de las que se esta calculando su similitud.

* El metodo que calcula la similitud haciendo uso de la metrica del coseno comienza recorriendo la matriz de la misma manera que Pearson.

Se realiza todo de la misma manera salvo las operaciones, en esta metrica no haremos uso de la media para realizar el calculo. Seguimos la ecuación proporcionada para el calculo de la similitud y lo almacenamos de igual que anteriormente.

* El metodo que calcula la similitud haciendo uso de la metrica de Euclides comienza estableciendo un flag a 'True' ya que sera necesario a la hora de realizar la ordenación de las similitudes.

Se realiza todo de la misma manera salvo las operaciones, seguimos la ecuación proporcionada para el calculo de la similitud y lo almacenamos de igual que anteriormente.



Se ha creado un metodo para cada una de las posibles predicciones (Simple y haciedo uso de la media).

* La prediccion simple comienza recorriendo los elementos vacios(sin medicion) para cada uno de ellos calcularemos sus vecinos mas proximos dependiendo del numero de vecinos que el usuario pase.
Continuamos recorriendo cada uno de los vecinos mas cercanos para realizar las operaciones pertinentes haciendo uso de las similitudes calculadas anteriormente, en este caso son dos sumatorios(seguimos la ecuacion que se nos proporciono). Por último añadimos ese resultado a la matriz de utilidad.

* La prediccion haciendo uso de la media se realiza de la misma forma salvo el calculo de los sumatorios y sumar al resultado final la media de la persona a la que estamos calculando el item.




Existe un metodo que se encarga de realizar una ordenación de la matriz de similitud para poder usarla a la hora de calcular los vecinos. Para ello recorremos las filas de la matriz similitud enumerando los elementos para tener costancia de que similitud pertenece a cada persona, a continuacion dependiendo del tipo de metrica realizamos un orden creciente o decreciente(en caso de usar la metrica euclidea se usa el orden creciente y los otros casos al contrario).


Un metodo del que se hablo anteriormente es el encargado de calcular los vecinos mas proximos dependiendo del número de vecinos(siempre mayor a 1). Este metodo realiza una copia de la lista ordenada de similitudes, sobre esta lista eliminamos las personas que no tengan valoraciones del item y la propia persona de la que se estan calculado los vecinos.
A partir de la lista modificada y ordenada extraemos los vecinos más cercanos y los añadimos a un atributo para podemos mostrarlos posteriormente.


Se creo un metodo para mostrar en consola la matriz de utilidad resultado, las similitudes con cada una de las personas y los vecinos más cercanos que se calculan para cada persona.


Por último tenemos el metodo encargado de cargar la matriz original, en este metodo también establecemos las medias de cada una de las personas y las valoraciones que estan vacias(almacenamos la persona y el item) para calcularlas posteriormente.