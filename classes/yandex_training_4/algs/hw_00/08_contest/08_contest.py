def roundUp(k: int, m: int):
    return k // m + (0 if k % m == 0 else 1)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    n = int(input())

    print("YES" if a > roundUp(b, n) else "NO")
