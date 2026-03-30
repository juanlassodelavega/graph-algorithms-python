import heapq
from collections import defaultdict


class Graph:
    def __init__(self, edges):
        self.adj = defaultdict(dict)
        for edge in edges:
            if len(edge) not in (2, 3):
                raise ValueError(f"Formato de arista invalido: {edge}")
            start, end = edge[0], edge[1]
            cost = edge[2] if len(edge) == 3 else 1
            if cost < 0:
                raise ValueError("Dijkstra no admite aristas con costo negativo")
            self.adj[start][end] = cost
            # Asegura que el nodo destino exista en la estructura.
            self.adj.setdefault(end, {})

    @property
    def vertices(self):
        return set(self.adj.keys())

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        if cost < 0:
            raise ValueError("Dijkstra no admite aristas con costo negativo")
        if n2 in self.adj[n1]:
            raise ValueError(f"La arista {n1} -> {n2} ya existe")

        self.adj[n1][n2] = cost
        self.adj.setdefault(n2, {})
        if both_ends:
            self.adj[n2][n1] = cost

    def remove_edge(self, n1, n2, both_ends=True):
        self.adj.get(n1, {}).pop(n2, None)
        if both_ends:
            self.adj.get(n2, {}).pop(n1, None)

    def dijkstra(self, source, dest):
        if source not in self.vertices:
            raise ValueError(f"El nodo origen '{source}' no existe")
        if dest not in self.vertices:
            raise ValueError(f"El nodo destino '{dest}' no existe")

        distances = {vertex: float("inf") for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        distances[source] = 0

        heap = [(0, source)]
        while heap:
            current_distance, node = heapq.heappop(heap)
            if current_distance > distances[node]:
                continue
            if node == dest:
                break

            for neighbor, weight in self.adj[node].items():
                candidate = current_distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    previous[neighbor] = node
                    heapq.heappush(heap, (candidate, neighbor))

        if distances[dest] == float("inf"):
            return [], float("inf")

        path = []
        current = dest
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path, distances[dest]


def print_dijkstra_and_length(graph, start, end):
    path, length = graph.dijkstra(start, end)
    if not path:
        print(f"No existe camino de '{start}' a '{end}'")
        return

    path_text = " -> ".join(path)
    print(
        f"Camino mas corto de '{start}' hasta '{end}': {path_text} | longitud: {length}"
    )


if __name__ == "__main__":
    graph = Graph(
        [
            ("A", "B", 10),
            ("A", "D", 7),
            ("A", "C", 4),
            ("B", "A", 10),
            ("B", "D", 2),
            ("B", "E", 10),
            ("C", "A", 4),
            ("C", "D", 2),
            ("C", "F", 3),
            ("D", "C", 2),
            ("D", "A", 7),
            ("D", "B", 2),
            ("D", "G", 5),
            ("E", "B", 10),
            ("E", "G", 2),
            ("F", "C", 3),
            ("F", "G", 5),
            ("G", "F", 5),
            ("G", "D", 5),
            ("G", "E", 2),
        ]
    )

    for destination in ("A", "B", "C", "D", "E", "F", "G"):
        print_dijkstra_and_length(graph, "A", destination)