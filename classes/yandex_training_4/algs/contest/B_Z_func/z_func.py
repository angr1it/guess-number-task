
def z_func(string: str) -> list:
    result = [0 for _ in range(len(string))]
    left, right = 0, 0
    for i in range(0, len(string)):
        result[i] = max(0, min(right - i, result[i - left]))

        while i + result[i] < len(string) and string[result[i]] == string[i + result[i]]:
            result[i] += 1

        if i + result[i] > right:
            left = i
            right = i + result[i]

    return result


if __name__ == "__main__":
    N = input()
    string = input()
    print(" ".join(str(x) for x in z_func(string)[::-1]))
