def choice(scores: tuple) -> list:
    N = len(scores)
    sums = [scores[0]]
    for i in range(1, N):
        sums.append(sums[i - 1] + scores[i])

    levels = [
        sums[N - 1] - scores[0] * N,
        *(
            scores[i] * i
            - sums[i - 1]
            + sums[N - 1]
            - sums[i]
            - scores[i] * (N - 1 - i)
            for i in range(1, N - 1)
        ),
        scores[N - 1] * N - sums[N - 1],
    ]

    return levels


if __name__ == "__main__":
    N = int(input())
    scores = tuple(map(int, input().split()))
    assert len(scores) == N

    levels = choice(scores)
    print(" ".join(str(x) for x in levels))
