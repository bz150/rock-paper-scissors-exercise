# rock-paper-scissors-exercise
Rock paper scissors project for OPIM 243

# First-Time Setup instructions

First, in the command line, navigate to the location in which the repo is store. In the case of desktop, it would be `cd ~/Desktop/rock-paper-scissors-exercise`

If this is the first time setting up, use the command line and type `conda create -n my-game-env python=3.8` to create the environment.
Next, activate it by using the command `conda activate my-game-env`

Once you're in that folder, try executing `python game.py`. If this works, you should see a welcome message and a prompt to choose your action.

# Customizing Player Name
By default, the player's name is "Player One" - this can be changed using the .env file. Please see the requirements.txt file for requirements.

To customize the player name using the .env file, first install package dependencies inside the virtual environment using `pip install -r requirements.txt`

Next, create a .env file and set USER_NAME equal to your desired name, e.g. if I were to use my name, it would be `USER_NAME = "Bryan Zhou"`

Then, upon runing the app, you should see "Welcome 'Bryan Zhou' ..." instead of 'Player One'

Alternatively, you can also run this directly from the command line using `USER_NAME = "Bryan Zhou" python my_game.py`, which will start the game as well.

# Explanation of Project Requirements
The `input()` function is used to accept a command from the user, either "rock," "paper," or scissors." This string is converted into lower case, and if none of these are entered, it will stop the program using `exit()`.

The `random.choice()` function is used to simulate a computer choice.

A series of `if` statements are then used to determine who the winner is, or if it's a tie.

Additionally, a `while` loop is used to allow the user to play more than once. This was not required, just put in for fun to practice.