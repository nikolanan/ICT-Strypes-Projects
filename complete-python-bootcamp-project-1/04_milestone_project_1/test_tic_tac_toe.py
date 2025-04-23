from tic_tac_toe import create_board
from tic_tac_toe import print_board
from tic_tac_toe import player_choice
from tic_tac_toe import make_move
from tic_tac_toe import place_on_board
from tic_tac_toe import check_game_end
from tic_tac_toe import whose_turn_is
from tic_tac_toe import play_again
from tic_tac_toe import play

def test_create_board():
    """
    Tests the create_board function to ensure it initializes the tic-tac-toe board correctly.
    The board should be a list of 9 elements, all initialized to "_".
    """
    board = create_board()
    assert isinstance(board, list), "Board should be a list"
    assert len(board) == 9, "Board should contain 9 elements"
    assert all(cell == "_" for cell in board), "All cells should be initialized to '_'"

def test_print_board(capsys):
    """
    Tests the print_board function to ensure it correctly formats and displays the tic-tac-toe board.
    """
    board = ["X", "O", "_", "_", "X", "_", "_", "_", "O"]
    print_board(board)
    
    # Capture the output
    captured = capsys.readouterr()
    output = captured.out

    # Check if key parts of the board output are present
    assert "X | O | _" in output
    assert "_ | X | _" in output
    assert "_ | _ | O" in output

    # Check if reference positions are shown
    assert "1 | 2 | 3" in output
    assert "4 | 5 | 6" in output
    assert "7 | 8 | 9" in output

def test_player_choice(monkeypatch):
    """
    Tests the player_choice function to ensure it correctly interprets user input for player choice.
    """

    # Simulate user input for 'X'
    monkeypatch.setattr('builtins.input', lambda _: 'X')
    assert player_choice() is True, "Player 1 should choose X"

    # Simulate user input for 'O'
    monkeypatch.setattr('builtins.input', lambda _: 'O')
    assert player_choice() is False, "Player 1 should choose O"

def test_make_move(monkeypatch):
    """
    Tests the make_move function to ensure it correctly interprets user input for a move.
    """
    board = ["_", "_", "_", "X", "_", "_", "_", "_", "_"]
    inputs = iter(["100", "4", "5"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = make_move(board)
    assert result == 4, "Should return index 3 for valid input '4'"

def test_place_on_board():
    """
    Tests the place_on_board function to ensure it correctly places a player's symbol on the board.
    """
    board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    place_on_board(board, 4, "X")
    assert board[4] == "X", "Board position should be updated with 'X'"
    assert board.count("X") == 1, "There should be one 'X' on the board"
    assert board.count("_") == 8, "There should be eight empty positions on the board"

def test_check_game_end():
    """
    Tests the check_game_end function to ensure it correctly identifies game-ending conditions.
    """
    board = ["X", "X", "X", "_", "_", "_", "_", "_", "_"]
    assert check_game_end(board) is True, "Game should end with 'X' winning"

    board = ["_", "_", "_", "X", "X", "X", "_", "_", "_"]
    assert check_game_end(board) is True, "Game should end with 'X' winning"

    board = ["_", "_", "_", "_", "_", "_", "X", "X", "X"]
    assert check_game_end(board) is True, "Game should end with 'X' winning"

    board = ["O", "O", "O", "_", "_", "_", "_", "_", "_"]
    assert check_game_end(board) is True, "Game should end with 'O' winning"

    board = ["_", "_", "_", "O", "O", "O", "_", "_", "_"]
    assert check_game_end(board) is True, "Game should end with 'O' winning"

    board = ["_", "_", "_", "_", "_", "_", "O", "O", "O"]
    assert check_game_end(board) is True, "Game should end with 'O' winning"

    board = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
    assert check_game_end(board) is True, "Game should end with 'O' winning"

    # Diagonal win from top-left to bottom-right for X
    board = ["X", "_", "_", "_", "X", "_", "_", "_", "X"]
    assert check_game_end(board) is True, "Game should end with 'X' winning diagonally (\\)"

    # Diagonal win from top-right to bottom-left for O
    board = ["_", "_", "O", "_", "O", "_", "O", "_", "_"]
    assert check_game_end(board) is True, "Game should end with 'O' winning diagonally (/)"

    board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    assert check_game_end(board) is False, "Game should not end"

    board = ["_", "X", "_", "O", "_", "X", "_", "O", "_"]
    assert check_game_end(board) is False, "Game should not end"

def test_whose_turn_is():
    """
    Tests the whose_turn_is function to ensure it correctly identifies whose turn it is
    based on the number of turns and whether X plays first.
    """
    assert whose_turn_is(0, True) is True, "After 1 turn, it should be X's turn"
    assert whose_turn_is(1, True) is False, "After 2 turns, it should be O's turn"
    assert whose_turn_is(2, False) is False, "After 3 turns, it should be X's turn"
    assert whose_turn_is(3, False) is True, "After 4 turns, it should be O's turn"

def test_play_again(monkeypatch):
    """
    Tests the play_again function to ensure it correctly interprets user input for playing again.
    """
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    assert play_again() is True, "User should want to play again"

    # Simulate user input for 'no'
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert play_again() is False, "User should not want to play again"

    different_inputs = iter(['not a y', 'test', 'dsdsa', 'n'])
    monkeypatch.setattr('builtins.input', lambda _: next(different_inputs))
    assert play_again() is False, "User should not want to play again"

def test_play_full_game(monkeypatch, capsys):
    """
    Tests the full game play to ensure the game runs correctly from start to finish.
    """
    inputs = iter([
        'X',    # player_choice()
        '1',    # X move
        '2',    # O move
        '4',    # X move
        '5',    # O move
        '7',    # X move (X wins)
        'n'     # play_again() - don't restart game
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    play()

    # Capture the output
    output = capsys.readouterr().out

    assert "X's turn." in output
    assert "O's turn." in output
    assert "X won!" in output