import random

"""
Generates a random number between 1 and 100
"""

number = random.randint(1,100)

"""
Stores the guesses that the user makes
"""

guess = 0

while guess != number:
    guess = int(input("Make a Guess:"))

    if (guess < number):
        print("Sorry you guessed to low, guess again")
    elif (guess > number):
        print("Sorry you guessed to high, guess again!")
    else:
        print("Woho you guessed correct!")



