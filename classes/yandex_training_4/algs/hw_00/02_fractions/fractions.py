

def GCD(a: int, b: int) -> int:
    if b > a:
        a, b = b, a

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a


def LCM(a: int, b: int) -> int:
    return (a * b) / GCD(a, b)


def fractions(lst: tuple[int]) -> tuple[int]:
    assert len(lst) == 4

    lcm = LCM(lst[1], lst[3])

    num = lst[0] * (lcm / lst[1]) + lst[2] * (lcm / lst[3])
    den = lcm

    gcd = GCD(num, den)
    num /= gcd
    den /= gcd

    return int(num), int(den)


if __name__ == "__main__":
    lst = tuple(map(int, input().split(" ")))
    assert len(lst) == 4

    print(" ".join(str(num) for num in fractions(lst)))
