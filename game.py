# game.py
# Rock paper scissors

import os
import random
from dotenv import load_dotenv
load_dotenv()

USER_NAME = os.getenv("USER_NAME", default = "Player One")

print("Rock, Paper, Scissors, Shoot!")
print("-------------------")
print("Welcome {USER_NAME} to my Rock-Paper-Scissors game...")
print("-------------------")

while True: #starts the loop that allows user to play again at the end
    #sourced from stack overflow user volatility: https://stackoverflow.com/a/14907102/15171801
    

    #ask for user input
    user_choice = input("Please choose either 'rock' 'paper' or 'scissors': ") #input() makes it string
    print("You chose:", user_choice) #printing multiple things separated by comma
    #print("You chose: " + user_chocie) #concatenation
    #print(f"You chose: {user_choice}") #string interpolation
    user_choice = user_choice.lower() #convert to lowercase and save into variable


    #simulating computer input
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    print("The computer chose:", computer_choice)


    #verify valid selection from user
    #stop the program and don't determine winner if user choice is invalid
    if user_choice not in options:
        print("Please choose a valid option and try again")
        exit() #exit based on instructions, but could also add loop here
        
    print("-------------------")

    #determining who won
    if user_choice == "rock":
        if computer_choice == "rock":
            print("Oh, it's a tie.")
        elif computer_choice == "paper":
            print("Oh, the computer won. It's ok.")
        elif computer_choice == "scissors":
            print("Oh, you won! Nice job.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Oh, you won! Nice job.")
        elif computer_choice == "paper":
            print("Oh, it's a tie.")
        elif computer_choice == "scissors":
            print("Oh, the computer won. It's ok.")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("Oh, the computer won. It's ok.")
        elif computer_choice == "paper":
            print("Oh, you won! Nice job.")
        elif computer_choice == "scissors":
            print("Oh, it's a tie.")
    else:
        print("OOPS SOMETHING WENT WRONG.")

    # restarting from top or ending the loop
    while True:
        answer = str(input('Do you want to play again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Invalid input, please use 'y' or 'n'")
    if answer == 'y':
        continue
    else:
        print("-------------------")
        print("Thanks for playing. Please play again!")
        print("-------------------")
        break