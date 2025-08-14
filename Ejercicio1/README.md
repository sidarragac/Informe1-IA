# Ejercicio 1

- [1. Análisis del problema](#1-análisis-del-problema)
- [2. Aplicación del algoritmo A*](#2-aplicación-del-algoritmo-a)
- [3. Por qué la ruta encontrada es óptima](#3-por-qu-la-ruta-encontrada-es-óptima)

## 1. Análisis del problema
El problema consiste en encontrar la ruta más corta entre dos ciudades de un mapa, partiendo desde un punto inicial (Arad) hasta un destino (Bucharest).

En este caso, el mapa se modela como un grafo ponderado, donde:
- Los nodos son las ciudades.
- Las aristas representan carreteras entre ciudades.
- Los pesos de las aristas indican la distancia entre ellas.

El reto es encontrar el camino con el menor coste total considerando que:

- No se debe visitar repetidamente nodos ya explorados (evitar ciclos).

- Se debe tomar en cuenta tanto el costo recorrido hasta el momento como una estimación del costo restante hasta la ciudad objetivo.

## 2. Aplicación del algoritmo A*
El algoritmo A* combina dos conceptos:
1. Búsqueda de costo uniforme (Uniform Cost Search): Minimiza la distancia recorrida hasta el momento.
2. Búsqueda heurística (Greedy Search): Prioriza nodos que parecen más cercanos a la ciudad objetivo.

Para cada nodo, A* calcula: f(n) = g(n) + h(n) donde:

- g(n): Costo real acumulado desde el inicio hasta n.
- h(n): Estimación heurística de la distancia desde n hasta la ciudad objetivo.
- f(n): Suma de ambos valores, usada como criterio de prioridad.

En este código:
- g(n) se actualiza sumando el costo real de cada acción (path_cost).
- h(n) se obtiene del diccionario target_distance, que contiene la distancia en línea recta a la ciudad objetivo.
- La frontera se implementa como una cola de prioridad (heapq) para siempre expandir el nodo con menor f(n).

## 3. ¿Por qué la ruta encontrada es óptima?
La ruta es óptima porque:
1. La heurística usada (h(n)) nunca sobreestima la distancia real a la ciudad objetivo (en este caso, usa distancias en línea recta).
2. La heurística también es consistente (o monótona), lo que significa que cumple: h(n) ≤ costo(n, n') + h(n'). Esto garantiza que una vez que un nodo se expande, ya se ha encontrado el camino más corto hacia él.
3. El algoritmo siempre elige expandir el nodo con menor f(n), asegurando que cuando llega a la ciudad objetivo, lo hace por el camino de menor costo posible.
Por lo tanto, A* garantiza encontrar la ruta más corta siempre que la heurística sea admisible y consistente, como en este caso.