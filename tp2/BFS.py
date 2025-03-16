from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    ordem_visita = []
    fila = deque([inicio])
    
    visitados.add(inicio)
    
    while fila:

        vertice = fila.popleft()
        ordem_visita.append(vertice)
        
        for vizinho in grafo.get(vertice, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    
    return ordem_visita

grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G'],
    'D': ['A'],
    'E': ['B'],
    'F': ['B'],
    'G': ['C']
}

ordem = bfs(grafo, 'A')
print("Ordem dos vértices visitados pela BFS:", ordem)
