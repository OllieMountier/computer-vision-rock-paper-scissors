import time
import random

import os
os.chdir('C:\\Users\\ollie\\Data_science\\VScode\\Projects\\Computer Vision RPS\\keras.models\\converted_keras')

import cv2
import numpy as np

from keras.models import load_model
model = load_model('keras_model.h5', compile = False)
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def main():
    rounds_played = 0
    
    while True:
        
        Timer = 5
        start_time = time.time()
        
        while Timer > 0:
           
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            
            current_time = time.time()
            if current_time - start_time >= 1:
                Timer = Timer - 1
                print(Timer)
                start_time = current_time
        else:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            print(prediction)
                
            rounds_played = get_winner(prediction, rounds_played)
            print(rounds_played)
            if rounds_played == 5 or cv2.waitKey(1) & 0xFF == ord('q'):
                break


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print('The computer chose: ', computer_choice)
    return computer_choice

def get_prediction(prediction):
    index = np.argmax(prediction)
    return index
    print(index)

def get_winner(prediction, rounds_played):
    computer_wins = 0
    user_wins = 0
    computer_choice = get_computer_choice()
    user_choice = get_prediction(prediction)
    
    ##computer wins
    if computer_choice == 'rock' and user_choice == 2 or \
        computer_choice == 'paper' and user_choice == 0 or\
        computer_choice == 'scissors' and user_choice == 1:
        print ("Computer wins")
        computer_wins = computer_wins + 1
    ##user wins
    elif user_choice == 0 and computer_choice == "scissors" or \
        user_choice == 1 and computer_choice == "rock" or \
        user_choice == 2 and computer_choice == "paper":
        print ("User wins")
        user_wins = user_wins + 1
    ##tie
    else:
        print ("Its a tie")

    print("User wins", user_wins, "Computer wins", computer_wins)
    rounds_played = rounds_played + 1
    return rounds_played
    

main()



