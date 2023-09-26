import random


def user_guess(x):
    """
    Function that generates a random number between 1 and 100
    """
    number = random.randint(1, x)
    user_guess = 0
    while user_guess != number:
        user_guess = int(input(f'Make a guess between 1 and {x}:\n'))

        if (user_guess < number):
            print('Sorry you guessed to low, guess again!')
        elif (user_guess > number):
            print('Sorry you guessed to high, guess again!')
        else:
            print(f'Woho you guessed correct, it was {number}!')


def computer_guess(x):
    """
    Function that makes the computer guess a number the user think about
    """
    low = 1
    high = x
    response = ''
    while response != 'r':
        guess = random.randint(low, high)
        response = input(f'Is {guess} to low (L), to high (H), or right (R)?\n')
        if response == 'l':
            low = guess + 1
        elif response == 'h':
            high = guess - 1

    print(f'The computer guessed your number, {guess}!')        


"""
Calling the functions
"""
user_guess(100)
computer_guess(100)
