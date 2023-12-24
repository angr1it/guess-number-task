def permutations(nums):
    results = []
    n = len(nums)
    visited = [False] * len(nums)

    def back(nums, seq):
        if len(seq) == n:
            results.append(seq[:])
            return

        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue
            seq.append(nums[i])

            visited[i] = True
            back(nums, seq)

            visited[i] = False
            seq.pop()

    back(nums, [])
    return results


if __name__ == "__main__":
    n = int(input())
    print("\n".join(''.join(str(x) for x in perm) for perm in permutations([i for i in range(1, n + 1)])))
