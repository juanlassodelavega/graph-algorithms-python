import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def _print_mst(self, parent):
        print("Arista\tPeso")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{self.graph[i][parent[i]]}")

    def _min_key(self, key, in_mst):
        min_value = sys.maxsize
        min_index = None

        for v in range(self.V):
            if not in_mst[v] and key[v] < min_value:
                min_value = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        in_mst = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self._min_key(key, in_mst)
            if u is None:
                raise ValueError("El grafo no es conexo; no existe MST completo")

            in_mst[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not in_mst[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self._print_mst(parent)
        total = sum(self.graph[i][parent[i]] for i in range(1, self.V))
        return parent, total


if __name__ == "__main__":
    g = Graph(5)
    g.graph = [
        [0, 6, 0, 1, 0],
        [6, 0, 5, 2, 2],
        [0, 5, 0, 0, 5],
        [1, 2, 0, 0, 1],
        [0, 2, 5, 1, 0],
    ]

    _, total_weight = g.prim_mst()
    print("Peso total del MST:", total_weight)