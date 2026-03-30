# Algoritmos de Grafos en Python

Este repositorio contiene implementaciones educativas de algoritmos clasicos de grafos:

- BFS (Breadth-First Search / recorrido en anchura)
- DFS (Depth-First Search / recorrido en profundidad)
- Dijkstra (camino mas corto)
- Prim (arbol de expansion minima) en dos variantes

## Estructura

- `BFSGrafos.py`: recorrido BFS iterativo con cola.
- `DFSGrafos.py`: recorrido DFS iterativo con pila.
- `DijkstraGrafos.py`: grafo con lista de adyacencia y Dijkstra con `heapq`.
- `PrimGrafos1.py`: Prim usando lista de aristas + monticulo (heap).
- `PRIMGrafos2.py`: Prim usando matriz de adyacencia.
- `Grafo.png`: imagen de apoyo del problema/estructura de grafo.

## Requisitos

- Python 3.8 o superior

## Ejecucion

Desde la carpeta del proyecto:

```bash
python3 BFSGrafos.py
python3 DFSGrafos.py
python3 DijkstraGrafos.py
python3 PrimGrafos1.py
python3 PRIMGrafos2.py
```

## Que imprime cada script

- BFS y DFS: nodo de inicio y orden de recorrido.
- Dijkstra: camino mas corto y longitud total desde `A` a cada nodo.
- PrimGrafos1: aristas del MST y costo total.
- PRIMGrafos2: aristas del MST (indices) y peso total.

## Mejoras aplicadas

Se realizaron mejoras para hacer el codigo mas reutilizable y robusto:

- Funciones de recorrido que ahora devuelven resultados (no solo imprimen).
- Validaciones de entrada (por ejemplo, nodo inicial inexistente).
- Bloques `if __name__ == "__main__":` para separar demo y logica reutilizable.
- Correcciones de logica en Prim para casos de conectividad.
- Dijkstra con prioridad (`heapq`) y manejo correcto de casos borde.

## Uso como modulo

Puedes importar funciones/clases sin ejecutar la demo:

```python
from BFSGrafos import bfs
from DFSGrafos import dfs
from DijkstraGrafos import Graph
from PrimGrafos1 import prim
```

## Nota

Estas implementaciones priorizan claridad didactica. Si quieres, se puede extender el proyecto con:

- tests automaticos (`pytest`)
- tipado estatico (`typing`)
- interfaz de linea de comandos
- visualizacion de grafos
