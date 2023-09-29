import random
from termcolor import colored

# Function to print the picked choices
def print_stats(user, computer):
    print("User: ", user)
    print("Computer: ", computer)

# Function to determine who wins
def validate(user, computer):
    if user == computer:
        print_stats(user, computer)
        print(colored("-- > Tie! < --", 'blue'))
    elif user == "Rock":
        if computer == "Paper":
            print_stats(user, computer)
            print(colored("-- > Computer wins! < --", 'red'))
        elif computer == "Scissors":
            print_stats(user, computer)
            print(colored("-- > User wins! < --", 'green'))
    elif user == "Paper":
        if computer == "Scissors":
            print_stats(user, computer)
            print(colored("-- > Computer wins! < --", 'red'))
        elif computer == "Rock":
            print_stats(user, computer)
            print(colored("-- > User wins! < --", 'green'))
    elif user == "Scissors":
        if computer == "Rock":
            print_stats(user, computer)
            print(colored("-- > Computer wins! < --", 'red'))
        elif computer == "Paper":
            print_stats(user, computer)
            print(colored("-- > User wins! <--", 'green'))


while True:
    # List of possible choices
    choices = ['Rock', 'Paper', 'Scissors']

    # Computer choice - random generated choice
    computer_choice = random.choice(choices)

    # User choice - user-typed choice
    user_choice = None
    # Checking if user choice is valid from the list
    while user_choice not in choices:
        # If not, ask again
        user_choice = input("[Choose] Rock, Paper or Scissors: ").lower().capitalize()

    print()
    validate(user_choice, computer_choice)  # Print the results and winner
    print()

    # Prompting user if they want to play again
    play_again = input("[Choose] Want to play again? (yes/no): ")
    # If answer is not yes -> break
    if play_again != "y" and play_again != "yes":
        break

print("Thank you for playing!")