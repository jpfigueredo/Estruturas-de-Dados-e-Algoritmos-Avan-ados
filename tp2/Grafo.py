from collections import deque

class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_conexao(self, centro1, centro2, peso=0):
        if centro1 not in self.adjacencia:
            self.adjacencia[centro1] = []
        if centro2 not in self.adjacencia:
            self.adjacencia[centro2] = []
        self.adjacencia[centro1].append((centro2, peso))
        self.adjacencia[centro2].append((centro1, peso))

    def obter_vizinhos(self, centro):
        return self.adjacencia.get(centro, [])

    def exibir_grafo(self):
        for centro, conexoes in self.adjacencia.items():
            print(f"{centro}: {conexoes}")

def bfs(grafo, inicio, destino):
    fila = deque([(inicio, [inicio], 0)])
    visitados = set()

    while fila:
        centro_atual, caminho, custo_total = fila.popleft()

        if centro_atual == destino:
            return caminho, custo_total

        if centro_atual not in visitados:
            visitados.add(centro_atual)
            for vizinho, peso in grafo.obter_vizinhos(centro_atual):
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho], custo_total + peso))

    return None, float('inf')

g = Grafo()

g.adicionar_conexao('A', 'B', 2)
g.adicionar_conexao('A', 'C', 3)
g.adicionar_conexao('B', 'D', 4)
g.adicionar_conexao('C', 'E', 1)
g.adicionar_conexao('D', 'E', 2)


for centro in ['A', 'B', 'C', 'D', 'E']:
    vizinhos = g.obter_vizinhos(centro)
    print(f"Vizinhos de {centro}: {vizinhos}")

caminho, custo = bfs(g, 'A', 'E')
print(f"Caminho encontrado: {caminho} com custo total de {custo} horas")
