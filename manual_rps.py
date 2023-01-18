import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    print(computer_choice)
    return computer_choice
    
    
def get_user_choice():
    user_choice = input("Please enter your guess: ")
    print(user_choice)
    return user_choice

user_choice = get_user_choice()
computer_choice = get_computer_choice()

def get_winner(computer_choice, user_choice):
    if ((computer_choice == 'Scissors') and (user_choice == 'Rock')) or ((computer_choice == 'Rock') and (user_choice == 'Paper')) or ((computer_choice == 'Paper') and (user_choice == 'Scissors')):
        print("You won")
    
    elif ((computer_choice == 'Paper') and (user_choice == 'Rock')) or ((computer_choice == 'Scissors') and (user_choice == 'Paper')) or ((computer_choice == 'Rock') and (user_choice == 'Scissors')):
        print("You lost")

    else:
        computer_choice == user_choice
        print("It is a tie!")
        
get_winner('Rock', 'Paper')


