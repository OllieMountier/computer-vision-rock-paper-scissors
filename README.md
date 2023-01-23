# computer-vision-rock-paper-scissors

Milestone 2 was my first introduction to using models. On teachable machine I created a model ready to use in my RPS project that contained 4 classes- Rock, Paper, Scissors and nothing. I then added 4 or 5 pictures into each class of what the camera should recognise to be each gesture. I used more than one image as it allowed me to "train" the model better and make its predictions more accurate down the line.
I then downloaded the models file which contained keras_model.h5 (the model itself) and a text file that contained the labels (classes) of the model called labels.txt.
![image](https://user-images.githubusercontent.com/116648304/212968246-1f5615d5-d04e-4946-9280-e9c19db1b770.png)

Milestone 3 consisted of creating an environment and downloading the suitable libraries for it to work with the model and code. The environment was called rps_env and created/activated using conda and then the libraries were downloaded onto it using pip. The libraries I downloaded were Opencv-python, Tensorflow and Ipykernel. After the libraries were downloaded I created a requirements.txt file that would allow all other users that run this code to install thee dependencies. 
Once all these libraries were downloaded, I ran a code provided by AIcore to check my model was functioning. After fixing a few bugs, the model ran and a camera output was shown as well as predictions.

Milestone 4 was the initial coding of the RPS game. The first step was to make a game that a user could play against the computer by manually inputting into the machine rather than using a camera.
This started by making two functions, one to get the users choice and one to get the computers choice. The users choice was selected by using the input function, the computers was done by making a list and using import random selecting a choice out of that list.
![image](https://user-images.githubusercontent.com/116648304/214065205-c3147334-01ca-4868-92ea-846c73b0680a.png)
The next step was select a winner. This was done by using if-elif-else statements and went through each possible choice, using and/or operators. Once each possible combination was resolved, the code outputted whether the winner was the computer or user or a tie.
![image](https://user-images.githubusercontent.com/116648304/214066011-c141823b-238c-4f0f-9876-b1b275f88ebd.png)
This was all tidied by creating a function called 'play' and all three functions-get_winner, user_choice and computer_choice were put inside this function so only one function had to be called for the game to work.
