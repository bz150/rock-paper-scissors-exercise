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

options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)

print("The computer chose:", computer_choice)

exit()

#determining who won

print("-------------------")
print("Oh, the computer won. It's ok.")

print("-------------------")

print("Thanks for playing. Please play again!")