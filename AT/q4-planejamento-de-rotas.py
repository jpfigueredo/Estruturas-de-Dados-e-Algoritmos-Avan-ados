class GraphMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.indices = {v: i for i, v in enumerate(vertices)}
        n = len(vertices)
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    def add_edge(self, v1, v2, weight=1):
        i1 = self.indices[v1]
        i2 = self.indices[v2]
        self.matrix[i1][i2] = weight
        self.matrix[i2][i1] = weight
    
    def print_matrix(self):
        print("Matriz de Adjacência:")
        print("   ", "  ".join(self.vertices))
        for i, row in enumerate(self.matrix):
            print(f"{self.vertices[i]}  {row}")


class GraphList:
    def __init__(self, vertices):
        self.adj_list = {v: [] for v in vertices}
    
    def add_edge(self, v1, v2, weight=1):
        self.adj_list[v1].append((v2, weight))
        self.adj_list[v2].append((v1, weight))
    
    def print_list(self):
        print("Lista de Adjacência:")
        for v, neighbors in self.adj_list.items():
            print(f"{v} -> {neighbors}")


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 3),
        ('D', 'F', 6),
        ('E', 'F', 6)
    ]
    
    g_matrix = GraphMatrix(vertices)
    for (v1, v2, w) in edges:
        g_matrix.add_edge(v1, v2, w)
    g_matrix.print_matrix()
    
    print("\n" + "-"*40 + "\n")
    
    g_list = GraphList(vertices)
    for (v1, v2, w) in edges:
        g_list.add_edge(v1, v2, w)
    g_list.print_list()
