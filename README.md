# rock-paper-scissors-exercise
Rock paper scissors project for OPIM 243

# First-Time Setup instructions

After cloning the repo into Github desktop, use `cd ~/Desktop/rock-paper-scissors-exercise` (or wherever it's located on your local drive) in the command line to navigate into the folder

Create a file using VS Code titled game.py and type in `print("Rock, Paper, Scissors, Shoot!")`

If this is the first time setting up, use the command line and type `conda create -n my-game-env python=3.8` to create the environment
Next, activate it by using the command `conda activate my-game-env`

Once you're in that virtual environment, try executing `python game.py`. If this works, you should be seeing the text string that you entered earlier!

Now you're all done with environment setup!

# Requirements - Explanation
The `input()` function is used to accept a command from the user, either "rock," "paper," or scissors." This string is converted into lower case, and if none of these are entered, it will stop the program using `exit()`

The `random.choice()` function is used to simulate a computer choice.

A series of `if` statements are then used to determine who the winner is, or if it's a tie.

# Customizing Player Name
By default, the player's name is "Player One" - this can be changed using the .env file. Please see the requirements.txt file for requirements.

To customize the player name using the .env file, first install package dependencies inside the virtual environment using `pip install -r requirements.txt`

Next, create a .env file and set USER_NAME equal to your desired name, e.g. `USER_NAME = "Bryan Zhou"`

Then, upon runing the app, you should see "Welcome 'Bryan Zhou' ..." instead of 'Player One'