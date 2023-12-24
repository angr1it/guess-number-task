import heapq


def dijkstra(graph, root, n):
    dist = [1e12 for _ in range(n)]
    dist[root] = 0
    visited = [False for _ in range(n)]
    pq = [(0, root)]
    print(graph)

    while len(pq) > 0:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if u not in graph:
            continue

        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heapq.heappush(pq, (dist[v], v))

    return dist, visited


if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ", 1)))

    graph = {}
    for _ in range(K):
        a, b, l = tuple(map(int, input().split(" ", 2)))
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append((b, l))
        graph[b].append((a, l))

    S, F = tuple(map(int, input().split(" ", 1)))
    if S == F:
        print(0)
    else:
        dist, visited = dijkstra(graph, S - 1, N)
        if visited[F - 1] is False:
            print(-1)
        else:
            print(dist[F - 1])
