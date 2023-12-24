def run(levels: list[int], n: int, k: int) -> int:
    time = 0
    left = []
    for ind in range(len(levels)):
        trips = levels[ind] // k
        time += trips * (ind + 1) * 2
        left.append(levels[ind] - trips * k)

    current = n - 1
    load = 0
    while current >= 0:
        if left[current] == 0:
            current -= 1
            continue
        if load == 0:
            time += (current + 1) * 2

        load += left[current]
        if load > k:
            left[current] = load % k
            load = 0
        else:
            left[current] = 0
            current -= 1

    return time


if __name__ == "__main__":
    k = int(input())
    n = int(input())

    levels = []
    for _ in range(n):
        levels.append(int(input()))

    print(run(levels, n, k))
