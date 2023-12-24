def canSplit(n, a, b):
    return n <= (b * (n // a))


if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        res.append(canSplit(*tuple(map(int, input().split(" ")))))

    for result in res:
        print("YES" if result else "NO")
