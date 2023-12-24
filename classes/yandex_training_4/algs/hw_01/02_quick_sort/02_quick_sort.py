import random


def partition(nums: list[int], left: int, right: int) -> int:
    pivot = nums[random.randint(left, right)]
    length = right - left
    equal = left
    greater = left

    for x in range(left, left + length + 1):
        current = nums[x]
        if current < pivot:
            nums[x] = nums[greater]
            nums[greater] = nums[equal]
            greater += 1
            nums[equal] = current
            equal += 1
        elif current == pivot:
            nums[x] = nums[greater]
            nums[greater] = current
            greater += 1

    return equal


def quicksort(arr: list[int], left: int, right: int):
    if left < right:
        x = partition(arr, left, right)
        quicksort(arr, left, x)
        quicksort(arr, x + 1, right)

    return arr


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        N = int(input.readline())
        if N > 0:
            a = list(map(int, input.readline().split(" ")))
            quicksort(a, 0, len(a) - 1)
        else:
            a = []
            input.readline()

    with open("output.txt", "w") as output:
        output.write(" ".join(str(x) for x in a))
