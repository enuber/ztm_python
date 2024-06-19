# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

def draw_horrizonal(size):
    print(' ___' * size)


def draw_vertical(size):
    print('|   ' * (size + 1))


def create_board(size):
    for num in range(size):
        draw_horrizonal(size)
        draw_vertical(size)
        draw_vertical(size)
    draw_horrizonal(size)


if __name__ == "__main__":
    board_size = 0

    while True:
        try:
            board_size = int(
                input('What size board would you like (example, entering 3 will create a 3x3 board)?'))
            if board_size <= 0:
                raise ValueError
        except ValueError as e:
            print(e)
        else:
            break

    create_board(board_size)
