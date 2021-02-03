# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#ask for user input
user_choice = input("Please choose either 'rock' 'paper' or 'scissors': ")

print("You chose:", user_choice) #printing multiple things separated by comma
#print("You chose: " + user_chocie) #concatenation
#print(f"You chose: {user_choice}") #string interpolation

#simulating computer input
print("-------------------")
options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)
print("The computer chose:", computer_choice)

#verify valid selection from user
#stop the program and don't determine winner if user choice is invalid
user_choice.lower()

print(user_choice)
quit()

#if user_choice in options:
#    #pass through
#else:
#    print("Please choose a valid option and try again")
#    exit()

quit()
#determining who won
print("-------------------")

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


print("-------------------")

print("Thanks for playing. Please play again!")