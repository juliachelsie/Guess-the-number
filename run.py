import random


def guess(x):
    """
    Function that generates a random number between 1 and 100
    """
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        guess = int(input(f"Make a guess between 1 and {x}:\n"))

        if (guess < number):
            print("Sorry you guessed to low, guess again!")
        elif (guess > number):
            print("Sorry you guessed to high, guess again!")
        else:
            print(f"Woho you guessed correct, it was {number}!")


"""
Calling the functions
"""
guess(100)
