## Ejercicio 3

- [1. Grafo de Estaciones](#1-grafo-de-estaciones)
- [2. Ejecución](#2-ejecución)
- [3. Resultados](#3-resultados)
- [4. Conclusiones](#4-conclusiones)

## 1. Grafo de Estaciones
<img width="574" height="392" alt="Grafo-Ejercicio3" src="https://github.com/user-attachments/assets/0ac0a2c6-283e-48eb-b0fb-1cc64a167f3d" />

## 2. Ejecución
- Ubique su línea de comandos en la carpeta `Ejercicio 3`.
- En la línea de comandos ejecute: `py main.py`.
- Ingrese la estación de salida y llegada. Para saltar esto y usar el caso base _**(A->J)**_, presione `Enter` dos veces.

## 3. Resultados 
Para el análisis de los algoritmos se utilizaron como parámetros la _**Estación A**_ como punto de partida y la _**Estación J**_ como punto de llegada.
Se analizó el tiempo que se demora y cuál fue el uso máximo de memoria que requirió cada algoritmo para llegar a la estación objetivo.<br>
Los resultados encontrados fueron los siguientes:

> ### 3.1 Breadth First Search (_BFS_)
- **Camino de A a J:** [A, C, F, J]
- **Tiempo medio de ejecución:** 0.000617 segundos
- **Máximo uso de memoria (Pico):** 0.011496 MB

> ### 3.2 Iterative Deepening Search (_IDS_)
- **Camino de A a J:** [A, C, F, J]
- **Tiempo medio de ejecución:** 0.000355 segundos
- **Máximo uso de memoria (Pico):** 0.009800 MB

## 4. Conclusiones
La diferencia más clara que se logra ver es que el **Iterative Deepening Search (IDS)** es mucho más eficiente en términos de uso de memoria. Esta diferencia radica en que el _**BFS**_ utiliza un **SET** para almacenar cada uno de los nodos (Estaciones) que va visitando, lo que implica que en grafos muy grandes, el uso de memoria se pueda elevar significativamente.<br><br>
Por otro lado, la diferencia en tiempo de ejecución entre ambos algoritmos es muy relativa y depende mucho de que tan cerca esté la solución al nodo raíz (Estación de partida). En el _**IDS**_, el tiempo de ejecución depende de que tantas iteraciónes debe de hacer para llegar a la "profundidad" donde se encuentra la solución. De acuerdo al grafo en la [sección 1](#1-grafo-de-estaciones), en el caso de buscar la ruta desde la _Estación A_ a la _Estación J_, solamente usamos 3 iteraciones de profundidad, lo cuál lo hace relativamente más eficiente que el _**BFS**_. Pero en algún otro caso donde se requieran más iteraciones, el tiempo de ejecución del _**IDS**_ se aproximará al tiempo del _**BFS**_.
