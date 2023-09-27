# Guess The Number

Guess The Number is a python terminal game. Users play against the computer by guessing a number that the computer randomly has chosen. The player can also decide a number and let the computer guess it. 

[Here is the live version of my project](https://guess-the-number-juliachelsie-12b6099377e2.herokuapp.com/)

## How to play

 The computer will ask the user to guess a number between 1 and 100, if the user guess a number that is to high the computer will print "Sorry you guessed to high, guess again!". If the user guess a number that is to low, the computer will print "Sorry you guessed to low, guess again!". If the user guess the right number the computer will print "Woho you guessed correct, it was (number)!"

The user can also decide a number and let the computer guess it. The computer will print out "Is (number) to low(L), to high(H), or right(R)?" and the user can choose to press "L" if it is to low, "H" if it is to high or "R" if the number the computer is guessing s right. When the computer guess right the frase "The computer guessed your number, (number)!" will print and the game is over. 

## Features

### User guessing the number

- The computer asks the user to guess a number between 1 and 100

![MakeGuess](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/makeguess.PNG)

- The computer print different answers if the user guessed to high, low or right.

![Guess_High_Low](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/guess-high-low.PNG)

- The computer print a message that telles the user that the guess was right.

![Result](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/result-user.PNG)

### The computer guessing the numer

- The computer prints a message asking the user if the number is to low, to high or right. The user press a key (L/H/R).

![copmuter_guessing](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/computer-guess.PNG)

- When the computer guess the right number a message prints.

![ComputerWin](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/computer-right.PNG)

## Testing

I have tested the code through a PEP8 linter and confirmed that there are no problems or errors.

![Testing](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/test-validator.PNG)

### Bugs

There are no bugs.

## Deployment

The project was deployed using Code Institute's moch terminal for Heroku.

Steps i followed for deployment:
- I cloned the repository
- I created a new Heroku app 
- I set the buildpacks to Python and NodeJS
- I linked the Heroku app to the repository
- Then i clicked on Deploy

## Credits

- Code Institute for the deployment terminal
- I searched the internet for ideas for this project and found an article that i took inspiration from on [UpGrad](https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/)
- I imported the random module to my project and read all about it at [python](https://docs.python.org/3/library/random.html)


