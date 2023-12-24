def process(row, cols, diag1, diag2, n, count) -> int:
    if row == n:
        count += 1
        return count

    for col in range(n):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
            count = process(row + 1, cols, diag1, diag2, n, count)
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    return count


if __name__ == "__main__":
    n = int(input())

    cols = [False for _ in range(n)]
    diag1 = [False for _ in range(2 * n - 1)]
    diag2 = [False for _ in range(2 * n - 1)]
    print(process(0, cols, diag1, diag2, n, 0))
