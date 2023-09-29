# Guess The Number

Guess The Number is a python terminal game. Users play against the computer by guessing a number that the computer randomly has chosen. The player can also decide a number and let the computer guess it. 

[Here is the live version of my project](https://guess-the-number-juliachelsie-12b6099377e2.herokuapp.com/)

## How to play

 The computer will ask the user to guess a number between 1 and 20, if the user guess a number that is too high the computer will print "Sorry you guessed too high, guess again!". If the user guess a number that is too low, the computer will print "Sorry you guessed too low, guess again!". If the user guess the right number the computer will print "Woho you guessed correct, it was (number)!"

The user can also decide a number and let the computer guess it. The computer will print out "Is (number) too low(L), too high(H), or right(R)?" and the user can choose to press "L" if it is too low, "H" if it is too high or "R" if the number the computer guessed is right. When the computer guesses right the frase "The computer guessed your number, (number)!" will print and the game is over. 

## Features

### Existing features

#### Entering a name

- The computer will ask the user to enter a name, then greets the user by that name and the game starts

![Name](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/welcomename.PNG)

#### User guessing the number

- The computer asks the user to guess a number between 1 and 20

![MakeGuess](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/makeguess2.PNG)

- The computer print different answers if the user guessed too low, too high or right.

- If the user guesses anything else than a number, a message prints that tells the user to only enter numbers.

![Guess]()

![Guess_High_Low](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/user-guess-high-low.PNG)

- The computer print a message that tells the user that the guess was right.

![Result](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/result-user2.PNG)

#### The computer guessing the number

- When the user guessed right, it's the computers turn to guess. A message prints that easily explains for the user how it is going to work.

![ComputerTurn](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/computerturn.PNG)

- The computer prints a message asking the user if the number is too low, too high or right. The user press a key (L/H/R).

![copmuter_guessing](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/comnputer-guess.PNG)

- When the computer guesses the right number a message prints.

![ComputerWin](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/computer-result.PNG)

### Features left to implement
- I would like to set a limit of tries when the user guesses against the computer. It will make the game a bit harder.
- I would also like to correct the code so that when the computer guesses the number, the user can only enter "H", "L" or "R". If the user enters anything else a text will appear that tells the user to try again. I did not have the time for that now.

## Testing

I have tested the code through a PEP8 linter and confirmed that there are no problems or errors.

![Testing](https://github.com/juliachelsie/guess-the-number/blob/main/documentation/test-validator.PNG)

### Bugs
There are no bugs.

## Deployment

The project was deployed using Code Institute's moch terminal for Heroku.

Steps I followed for deployment:
- I cloned the repository
- I created a new Heroku app 
- I set the buildpacks to Python and NodeJS
- I linked the Heroku app to the repository
- I clicked on Deploy

## Credits

- Code Institute for the deployment terminal
- I searched the internet for ideas for this project and found an article that i took inspiration from on [UpGrad](https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/)
- I imported the random module to my project and read all about it at [python](https://docs.python.org/3/library/random.html)


