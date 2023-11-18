import random
import random
# write hello world to the console


def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == "yes"

# Main game loop
while True:
    play_game()
    if not play_again():
        break

