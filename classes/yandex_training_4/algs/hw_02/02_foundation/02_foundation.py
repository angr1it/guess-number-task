def calcPrefix(string: str) -> list[int]:
    p = [0]
    for i in range(len(string) - 1):
        x = p[i]
        while x > 0 and string[i + 1] != string[x]:
            x = p[x - 1]

        p.append(x + 1 if string[i + 1] == string[x] else 0)

    return p


if __name__ == "__main__":
    string = input()
    res = calcPrefix(string)
    print(len(res) if res[len(res) - 1] == 0 else len(res) - res[len(res) - 1])
