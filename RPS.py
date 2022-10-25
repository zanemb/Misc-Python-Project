#   Zane Mazor-Brown
#   Professor King
#   BUS 392-01
#   29 October 2021

#   Homework #3

#   Write a program that lets the user play the game of Rock, Paper, Scissors 
#   against the computer. The program should work as follows:

#   1. When the program begins, a random number in the range of 1 through 3 is
#      generated. If the number is 1, then the computer has chosen rock. If the
#      number is 2, then the computer has chosen paper. If the number is 3, 
#      then the computer has chosen scissors. (Don’t display the computer’s 
#      choice yet.)
#   2. The user enters his or her choice of “rock,” “paper,” or “scissors” at 
#      the keyboard.
#   3. The computer’s choice is displayed.
#   4. A winner is selected according to the following rules:
#       - If one player chooses rock and the other player chooses scissors, 
#         then rock wins.(Rock smashes scissors.)
#       - If one player chooses scissors and the other player chooses paper,
#         then scissors wins.(Scissors cuts paper.)
#       - If one player chooses paper and the other player chooses rock, then
#         paper wins. (Paper wraps rock.)
#       - If both players make the same choice, the game is a tie.

# import random module to find random numbers
import random
# define function to generate computer's move (int between 1 and 3 (inclusive)
def random_number():
    return random.randint(1, 3)
# define function to return rock, paper, or scissors given 1, 2, or 3
def find_computer_play(number):
    # condition for computer play being 'Rock'
    if number == 1:
        return "Rock"
    # condition for computer play being 'Paper'
    elif number == 2:
        return "Paper"
    # condition for computer play being 'Scissors'
    else:
        return "Scissors"

# define function to prompt user to input Rock, Paper, or Scissors
def user_input():  
    return input("Enter 'Rock', 'Paper', or 'Scissors': ").title()
    # (could have used .lower/upper() but wanted to experiment with .title())

# define function to call a random number and translate it into a valid play
def find_display_computer():
    # call function to find computer play with the random number function
    computer_play = find_computer_play(random_number())
    # display the computer's play to the user
    print(f"Computer chose: {computer_play}")
    # return the computers play for evaluation against the user's play
    return computer_play

# define function to evaluate user and computer plays and return the outcome
def who_wins(user, comp):
    # assign outcomes to shorter variables for easy reference
    tie = "You tied!"
    win = "You win!"
    loss = "Computer wins!"
    # condition for a Rock - Rock tie
    if user == "Rock" and comp == "Rock":
        return tie
    # condition for a Rock - Paper computer win/user loss
    elif user == "Rock" and comp == "Paper":
        return loss
    # condition for a Rock - Scissors user win/computer loss
    elif user == "Rock" and comp == "Scissors":
        return win
    # condition for a Paper - Rock user win/computer loss
    elif user == "Paper" and comp == "Rock":
        return win
    # condition for a Paper - Paper tie
    elif user == "Paper" and comp == "Paper":
        return tie
    # condition for a Paper - Scissors computer win/user loss
    elif user == "Paper" and comp == "Scissors":
        return loss
    # condition for a Scissors - Rock computer win/user loss
    elif user == "Scissors" and comp == "Rock":
        return loss
    # condition for a Scissors - Paper user win/computer loss
    elif user == "Scissors" and comp == "Paper":
        return win
    # condition for a Scissors - Scissors tie
    elif user == "Scissors" and comp == "Scissors":
        return tie
    # if none of the previous conditions are met, print "Invalid input"
    else:
        return "Invalid input"

# define main function to call all previous functions
def main():
    # call function to prompt user for input
    user_play = user_input()
    # generate and display computer's move
    computer_play = find_display_computer()
    # use computer and user plays to call who_wins function and return outcome
    outcome = who_wins(user_play, computer_play)
    # display outcome of game to user
    print(outcome)

# call main function
main()


# combinations for ROCK PAPER SCISSORS

# USER - COMP

# ROCK ROCK = tie
# ROCK PAPER = computer win
# ROCK SCISSORS = user win

# PAPER ROCK = user win
# PAPER PAPER = tie
# PAPER SCISSORS = computer win

# SCISSORS ROCK = computer win
# SCISSORS PAPER = user win
# SCISSORS SCISSORS = tie

