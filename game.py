# game.py
# Rock paper scissors

import random

while True:
    
    print("Rock, Paper, Scissors, Shoot!")
    print("-------------------")
    print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
    print("-------------------")


    #ask for user input
    user_choice = input("Please choose either 'rock' 'paper' or 'scissors': ") #input() makes it string
    print("You chose:", user_choice) #printing multiple things separated by comma
    #print("You chose: " + user_chocie) #concatenation
    #print(f"You chose: {user_choice}") #string interpolation
    user_choice = user_choice.lower()


    #simulating computer input
    print("-------------------")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    print("The computer chose:", computer_choice)


    #verify valid selection from user
    #stop the program and don't determine winner if user choice is invalid
    if user_choice not in options:
        print("Please choose a valid option and try again")
        exit()
        
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

        # main program
    while True:
        answer = str(input('Do you want to play again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("-------------------")
        print("Thanks for playing. Please play again!")
        break