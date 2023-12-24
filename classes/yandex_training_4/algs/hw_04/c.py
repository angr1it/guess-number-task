class CutRes:
    def __init__(self, w, m) -> None:
        self.weight = w
        self.mask = m


def iteratingAndFindMax(n, matrix):
    maxW, maxM = 0, 0
    for mask in range(1, 1 << (n - 1)):
        weight = 0

        for i in range(n):
            for j in range(n):
                if mask & (1 << i) != 0 and mask & (1 << j) == 0:
                    weight += matrix[i][j]

        if weight > maxW:
            maxW = weight
            maxM = mask

    return maxW, maxM


if __name__ == "__main__":
    n = int(input())

    matrix = []
    for _ in range(n):
        matrix.append(tuple(map(int, input().split(" ", n - 1))))

    weight, mask = iteratingAndFindMax(n, matrix)
    print(weight)
    print(" ".join("1" if (mask >> i & 1) == 0 else "2" for i in range(n)))
