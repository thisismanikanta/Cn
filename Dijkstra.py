import sys

def dijkstra(graph, src, dest, names):
    n = len(graph)
    visited = [False] * n
    dist = [sys.maxsize] * n
    parent = [-1] * n
    dist[src] = 0

    for _ in range(n):
        min_dist = sys.maxsize
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    parent[v] = u

    path = []
    node = dest
    while node != -1:
        path.append(names[node])
        node = parent[node]
    path.reverse()

    if dist[dest] == sys.maxsize:
        print(f"No path from {names[src]} to {names[dest]}.")
    else:
        print("Shortest path from {} to {}: {}".format(
            names[src], names[dest], " -> ".join(path)))
        print("Total cost:", dist[dest])


names = ['a', 'b', 'c', 'd', 'e', 'z']

graph = [
    [0, 4, 2, 0, 0, 0],
    [4, 0, 1, 5, 0, 0],
    [2, 1, 0, 8, 10, 0],
    [0, 5, 8, 0, 2, 6],
    [0, 0, 10, 2, 0, 5],
    [0, 0, 0, 6, 5, 0]
]

src = 0
dest = 5

dijkstra(graph, src, dest, names)
