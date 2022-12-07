from tictactoe import TicTacToe


def test_game_can_init():
    game = TicTacToe()
    assert (isinstance(game, TicTacToe))


def test_game_can_instantiate():
    game = TicTacToe()
    assert (game.record == {'x': [], 'o': []})
    assert (game.number == set(range(1, 10)))
    assert (game.start_mark == 'x')
    assert (game.result is None)


def test_game_can_mark():
    game = TicTacToe()
    game.mark_position('x', 5)
    assert (game.record['x'] == [5])
    assert (5 not in game.number)


def test_run_game():
    game = TicTacToe()
    # run the game, expect draw, you win, or you loose
    game.run()
    assert (game.result in ('You Win', 'You Loose', 'Draw Game'))


def test_you_win_result():
    game = TicTacToe()
    game.record = {'x': [1, 2, 3], 'o': [4, 5]}
    assert (TicTacToe.claim_winner(game.record['x']) is True)


def test_you_lose_result():
    game = TicTacToe()
    game.record = {'x': [1, 2, 7], 'o': [4, 5, 6]}
    assert (TicTacToe.claim_winner(game.record['x']) is False)
