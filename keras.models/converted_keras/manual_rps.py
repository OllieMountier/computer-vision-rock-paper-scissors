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

def get_winner():
    global computer_choice
    global user_choice
    
    if computer_choice == 'rock' and user_choice == 'paper' or \
        computer_choice == 'paper' and user_choice == 'rock' or\
        computer_choice == 'scissors' and user_choice == 'paper':
        print ("Computer wins")
        
    ##user wins
    elif user_choice == 'rock' and computer_choice == "scissors" or \
        user_choice == 'paper' and computer_choice == "rock" or \
        user_choice == 'scissors' and computer_choice == "paper":
        print ("User wins")
        
    ##tie
    else:
        print ("Its a tie")

def play():
    get_computer_choice()
    get_user_choice()
    get_winner()

play()

    


