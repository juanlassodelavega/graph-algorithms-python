# Algoritmos de Grafos en Python

Este repositorio contiene implementaciones educativas de algoritmos clasicos de grafos:

- BFS (Breadth-First Search / recorrido en anchura)
- DFS (Depth-First Search / recorrido en profundidad)
- Dijkstra (camino mas corto)
- Prim (arbol de expansion minima) en dos variantes

## Estructura

```
.
├── src/
│   ├── bfs.py          # Recorrido BFS iterativo con cola
│   ├── dfs.py          # Recorrido DFS iterativo con pila
│   ├── dijkstra.py     # Grafo con lista de adyacencia y Dijkstra con heapq
│   ├── prim_heap.py    # Prim usando lista de aristas + monticulo (heap)
│   └── prim_matrix.py  # Prim usando matriz de adyacencia
├── tests/              # Tests automaticos (por agregar)
├── assets/
│   └── grafo.png       # Imagen de apoyo del problema/estructura de grafo
└── README.md
```

## Requisitos

- Python 3.8 o superior

## Ejecucion

Desde la carpeta del proyecto:

```bash
python3 src/bfs.py
python3 src/dfs.py
python3 src/dijkstra.py
python3 src/prim_heap.py
python3 src/prim_matrix.py
```

## Que imprime cada script

- `bfs.py` y `dfs.py`: nodo de inicio y orden de recorrido.
- `dijkstra.py`: camino mas corto y longitud total desde `A` a cada nodo.
- `prim_heap.py`: aristas del MST y costo total.
- `prim_matrix.py`: aristas del MST (indices) y peso total.

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
from src.bfs import bfs
from src.dfs import dfs
from src.dijkstra import Graph
from src.prim_heap import prim
```

## Nota

Estas implementaciones priorizan claridad didactica. Si quieres, se puede extender el proyecto con:

- tests automaticos (`pytest`)
- tipado estatico (`typing`)
- interfaz de linea de comandos
- visualizacion de grafos
