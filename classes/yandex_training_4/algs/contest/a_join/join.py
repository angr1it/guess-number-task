if __name__ == "__main__":
    k = int(input())
    l0 = 1
    hi = k * k
    while hi > l0:
        m = (hi + l0) // 2
        i2 = int((m + 1.0e-6) ** (1.0 / 2.0))
        i3 = int((m + 1.0e-6) ** (1.0 / 3.0))
        i6 = int((m + 1.0e-6) ** (1.0 / 6.0))

        count = i2 + i3 - i6
        if count < k:
            l0 = m + 1
        else:
            hi = m

    print(l0)
