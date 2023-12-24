if __name__ == "__main__":
    N = int(input())
    if N > 0:
        a = list(map(int, input().split(" ")))
    else:
        a = []
        input()

    print(" ".join(str(x) for x in sorted(a)))
