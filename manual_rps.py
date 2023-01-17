import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    return computer_choice
    

def get_user_choice():
    user_choice = input("Please enter your guess: ")
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == 'Rock' and user_choice == 'Paper' or \
        computer_choice == 'Paper' and user_choice == 'Rock' or\
        computer_choice == 'Scissors' and user_choice == 'Paper':
        print ("You lost!")
        
    ##user wins
    elif user_choice == 'Rock' and computer_choice == 'Scissors' or \
        user_choice == 'Paper' and computer_choice == 'Rock' or \
        user_choice == 'Scissors' and computer_choice == 'Paper':
        print ("You win!")
        
    ##tie
    else:
        print ("Its a tie")

