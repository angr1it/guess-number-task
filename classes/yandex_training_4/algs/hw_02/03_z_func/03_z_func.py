def calcZFunc(string: str) -> list:
    left = 0
    right = 0
    z = [0 for _ in range(len(string))]

    for i in range(1, len(string)):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])

        while z[i] + i < len(string) and string[z[i]] == string[z[i] + i]:
            z[i] += 1

        if z[i] + i - 1 > right:
            left = i
            right = z[i] + i - 1

    return z


if __name__ == "__main__":
    string = input()
    print(" ".join(str(x) for x in calcZFunc(string)))
