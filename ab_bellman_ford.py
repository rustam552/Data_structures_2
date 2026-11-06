my_trace = {
    1: [0, 6, 3, float('inf'), float('inf')],
    2: [0, 1, 3, 9, 10],
    3: [0, 1, 3, 4, 8],
    4: [0, 1, 3, 4, 3],
}

def bellman_ford(vertices, edges, source):
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0
    prev = {v: None for v in vertices}
    history = [dist.copy()]

    for k in range(1, len(vertices)):
        new = dist.copy()
        for a, b, w in edges:
            if dist[a] + w < new[b]:
                new[b] = dist[a] + w
                prev[b] = a
        dist = new
        history.append(dist.copy())

    for a, b, w in edges:
        if dist[a] + w < dist[b]:
            raise ValueError("Negative cycle detected")

    return dist, prev, history

def build_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1]

def bellman_ford_early(vertices, edges, source):
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0
    prev = {v: None for v in vertices}
    rounds = 0

    for k in range(1, len(vertices)):
        rounds += 1
        new = dist.copy()
        changed = False
        for a, b, w in edges:
            if dist[a] + w < new[b]:
                new[b] = dist[a] + w
                prev[b] = a
                changed = True
        dist = new
        if not changed:
            return dist, prev, rounds

    for a, b, w in edges:
        if dist[a] + w < dist[b]:
            raise ValueError("Negative cycle detected")

    return dist, prev, rounds
