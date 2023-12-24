def show(data: list):
    return " ".join(str(x) for x in data)


def try_brick_comb(combinations: dict, examples: list, cur_sum, residue, pos, accum):
    if cur_sum not in combinations:
        combinations[cur_sum] = accum
    else:
        combinations[cur_sum] = min(combinations[cur_sum], accum, key=len)

    if pos >= len(examples):
        return
    try_brick_comb(combinations, examples, cur_sum + examples[pos], residue - examples[pos], pos + 1, accum + [examples[pos]])
    try_brick_comb(combinations, examples, cur_sum, residue - examples[pos], pos + 1, accum)


def process(N: int, examples: list) -> None:
    bricks_sum = sum(examples)
    if bricks_sum * 2 < N:
        return -1, None

    combinations = {}
    try_brick_comb(combinations, examples, 0, bricks_sum, 0, [])

    result_length = float("inf")
    results = None
    for first_sum, first_bricks in combinations.items():
        second_sum = N - first_sum
        if second_sum in combinations:
            second_bricks = combinations[second_sum]
            res_len = len(second_bricks) + len(first_bricks)

            if res_len < result_length:
                results = second_bricks + first_bricks
                result_length = res_len

    if not results:
        return 0, None

    return result_length, results


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    examples = list(map(int, input().split()))
    l, res = process(N, examples)
    print(l)
    if l > 0:
        print(show(res))
