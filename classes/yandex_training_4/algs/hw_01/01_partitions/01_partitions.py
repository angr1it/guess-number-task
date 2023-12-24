def partition(nums: tuple[int], pivot: int) -> int:
    left = 0
    right = 0

    for x in range(len(nums)):
        current = nums[x]
        if current < pivot:
            nums[x] = nums[right]
            nums[right] = nums[left]
            right += 1
            nums[left] = current
            left += 1
        elif current == pivot:
            nums[x] = nums[right]
            nums[right] = current
            right += 1

    return left


if __name__ == "__main__":
    N = int(input())
    if N > 0:
        a = list(map(int, input().split(" ")))
        x = int(input())

        res = partition(a, x)
        print(f"{res}\n{N - res}")
    else:
        input()
        input()
        print("0\n0")
