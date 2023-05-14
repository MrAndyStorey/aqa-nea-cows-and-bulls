# AQA Sample NEA - Task 2 – Cows and Bulls
Python and Visual Basic solutions to an AQA Sample NEA Task (Task 2 – Cows and Bulls)

## Introduction
Cows and Bulls is a guessing game where the player tries to guess a number that has been randomly generated. The randomly generated number must contain exactly four digits between 0 and 9 with no duplicate digits.

The player is asked to guess that four-digit number. This is compared to the randomly-generated four-digit number. Each individual digit entered by the player is compared to each digit within the randomly-generated number. 

If a digit is in the randomly-generated number and is in the same position in the randomly-generated number as it was in the player’s number then the digit is a “bull”. If the digit is in the randomly-generated number but is in a different position then the digit is a “cow”.

The player has won the game when they have correctly guessed the four digit randomly-generated number. A record is kept of the number of guesses it took to guess the correct number.

## Extention tasks
The code includes functionality that solves the following extention tasks that are not in the original specification:
* Highlight the number of cows and bulls text when giving the user their feedback e.g. 1234 - <font color="red">2 bulls</font>, <font color="green">0 cows</font>)
* When the user gets the number correct, let them play again instead of exiting the program.
* Tell the user if they have already entered a four-digit number.  Don’t count this as one of their guesses, but they do have them re-enter.
* Add a new command for the user to LIST all of their guesses so far, along with the number of cows and bulls for each guess

## Packages Used
Unlike VB.net and Small Basic, printing coloured text in Python is not built in.  The most common way to do this is using the [Colorama library module](https://pypi.org/project/colorama/).  Colorama allows the printing of colored text on all platforms, effectly providing constant shorthands for ANSI escape sequences.

