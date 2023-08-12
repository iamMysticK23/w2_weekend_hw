# Comments will go here (updated 8.12.23 @ 307PM PST)
# Rock Paper Scissors Game
# Created by Kenai and Priscilla

# -----PSUEDO CODE-----#

# TWO MAIN VARIABLES: PLAYER AND COMPUTER(RANDOM)
# COMPUTER HAS 3 RANDOM OPTIONS (ROCK, PAPER, SCISSORS)
# PLAYER'S DECISION IS COMPLETED BY AN INPUT STATEMENT

# PRINT RULES OF PLAY:
# ROCK VS PAPER | PAPER WINS
# ROCK VS SCISSORS | ROCK WINS
# PAPER VS SCISSORS | SCISSOR WINS


# ---global variables below ---#
# DEFAULT LIST TO STORE THE 3 OPTIONS
# GAME_CHOICES = ["ROCK", "PAPER", "SCISSORS"]
# WIN/LOSE COUNTER(?)

# OPTION TO START OR END THE GAME?(while True)

# CONDITIONS THAT CAN BE MET DURING GAME PLAY:
# IF PLAYER == ROCK AND COMPUTER == PAPER:
    # SHOW PLAYER LOSES
# IF PLAYER == SCISSORS AND COMPUTER == ROCK:
    # SHOW PLAYER LOSES
# IF PLAYER == PAPER AND COMPUTER == SCISSORS:
    # SHOW PLAYER LOSES
# ELSE:
    # SHOW PLAYER WINS


# CONTINUE TO ASK PLAYER FOR INPUT UNTIL THEY PRESS 'Q' TO QUIT.
# IF RESPONSE.LOWER(ACCOUNTS FOR UPPER CASE INPUT) == 'Q':
# PRINT ("THANK YOU FOR PLAYING")
# BREAK



from random import randint

# welcome to rock, paper scissors and general instructions
print("\nWelcome to the Rock, Paper, Scissors Game")
print("Made in 2023 by Kenai and Priscilla")

# display the rules of the game
print("\n\t------------| Rules of the game: |-------------")
print("\tRock vs Paper | PAPER WINS\n\tRock vs Scissors | ROCK WINS\n\tPaper vs Scissors | SCISSORS WIN")

# keep track of user wins and computer wins
# defaults to 0
player_win_count = 0
computer_win_count = 0
draw_count = 0
    # gameplay_options = ["Rock", "Paper", "Scissors"]
    # All variations of Rock, Paper, Scissors in the list for validation
gameplay_options = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors", "ROCK", "PAPER", "SCISSORS"] # 8 indexes

# start the game after user puts in correct input
while True:
    player = input("Please pick from these options: Rock, Paper, Scissors: ")
    while player not in gameplay_options:
        player = input("Invalid option. Please pick 'Rock', 'Paper' or 'Scissors'.")


    # list of choices - can only be "Rock", "Paper", or "Scissors"

    computer = gameplay_options[randint(0, 8)]

    # print what player chose
    print("You chose: " + player.upper())
    print("Computer chose: " + computer.upper())

    
    if player.upper() == computer.upper():
        print("\nGame Tied!")
        draw_count += 1 

    elif (player.upper() == "ROCK" and computer.upper() == "SCISSORS"):
        print("\nYou win: " + player.upper() + " BEATS " + computer.upper())
        player_win_count += 1 

    elif (player.upper() == "PAPER" and computer.upper() == "ROCK"):
        print("You win: " + player.upper() + " COVERS " + computer.upper())
        player_win_count += 1 

    elif (player.upper() == "SCISSORS" and computer.upper() == "PAPER"):
        print("You win: " + player.upper() + " CUTS " + computer.upper())
        player_win_count += 1 
    else:
         print("You lose!")
         computer_win_count += 1   
    print("\nPlayer score: " + str(player_win_count) )
    print("Computer score: " + str(computer_win_count))
    print("Tie count: " + str(draw_count))

    # ask if they want to play again
    play_again = input("\nWould you like to play again?\nPress 'y' for yes or 'n' for no ")
    if play_again.lower() == 'n':
        break

print("Hope you enjoyed the game!")
    












