def detect_cycle_dfs(graph):
    """
    Detecta se existe algum ciclo em um grafo direcionado representado
    por um dicionário de listas de adjacência.

    :param graph: dicionário { nó: [lista_de_adj] }
    :return: True se existir ciclo, False caso contrário
    """

    visited = set()
    rec_stack = set()

    def dfs(v):
        visited.add(v)
        rec_stack.add(v)

        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(v)
        return False

    for node in graph.keys():
        if node not in visited:
            if dfs(node):
                return True 

    return False 


if __name__ == "__main__":
    transactions = {
        "ContaA": ["ContaB"],
        "ContaB": ["ContaC"],
        "ContaC": ["ContaA"]
    }

    if detect_cycle_dfs(transactions):
        print("Ciclo detectado! Há potencial esquema de lavagem de dinheiro.")
    else:
        print("Nenhum ciclo encontrado.")
