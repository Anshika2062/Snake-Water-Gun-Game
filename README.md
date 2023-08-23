# Snake-Water-Gun-Game

This is a simple console-based implementation of the classic game "Snake, Water, Gun" using Python. The game allows a user to play against the computer by choosing one of the three options: snake, water, or gun. The computer's choice is generated randomly, and the winner is determined based on the chosen options.

# How to Play

1. Make sure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory where you have saved the repository files.
5. Run the following command to start the game:

```
python snake_water_gun.py

```

6. The game will prompt you to enter your choice (snake, water, or gun).
7. After you make your choice, the computer's choice will be displayed, and the winner will be announced.

# Rules

- Snake beats Water (Snake drinks Water)
- Water beats Gun (Water rusts Gun)
- Gun beats Snake (Gun shoots Snake)

# Implementation Details

The game is implemented using Python's `random` module for generating the computer's choice. The user's choice is taken as input using the `input()` function. The comparison of choices and determination of the winner are done using if-else statements.



