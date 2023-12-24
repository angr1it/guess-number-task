def check(first, second):
    if len(first) != len(second):
        print("NO")
        return

    first = sorted(first)
    second = sorted(second)

    for ind in range(len(first)):
        if first[ind] != second[ind]:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    first = input()
    second = input()

    check(first, second)
