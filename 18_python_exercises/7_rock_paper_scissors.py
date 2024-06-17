# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# choices = ['rock', 'paper', 'scissors']
# play_again_choices = ['yes', 'no', 'y', 'n']
# play_game = True
# player1_choice = ''
# player2_choice = ''
# play_again = ''


# def check_win():
#     if (player1_choice == 'rock' and player2_choice == 'scissors') or (player1_choice == 'paper' and player2_choice == 'rock') or (player1_choice == 'scissors' and player2_choice == 'paper'):
#         print('congrats player 1 wins')
#     elif (player2_choice == 'rock' and player1_choice == 'scissors') or (player2_choice == 'paper' and player1_choice == 'rock') or (player2_choice == 'scissors' and player1_choice == 'paper'):
#         print('congrats player 1 wins')
#     else:
#         print('it was a tie')


# while play_game:
#     # player 1 choice
#     while True:
#         try:
#             player1_choice = input('Player 1 type Rock, Paper or, Scissors: ')
#             player1_choice = player1_choice.lower()
#             if player1_choice not in choices:
#                 raise ValueError(
#                     'Please make sure to type in Rock, Paper, or Scissors')
#         except ValueError as e:
#             print(e)
#         else:
#             break
#     while True:
#         try:
#             player2_choice = input(
#                 'Player 2 type Rock, Paper or, Scissors: ')
#             player2_choice = player2_choice.lower()
#             if player2_choice.lower() not in choices:
#                 raise ValueError(
#                     'Please make sure to type in Rock, Paper, or Scissors')
#         except ValueError as e:
#             print(e)
#         else:
#             break
#     check_win()
#     try:
#         play_again = input('Play again (Yes or Y)/(No or N) ')
#         play_again = play_again.lower()
#         if play_again not in play_again_choices:
#             raise ValueError('Try again')
#         elif play_again == 'no' or play_again == 'n':
#             play_game = False
#     except ValueError as e:
#         print(e)


def get_player_choice(player):
    while True:
        player_choice = input(
            f"Player {player}, enter your choice (rock, paper, scissors): ").strip().lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Invalid choice! Please enter either 'rock', 'paper', or 'scissors'.")


def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return None  # Tie

    if (player1_choice == 'rock' and player2_choice == 'scissors') or \
       (player1_choice == 'scissors' and player2_choice == 'paper') or \
       (player1_choice == 'paper' and player2_choice == 'rock'):
        return 1  # Player 1 wins
    else:
        return 2  # Player 2 wins


def play_game():
    while True:
        player1_choice = get_player_choice(1)
        player2_choice = get_player_choice(2)

        winner = determine_winner(player1_choice, player2_choice)

        if winner is None:
            print("It's a tie!")
        else:
            print(f"Player {winner} wins!")

        play_again = input(
            "Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
