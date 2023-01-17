import random

choices = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    computer_choice = random.choice(choices)
    print(computer_choice)
    

def get_user_choice():
    user_choice = input("Please enter your guess: ")
    print(user_choice)

get_computer_choice()
get_user_choice()

