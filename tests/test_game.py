from game.score import score_game
from game.__main__ import game_core_v3


def test_game_score():
    assert score_game(game_core_v3) < 20
