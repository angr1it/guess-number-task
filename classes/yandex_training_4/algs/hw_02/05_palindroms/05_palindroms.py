import math

START = "^"
END = "$"
DELIMITER = "#"


def extendString(string: str) -> str:
    if len(string) == 0:
        return START + END

    return START + DELIMITER + DELIMITER.join(s for s in string) + DELIMITER + END


def countPalidroms(string: str) -> int:
    extended = extendString(string)
    n = len(extended)

    dp = [0 for _ in range(n)]
    center = 0
    radius = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i

        if radius > i:
            dp[i] = min(radius - i, dp[mirror])

        while extended[i + 1 + dp[i]] == extended[i - 1 - dp[i]]:
            dp[i] += 1

        if dp[i] + i > radius:
            center = i
            radius = dp[i] + i

    res = 0
    for d in dp:
        res += int(math.ceil(d / 2))
    return res


if __name__ == "__main__":
    print(countPalidroms(input()))
