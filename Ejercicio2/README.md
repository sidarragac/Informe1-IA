# Ejercicio 2
## 1. Resolver el ejercicio planteado.
Se toma como base el código suministrado por el profesor y se realizan las siguientes modificaciones para completar el ejercicio:

- Se agrega el atributo action a la clase Node para poder determinar la ruta recorrida: Up, Down, Left, Right.
- Se define la clase Problem: se le agregan los atributos de initial (posición inicial), goal (posición objetivo), actions (conjunto de acciones que se pueden realizar).
- En la función find_exit se agrega el diccionario de acciones, donde la clave es el cambio de posición que se debe realizar en el maze y el valor es el nombre de dicho movimiento.
- En la función get_neighbors se modifica la variable neighbors (que era una lista) y se convierte en un diccionario para guardar no solo los vecinos a los cuales se puede mover, sino también la acción que hay que realizar para llegar a ese vecino (Up, Down, Left o Right).
- Finalmente, en la función reconstruct_path, se agregó la lógica para reconstruir también el conjunto de acciones realizadas para llegar de la posición inicial a la final.