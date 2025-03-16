graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

visited = set()

def dfs(v):
    visited.add(v)
    
    print(v, end=' ')
    
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor)

dfs('A')
print()
