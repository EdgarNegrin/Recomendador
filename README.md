# Recomendador

Ejemplo de uso:

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


Descripción del código

Para la realización de este recomendador se ha creado una clase la cual se encargara de todas las operaciones, desde cargar el fichero hasta imprimir los resultados