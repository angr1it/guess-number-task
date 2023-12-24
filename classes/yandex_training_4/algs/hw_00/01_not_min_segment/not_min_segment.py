

def not_min_segment(data: list[int], segment_pairs: list) -> list:
    res = []
    for left, right in segment_pairs:
        _min = min(data[left:right + 1])
        _max = max(data[left:right + 1])
        if _min == _max:
            res.append("NOT FOUND")
        else:
            res.append(_max)

    return res


if __name__ == "__main__":
    N, M = map(int, input().split(' ', 1))

    data = list(map(int, input().split(' ')))
    assert len(data) == N

    pairs = []
    for _ in range(M):
        pair = tuple(map(int, input().split(' ')))
        assert len(pair) == 2
        pairs.append(pair)

    result = not_min_segment(data, pairs)

    print('\n'.join(str(line) for line in result))
