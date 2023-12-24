INF = 1e64


def canAddToPath(matrix, path, v, pos):
    if matrix[path[pos - 1]][v] == 0:
        return False
    for i in range(pos):
        if path[i] == v:
            return False

    return True


def hamiltonianCycleUtil(matrix, path, n, pos, current_length, shortes_length):
    if pos == n:
        if matrix[path[pos - 1]][path[0]] > 0:
            shortes_length = min(
                current_length + matrix[path[pos - 1]][path[0]], shortes_length
            )
        return current_length, shortes_length

    for v in range(1, n):
        if canAddToPath(matrix, path, v, pos):
            path[pos] = v
            current_length, shortes_length = hamiltonianCycleUtil(
                matrix,
                path,
                n,
                pos + 1,
                current_length + matrix[path[pos - 1]][v],
                shortes_length,
            )
            path[pos] = -1

    return current_length, shortes_length


def findShortestHamiltonianCycle(n, matrix):
    path = [-1] * (n + 1)
    path[0] = 0
    _, shortes_length = hamiltonianCycleUtil(matrix, path, n, 1, 0, INF)

    return -1 if shortes_length == INF else shortes_length


if __name__ == "__main__":
    n = int(input())

    matrix = []
    for _ in range(n):
        matrix.append(tuple(map(int, input().split(" ", n - 1))))

    if n == 1:
        print(0)
    else:
        print(findShortestHamiltonianCycle(n, matrix))
