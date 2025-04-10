# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.




def create_board():
    board = []
    for x in range(10):
        board.append("_")
    return board
    


def print_board(board:list):
    for x in range(0,9,3):
        print(f"{board[x]} {board[x+1]} {board[x+2]}" + "\n")
            

def player_choice():
    player_X_first = True
    choice = input("What do you want to choose? X or O. Type either X or O to choose: ")
    while choice.lower() not in ["x","o"]:
        choice = input("Wrong character. Choose betwee X or O: ")
    if choice == "x":
        return player_X_first
    return not player_X_first

def make_move(board:list):
    while True:
        try:
            move =  int(input("Enter your move from 1-9: "))
            if board[move - 1] in ["x","o"]:
                print("That position has already been chosen!Try again! ")
                continue
            if  1 <= move <=9:
                return move-1
            print("Choose between 1-9")
            
        except(ValueError):
            print("Invalid input, please choose a number from 1-9: ")

def place_on_board(board:list, index:int,x_plays_first):
    if x_plays_first:
        board[index] = "X"
    else:
        board[index] = "O"

def check_game_end(board:list):
    for x in range (0,9,3):
        if board[x] == board[x+1] and board[x+1] == board[x+2] and board[x]!="_":
            return 1
    for x in range(0,3):
        if board[x] == board[x+3] and board[x+3] == board[x+6] and board[x]!="_":
            return 1

    index = 0 
    if board[index] == board[index+ 4] and board[index+8] and board[x]!="_":
        return 1
    index = 2
    if board[index] == board[index+2] and board[index+2] == board[index+4] and board[x]!="_":
        return 1
    if board.count("_") == 0:
        return 2
    return 0

# 0 1 2
# 3 4 5
# 6 7 8


def play():
    board = create_board()
    x_plays_first = player_choice()
    while True:
        index_placed = make_move(board)
        place_on_board(board,index_placed,x_plays_first)
        print_board(board)
        x_plays_first = False
        state = check_game_end(board)
        if state == 1:
            if not x_plays_first:
                print("X won!")
                return
            else:
                print("O won")
                return
                
        elif state == 2:
            print("Draw")


play()
        

    







