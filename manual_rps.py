import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    return computer_choice

get_computer_choice()
    

def get_user_choice():
    user_choice = input("Please enter your guess: ")
    return user_choice

def get_winner(computer_choice, user_choice):
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    if computer_choice == 'Rock' and user_choice == 'Scissors' or computer_choice == 'Paper' and user_choice == 'Rock' or computer_choice == 'Scissors' and user_choice == 'Paper':
        print("You won")
    
    elif computer_choice == 'Rock' and user_choice == 'Paper' or computer_choice == 'Paper' and user_choice == 'Scissors' or computer_choice == 'Scissors' and user_choice == 'Rock':
        print("You lost")

    else:
        print("It is a tie!")
        
get_winner(computer_choice = get_computer_choice, user_choice = get_user_choice)


