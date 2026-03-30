def dfs(graph, start):
    if start not in graph:
        raise ValueError(f"El nodo inicial '{start}' no existe en el grafo")

    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        # Se apilan en orden inverso para respetar el orden original al desapilar.
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

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
    traversal = dfs(graph, start_node)
    print("<< PROFUNDIDAD >> nodo de salida -->", start_node)
    print("Recorrido:", " ".join(traversal))