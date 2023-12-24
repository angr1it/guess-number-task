def merge(arr1: list, arr2: list) -> list:
    N = len(arr1) + len(arr2)
    res = [None for _ in range(N)]
    p1, p2 = 0, 0

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            res[p1 + p2] = arr1[p1]
            p1 += 1
        else:
            res[p1 + p2] = arr2[p2]
            p2 += 1

    while p1 < len(arr1):
        res[p1 + p2] = arr1[p1]
        p1 += 1

    while p2 < len(arr2):
        res[p1 + p2] = arr2[p2]
        p2 += 1

    return res


if __name__ == "__main__":
    N = int(input())
    if N > 0:
        a = list(map(int, input().split(" ")))
    else:
        a = []
        input()

    M = int(input())
    if M > 0:
        b = list(map(int, input().split(" ")))
    else:
        b = []
        input()

    print(" ".join(str(x) for x in merge(a, b)))
