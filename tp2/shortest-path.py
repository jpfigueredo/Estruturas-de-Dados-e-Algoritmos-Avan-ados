from collections import deque

def bfs_ordem_visita(grafo, inicio):
    visitados = []
    fila = deque([inicio])
    
    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            visitados.append(vertice)
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    fila.append(vizinho)
    return visitados

ordem = bfs_ordem_visita(grafo, 'A')
print("Ordem de visita:", ordem)


def bfs_caminho(grafo, inicio, destino):
    fila = deque([(inicio, [inicio])])
    visitados = []
    
    while fila:
        (vertice, caminho) = fila.popleft()
        
        if vertice not in visitados:
            visitados.append(vertice)
            
            if vertice == destino:
                return visitados, caminho
            
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    novo_caminho = list(caminho)
                    novo_caminho.append(vizinho)
                    fila.append((vizinho, novo_caminho))
    
    return visitados, []

ordem_visita, caminho_mais_curto = bfs_caminho(grafo, 'A', 'F')
print("Ordem de visita:", ordem_visita)
print("Caminho mais curto de A até F:", caminho_mais_curto)
