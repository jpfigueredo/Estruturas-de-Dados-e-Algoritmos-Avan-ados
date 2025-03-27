import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, nome):
        if nome not in self.vertices:
            self.vertices[nome] = {}
    
    def adicionar_conexao(self, origem, destino, distancia):
        self.vertices[origem][destino] = distancia # Adiciona para grafos direcionados
        self.vertices[destino][origem] = distancia  # Remove para grafos direcionados

def dijkstra(grafo, inicio):
    # Inicialização das estruturas
    distancias = {vertice: float('infinity') for vertice in grafo.vertices}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]
    anteriores = {vertice: None for vertice in grafo.vertices}
    
    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        
        # Se já encontramos um caminho melhor, ignoramos
        if distancia_atual > distancias[vertice_atual]:
            continue
            
        for vizinho, peso in grafo.vertices[vertice_atual].items():
            distancia_candidata = distancia_atual + peso
            
            # Se encontramos um caminho melhor
            if distancia_candidata < distancias[vizinho]:
                distancias[vizinho] = distancia_candidata
                anteriores[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (distancia_candidata, vizinho))
    
    return distancias, anteriores

def reconstruir_caminho(anteriores, inicio, destino):
    caminho = []
    atual = destino
    
    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]
    
    caminho.reverse()
    return caminho if caminho[0] == inicio else []

# Exemplo de uso
if __name__ == "__main__":
    # Criação do grafo
    g = Grafo()
    vertices = ['A', 'B', 'C', 'D', 'E']
    
    for v in vertices:
        g.adicionar_vertice(v)
    
    conexoes = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 5),
        ('B', 'D', 10),
        ('C', 'D', 3),
        ('D', 'E', 4),
        ('E', 'B', 3)
    ]
    
    for conexao in conexoes:
        g.adicionar_conexao(*conexao)
    
    # Execução do algoritmo
    inicio = 'A'
    distancias, anteriores = dijkstra(g, inicio)
    
    # Exibição dos resultados
    print(f"Centro de distribuição: {inicio}\n")
    print("{:<10} {:<15} {:<15}".format("Bairro", "Distância Mínima", "Caminho"))
    print("-" * 40)
    
    for vertice in vertices:
        if vertice == inicio:
            continue
        caminho = reconstruir_caminho(anteriores, inicio, vertice)
        if distancias[vertice] != float('infinity'):
            print("{:<10} {:<15} {:<15}".format(
                vertice,
                distancias[vertice],
                " → ".join(caminho)
            ))
        else:
            print("{:<10} {:<15} {:<15}".format(vertice, "Inacessível", ""))