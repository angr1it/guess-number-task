from ..hidden_num import HiddenNum


def solve(
    hidden: HiddenNum, min_num: int = 0, max_num: int = 100
) -> tuple[int, int]:
    """
    Бинарный поиск скрытого числа.
    Args:
        hidden (HiddenNum): загаданное число;
        min_num (int): левая граница отрезка поиска;
        max_num (int): правая граница;
    Returns:
        * int: угаданное число; либо None, если не найдено;
        * int: число попыток.
    """
    left = min_num
    right = max_num
    while left < right:
        mid = (left + right) // 2
        result = hidden.guess(mid)

        if result == 0:
            return mid, hidden.count

        if result < 0:
            left = mid + 1
        else:
            right = mid - 1

    if not hidden.guess(right):
        return right, hidden.count

    return None, hidden.count  # Числа нет в диапозоне
