graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [6],
    5: [6],
    6: []
}

def dfs(graph, start, visited=None):
    """
    Realiza a busca em profundidade (DFS) a partir do vértice 'start'.
    A função visita recursivamente cada vértice, explorando
    completamente cada ramo antes de retroceder.
    
    Ordem de visita (considerando ordem dos vizinhos em lista): 
    Para o grafo dado, a ordem esperada é: 1, 2, 4, 6, 3, 5.
    """
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

from collections import deque

def bfs(graph, start):
    """
    Realiza a busca em largura (BFS) a partir do vértice 'start'.
    A função utiliza uma fila (queue) para visitar todos os vértices
    em ordem de proximidade (níveis) em relação ao vértice inicial.
    
    Ordem de visita esperada para o grafo dado: 1, 2, 3, 4, 5, 6.
    """
    visited = []
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

dfs_order = dfs(graph, 1)
bfs_order = bfs(graph, 1)

print("Ordem de visitação com DFS:", dfs_order)
print("Ordem de visitação com BFS:", bfs_order)