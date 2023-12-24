def process(data: tuple, N: int) -> list:
    nums = [0 for _ in range((N + 1) * 2 + 1)]
    nums[0], nums[-1] = -1, -2

    for i in range(len(data)):
        nums[(i + 1) * 2] = data[i]

    dp = [0 for _ in range(len(nums))]
    center, radius = 0, 0

    for i in range(1, len(nums) - 2):
        mirror = 2 * center - i

        if radius > i:
            dp[i] = min(radius - i, dp[mirror])
        else:
            dp[i] = 0

        while nums[i + 1 + dp[i]] == nums[i - 1 - dp[i]]:
            dp[i] += 1

        if dp[i] + i > radius:
            center = i
            radius = dp[i] + i

    res = []
    p = len(dp) // 2
    while p > 0:
        if dp[p] > 1 and dp[p] == p - 1 and dp[p] % 2 == 0:
            res.append(N - p // 2)
        p -= 1

    res.append(N)
    return res


if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ", 1)))
    nums = tuple(map(int, input().split(" ")))
    assert len(nums) == N

    print(" ".join(str(x) for x in process(nums, N)))
