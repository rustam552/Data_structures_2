import math
INF = math.inf

edges = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

def dijkstra(source):
    dist = {n: INF for n in nodes}
    prev = {n: None for n in nodes}
    dist[source] = 0
    settled = set()
    
    # init
    print(f"init          | A=0 B=INF C=INF D=INF E=INF F=INF")
    
    while len(settled) < len(nodes):
        # простой поиск минимума
        u = min((n for n in nodes if n not in settled), key=lambda n: dist[n], default=None)
        if u is None or dist[u] == INF:
            break
        settled.add(u)
        
        for v, w in edges[u]:
            if v not in settled and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
        
        # печать состояния
        line = ' '.join(f"{n}={int(dist[n]) if dist[n] < INF else 'INF'}" for n in nodes)
        print(f"settle {u} ({int(dist[u])}) | {line}")
    
    return dist, prev

dist, prev = dijkstra('A')

def get_path(target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return ' -> '.join(reversed(path))

print()
for n in ['B', 'C', 'D', 'E', 'F']:
    print(f"A to {n}: cost {int(dist[n])}: {get_path(n)}")
