from collections import defaultdict
from heapq import heapify, heappop, heappush


def prim(grafo):
    nodos = grafo.get("nodos", [])
    aristas = grafo.get("aristas", [])
    if not nodos:
        return []

    conexiones = defaultdict(list)
    for costo, n1, n2 in aristas:
        conexiones[n1].append((costo, n1, n2))
        conexiones[n2].append((costo, n2, n1))

    inicio = nodos[0]
    usados = {inicio}
    candidatas = conexiones[inicio][:]
    heapify(candidatas)

    recorrido = []
    while candidatas and len(usados) < len(nodos):
        costo, n1, n2 = heappop(candidatas)
        if n2 in usados:
            continue

        usados.add(n2)
        recorrido.append((costo, n1, n2))
        for arista in conexiones[n2]:
            if arista[2] not in usados:
                heappush(candidatas, arista)

    if len(usados) != len(nodos):
        raise ValueError("El grafo no es conexo; no existe un arbol de expansion minimo completo")

    return recorrido


if __name__ == "__main__":
    grafo = {
        "nodos": ["A", "B", "C", "D", "E", "F"],
        "aristas": [
            (10, "A", "B"),
            (25, "A", "D"),
            (30, "B", "C"),
            (10, "B", "D"),
            (12, "C", "E"),
            (5, "D", "E"),
            (20, "D", "F"),
            (40, "E", "F"),
        ],
    }

    mst = prim(grafo)
    costo_total = sum(costo for costo, _, _ in mst)
    print("Prim:", mst)
    print("Costo total:", costo_total)