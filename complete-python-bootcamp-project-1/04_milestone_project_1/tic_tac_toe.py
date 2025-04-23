#This is a simple implementation of the classic Tic Tac Toe game.

def create_board() -> list:
    """Creates the board.

    :return: Returns a list of 9 elements, each initialized to "_".
    :rtype: list
    """
    return ["_"]*9

def print_board(board: list) -> None:
    """Prints the current state of the board and the reference positions.

    :param board: The current state of the tic-tac-toe board.
    :type board: list
    """
    print("Current board:")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\nReference positions:")
    for i in range(0, 9, 3):
        print(f" {i+1} | {i+2} | {i+3} ")
        if i < 6:
            print("---+---+---")
    print()    

def player_choice() -> bool:
    """
    Determines what player 1 plays with X or O, and returns True if player 1 plays with X.

    :return: True if player 1 chooses X, False if player 1 chooses O.
    :rtype: bool
    """
    player_x_first = True
    choice = input("What do you want to choose? X or O. Type either X or O to choose: ")
    while choice.lower() not in ["x","o"]:
        choice = input("Wrong character. Choose betwee X or O: ")
    if choice.lower() == "x":
        return player_x_first
    return not player_x_first

def make_move(board: list) -> int:
    """
    Prompts the player to make a move by selecting a position on the board.

    :param board: The current state of the tic-tac-toe board.
    :type board: list
    :return: The index of the board where the player wants to place their mark.
    :rtype: int
    """
    while True:
        try:
            move =  int(input("Enter your move from 1-9: "))
            if board[move - 1].lower() in ["x","o"]:
                print("That position has already been chosen!Try again! ")
                continue
            if  1 <= move <=9:
                return move-1
            print("Choose between 1-9")
                
        except ValueError:
            print("Invalid input, please choose a number from 1-9: ")
        except IndexError:
            print("Invalid move. That position is not on the board.")

def place_on_board(board: list, index: int, player_move: bool) -> None:
    """Places the player's mark (X or O) on the board at the specified index.

    :param board: The current state of the tic-tac-toe board.
    :type board: list
    :param index: The position on the board where the player's mark will be placed (0-8).
    :type index: int
    :param player_move: True if it's player X's turn, False if it's player O's turn.
    :type player_move: bool
    """
    if player_move:
        board[index] = "X"
    else:
        board[index] = "O"

def check_game_end(board: list) -> bool:
    """Checks if the game has ended by determining if there is a winner or a draw.

    :param board: The current state of the tic-tac-toe board.
    :type board: list
    :return: True if the game has ended (either a win or a draw), False otherwise.
    :rtype: bool
    """
    for x in range (0,9,3):
        if board[x] == board[x+1] and board[x+1] == board[x+2] and board[x]!="_":
            print(f"{board[x]} won!")
            return True
    for x in range(0,3):
        if board[x] == board[x+3] and board[x+3] == board[x+6] and board[x]!="_":
            print(f"{board[x]} won!")
            return True

    index = 0 
    if board[index] == board[index+ 4] and board[index+ 4] == board[index+8] and board[index]!="_":
        print(f"{board[index]} won!")
        return True
    index = 2
    if board[index] == board[index+2] and board[index+2] == board[index+4] and board[index]!="_":
        print(f"{board[index]} won!")
        return True
    if board.count("_") == 0:
        print("It's a draw!")
        return True
    return False

def whose_turn_is(turns: int, x_plays_first: bool) -> bool:
    """Determines whose turn it is based on the number of turns and whether X plays first.

    :param turns: The current turn number in the game.
    :type turns: int
    :param x_plays_first: A boolean indicating if X plays first (True) or O plays first (False).
    :type x_plays_first: bool
    :return: True if it's X's turn, False if it's O's turn.
    :rtype: bool
    """
    if x_plays_first:
        if turns %2 == 0:
            return True
        else:
            return False
    else:
        if turns %2 == 0:
            return False
        else:
            return True

def play_again() -> bool:
    """Asks the player if they want to play another game. 

    :return: True if the player chooses to play again, False otherwise.
    :rtype: bool
    """
    yes_no = input("Do you want to play again? Y/N ")
    while yes_no.lower() not in ["y","n"]:
        print("Wrong character! Please enter Y or N ")
        yes_no = input("Do you want to play again? Y/N ")
    return yes_no.lower() == "y"

def play() -> None:
    """
    Main function to run the Tic Tac Toe game.
    """
    while True:
        board = create_board()
        x_plays_first = player_choice()
        turns = 0

        while True:    
            who_is_on_turn = whose_turn_is(turns, x_plays_first)
            print(f"{'X' if who_is_on_turn else 'O'}'s turn.")
            index_placed = make_move(board)

            place_on_board(board, index_placed, who_is_on_turn)
            print_board(board)

            if check_game_end(board):
                break
            turns += 1

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play()