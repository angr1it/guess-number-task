def rabbit(field: list, N: int, M: int) -> int:
    dp = [[0 for x in range(M)] for y in range(N)]
    maxSize = 0

    for y in range(N):
        dp[y][0] = field[y][0]
        maxSize = max(maxSize, dp[y][0])

    for x in range(M):
        dp[0][x] = field[0][x]
        maxSize = max(maxSize, dp[0][x])

    for y in range(1, N):
        for x in range(1, M):
            if field[y][x] == 1:
                dp[y][x] = min(dp[y - 1][x - 1], dp[y][x - 1], dp[y - 1][x]) + 1
                maxSize = max(maxSize, dp[y][x])

    return maxSize


if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))

    field = []
    for y in range(N):
        field.append(tuple(map(int, input().split(" "))))

    print(rabbit(field, N, M))
