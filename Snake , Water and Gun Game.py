# SNAKE , WATER & GUN GAME!!!


import random     #importing random module

s = "snake"
w = "water"
g = "gun"


def Game():

    choices = [s , w, g]

    u = input("You chose: ")

    c = random.choice(choices)
    print(f"Computer chose: {c}\n")


    if u not in choices:
        print('Invalid Entry. Please choose from snake , water and gun.\n')


    if (c == u):
        print("It's a tie between computer an you.")


    elif (c == s):
        if (u == w):
            print("Computer Won!!! \nYou Lost!!!")

        else:
            print("You Won!!! \nComputer Lost!!!")


    elif (c == w):
        if (u == g):
            print("Computer Won!!! \nYou Lost!!!")
        else:
            print("You Won!!! \nComputer Lost!!!")


    elif (c == g):
        if (u == s):
            print("Computer Won!!! \nYou Lost!!!")
        else:
            print("You Won!!! \nComputer Lost!!!")


Game() 