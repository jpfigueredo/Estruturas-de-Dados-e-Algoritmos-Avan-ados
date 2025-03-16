class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.grafo:
            self.grafo[bairro] = []

    def adicionar_rua(self, bairro1, bairro2):
        if bairro1 in self.grafo and bairro2 in self.grafo:
            self.grafo[bairro1].append(bairro2)
            self.grafo[bairro2].append(bairro1)

    def obter_vizinhos(self, bairro):
        return self.grafo.get(bairro, [])

# Criação do grafo
cidade = Grafo()
bairros = ["Centro", "Zona Norte", "Zona Sul", "Leste", "Oeste", "Bairro Novo"]
for bairro in bairros:
    cidade.adicionar_bairro(bairro)

# Adição das ruas
ruas = [
    ("Centro", "Zona Norte"),
    ("Centro", "Zona Sul"),
    ("Zona Norte", "Zona Sul"),
    ("Zona Norte", "Leste"),
    ("Zona Sul", "Oeste"),
    ("Leste", "Oeste"),
    ("Oeste", "Bairro Novo"),
    ("Zona Norte", "Bairro Novo")
]
for rua in ruas:
    cidade.adicionar_rua(rua[0], rua[1])

# Exemplo de uso: obter vizinhos do Centro
print("Vizinhos do Centro:", cidade.obter_vizinhos("Centro"))
