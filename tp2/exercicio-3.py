grafo = {
    'Centro': ['Bairro A', 'Bairro B'],
    'Bairro A': ['Centro', 'Bairro C'],
    'Bairro B': ['Centro', 'Bairro C'],
    'Bairro C': ['Bairro A', 'Bairro B', 'Bairro D'],
    'Bairro D': ['Bairro C']
}

def obter_vizinhos(bairro):
    return grafo.get(bairro, [])

bairro = 'Bairro C'
vizinhos = obter_vizinhos(bairro)
print(f'Bairros vizinhos ao {bairro}: {vizinhos}')
