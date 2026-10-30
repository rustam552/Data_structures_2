from collections import deque

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

def bfs(start):
    discovered = {start}
    dist = {start: 0}
    parent = {start: None}
    Q = deque([start])
    order = []
    while Q:
        u = Q.popleft()
        order.append(u)
        for v in adj[u]:
            if v not in discovered:
                discovered.add(v)
                dist[v] = dist[u] + 1
                parent[v] = u
                Q.append(v)
    return order, dist, parent

def get_path(parent, target):
    if target not in parent:
        return "no path"
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return ' -> '.join(reversed(path))

# Основной вывод
order, dist, parent = bfs('A')
print("BFS order from A:", ' '.join(order))
print(f"Shortest A -> G: distance {dist['G']}, path {get_path(parent, 'G')}")

_, distD, parentD = bfs('D')
print(f"Shortest D -> G: distance {distD['G']}, path {get_path(parentD, 'G')}")
