import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    return computer_choice
    

def get_user_choice():
    user_choice = input("Please enter your guess: ")
    print(user_choice)

get_computer_choice()
get_user_choice()

