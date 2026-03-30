from collections import deque


def bfs(graph, start):
    if start not in graph:
        raise ValueError(f"El nodo inicial '{start}' no existe en el grafo")

    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    graph = {
        "0": ["1", "3"],
        "1": ["0", "2", "4"],
        "2": ["0", "1", "5"],
        "3": ["0", "4", "5"],
        "4": ["1", "3", "5"],
        "5": ["2", "3"],
    }
    start_node = "5"
    traversal = bfs(graph, start_node)
    print("<< ANCHURA >> nodo de salida -->", start_node)
    print("Recorrido:", " ".join(traversal))