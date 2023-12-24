def isValid(seq: str) -> bool:
    if len(seq) % 2:
        return False

    half = len(seq) // 2 + 1
    q = []
    for s in seq:
        if s == "(" or s == "[" or s == "{":
            if len(q) == half:
                return False

            if s == "(":
                q.append(")")
            if s == "[":
                q.append("]")
            if s == "{":
                q.append("}")
        else:
            if len(q) == 0:
                return False
            if q.pop() != s:
                return False

    return len(q) == 0


if __name__ == "__main__":
    seq = input()
    print("yes" if isValid(seq) else "no")
