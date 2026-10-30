adj = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}
for k in adj:
    adj[k] = sorted(adj[k])

def dfs(start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        order.append(u)
        # соседи в обратном алфавитном порядке
        for v in sorted(adj[u], reverse=True):
            if v not in visited:
                stack.append(v)
    return order

print("DFS order from A:", ' '.join(dfs('A')))
print("DFS order from G:", ' '.join(dfs('G')))
