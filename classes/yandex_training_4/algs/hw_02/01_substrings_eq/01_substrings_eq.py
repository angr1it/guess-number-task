MODULE = 1000000007
X = 257


def process(string: str) -> tuple:
    p = [0]
    pow = [1]
    res = 0

    for i in range(1, len(s) + 1):
        res = (res * X + ord(s[i - 1]) - ord("a") + 1) % MODULE
        p.append(res)
        pow.append((pow[i - 1] * X) % MODULE)

    return p, pow


def isEqual(p: list, pow: list, length: int, p1: int, p2: int) -> bool:
    if p1 == p2:
        return True

    a = (p[p1 + length] + p[p2] * pow[length]) % MODULE
    b = (p[p2 + length] + p[p1] * pow[length]) % MODULE
    return a == b


if __name__ == "__main__":
    s = input()
    Q = int(input())
    nums = []
    for _ in range(Q):
        nums.append(tuple(map(int, input().split(" "))))

    p, pow = process(s)
    results = [isEqual(p, pow, *params) for params in nums]

    print("\n".join("yes" if x else "no" for x in results))
