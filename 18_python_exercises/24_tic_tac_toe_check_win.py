# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

# Here are some more examples to work with:

def check_winner(board):
    # check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]

    # check column
    for col in range(len(board)):
        col_elements = [board[row][col] for row in range(len(board))]
        if len(set(col_elements)) == 1 and col_elements[0] != 0:
            return col_elements[0]

    # check diagonols
    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != 0:
        return board[0][0]

    if len(set([board[i][len(board)-1-i] for i in range(len(board))])) == 1 and board[0][len(board)-1] != 0:
        return board[0][len(board)-1]

        # no winner
    return 0


if __name__ == "__main__":
    winner_is_2 = [[2, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]

    winner_is_also_1 = [[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]

    no_winner = [[1, 2, 0],
                 [2, 1, 0],
                 [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 0]]

    other_diagonal = [[1, 1, 2],
                      [0, 2, 0],
                      [2, 1, 0]]

    print(check_winner(winner_is_2))
    print(check_winner(winner_is_1))
    print(check_winner(winner_is_also_1))
    print(check_winner(no_winner))
    print(check_winner(also_no_winner))
    print(check_winner(other_diagonal))
