import random


def get_user_name():

    while True:
        print('Welcome to a game where you guess a number the computer picked')
        print('You can only guess numbers.')
        print("Enter your name please:")
        name = input()
        print(f"Hello {name}! Let's play!\n")
        break


def user_guess(x):
    """
    Function that generates a random number between 1 and 20
    """
    number = random.randint(1, x)
    user_guess = 0
    while user_guess != number:
        user_guess = int(input(f'Make a guess between 1 and {x}:\n'))

        if (user_guess < number):
            print('Sorry you guessed too low, guess again!\n')
        elif (user_guess > number):
            print('Sorry you guessed too high, guess again!\n')
        else:
            print(f'Woho you guessed correct, it was {number}!\n')


def computer_guess(x):
    """
    Function that makes the computer guess a number the user think about
    """
    print(f"Now it's your turn to pick a number between 1 and {x}!")
    print('The computer will now guess your number.')
    print("Press H if it's to high, L if it's to low and R if it's right!\n")
    low = 1
    high = x
    response = ''
    while response != 'r':
        guess = random.randint(low, high)
        response = input(f'Is {guess} too low(L), too high(H), or right(R)?\n')
        if response == 'l':
            low = guess + 1
        elif response == 'h':
            high = guess - 1

    print(f'The computer guessed your number, {guess}!')


"""
Calling functions
"""
get_user_name()
user_guess(20)
computer_guess(20)
