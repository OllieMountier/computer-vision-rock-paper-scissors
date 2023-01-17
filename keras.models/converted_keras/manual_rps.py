import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print('The computer chose: ', computer_choice)
    return computer_choice

def get_user_choice():
    user_choice = input("Please enter your guess: ").lower
    while True:
        global choices 
        if user_choice in choices:
            print("You chose: ", user_choice)
            break
        else:
            print("Please enter a valid guess: ")
            

    


