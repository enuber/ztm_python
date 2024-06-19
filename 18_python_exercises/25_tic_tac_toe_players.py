# This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 4.

# In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game. In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2 ( or whoever is X and O won).

# There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.

# The next logical step is to deal with handling user input. When a player(say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:

# game = [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]
# The computer asks Player 1 (X) what their move is ( in the format row, col), and say they type 1, 3. Then the game would print out

# game = [[0, 0, X],
#         [0, 0, 0],
#         [0, 0, 0]]
# And ask Player 2 for their move, printing an O in that place.

# Things to note:

# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of(0, 0). To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this, it should be explained to the player.
# Ask the user to enter coordinates in the form “row, col” - a number, then a comma, then a number. Then you can use your Python skills to figure out which row and column they want their piece to be in .
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.

# Bonus:

# For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.


def print_board(board):
    for row in board:
        print(" ".join([str(cell) for cell in row]))


def check_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]

    # Check columns
    for col in range(len(board)):
        col_elements = [board[row][col] for row in range(len(board))]
        if len(set(col_elements)) == 1 and col_elements[0] != 0:
            return col_elements[0]

    # Check diagonals
    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != 0:
        return board[0][0]
    if len(set([board[i][len(board) - 1 - i] for i in range(len(board))])) == 1 and board[0][len(board) - 1] != 0:
        return board[0][len(board) - 1]

    return 0


def is_full(board):
    for row in board:
        if 0 in row:
            return False
    return True


def play_game():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    players = {1: 'X', 2: 'O'}
    current_player = 1

    while not is_full(board):
        print_board(board)
        move = input(f"Player {current_player} ({
                     players[current_player]}), enter your move (row,col): ")
        try:
            row, col = map(int, move.split(','))
            if row < 1 or row > 3 or col < 1 or col > 3:
                raise ValueError
            if board[row - 1][col - 1] != 0:
                raise ValueError
            board[row - 1][col - 1] = players[current_player]
        except ValueError:
            print("Invalid move. Please enter a valid move in the form 'row,col' where both row and col are between 1 and 3 and the cell is not occupied.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {current_player} ({players[current_player]}) wins!")
            break

        current_player = 1 if current_player == 2 else 2

    if not winner:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()
