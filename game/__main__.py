from game.hidden_num import HiddenNum
from game.solvers.binary import solve
from game.score import score_game


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    hidden_num = HiddenNum(number)  # Показалось, что так было бы логичнее;
    # можно ведь и за 0 попыток "угадать";

    _, count = solve(hidden_num, 0, 100)

    return count


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
