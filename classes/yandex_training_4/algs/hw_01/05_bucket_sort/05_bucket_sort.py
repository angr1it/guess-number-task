DELIMETER = "**********"


def printBuckets(buckets: dict) -> None:
    for i in range(10):
        if str(i) not in buckets.keys():
            res = "empty"
        else:
            res = ", ".join(tup_to_str(x) for x in buckets[str(i)])

        print(f"Bucket {i}: {res}")
    print(DELIMETER)


def moveToBacket(s: list[tuple], offset: int):
    buckets = {}

    for string in s:
        val = string[len(string) - 1 - offset]
        if val not in buckets:
            buckets[val] = []
        buckets[val].append(string)

    return buckets


def tup_to_str(tup: tuple) -> str:
    return "".join(x for x in tup)


def shuffle(s: list, buckets: dict) -> None:
    p = 0
    for i in range(10):
        if str(i) in buckets:
            if len(buckets[str(i)]) > 0:
                for b in buckets[str(i)]:
                    s[p] = b
                    p += 1


if __name__ == "__main__":
    n = int(input())

    s = []

    for _ in range(n):
        s.append(tuple(input()))

    print("Initial array:")
    print(", ".join(tup_to_str(x) for x in s))
    print(DELIMETER)

    k = len(s[0])

    for i in range(k):
        print(f"Phase {i + 1}")
        buckets = moveToBacket(s, i)
        printBuckets(buckets)
        shuffle(s, buckets)

    print("Sorted array:")
    print(", ".join(tup_to_str(x) for x in s))
