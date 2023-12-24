OPEN_BRACKETS = ("(", "[")
CLOSE_BRACKETS = (")", "]")


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []
    simbols = []
    m = n // 2
    stack = []

    def _generate(open_left, close_left):
        if not open_left and not close_left:
            result.append("".join(simbols))
            return

        if open_left:
            for i in range(len(OPEN_BRACKETS)):
                simbols.append(OPEN_BRACKETS[i])
                stack.append(CLOSE_BRACKETS[i])
                _generate(open_left - 1, close_left)

                simbols.pop()
                stack.pop()

        if open_left < close_left and len(stack) > 0:
            pop = stack.pop()
            for i in range(len(CLOSE_BRACKETS)):
                if pop != CLOSE_BRACKETS[i]:
                    continue

                simbols.append(CLOSE_BRACKETS[i])
                _generate(open_left, close_left - 1)
                simbols.pop()
                stack.append(CLOSE_BRACKETS[i])

    _generate(m, m)
    return result


if __name__ == "__main__":
    N = int(input())
    if N % 2 == 1:
        print()
    else:
        print("\n".join(generateParenthesis(N)))
