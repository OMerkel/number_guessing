# Number Guessing Game

This is an implementation of the good old Number Guessing game.

## Rules

* The player has to guess a number between 1 and 100.
* The player has a maximum of 6 attempts to guess the number.
* Hints are provided when the player's guess is too high or too low.

## Software Architecture Constraints

The implementation targets to follow functional programming interfaces.
As such any for-loops and while-loops are avoided. All variables are treated as immutable.
Once defined and initialized these are not allowed to be overwritten.

To implement unit tests a mocking of user inputs is used.
The possible IO side effects of user input and random number generation needs to be addressed.

Thus a recursive function guess_number is handling the gane play.

```
def guess_number(target, attempts):
    """ Function to guess the number

    :param target: The number to guess
    :param attempts: Number of attempts left

    :return: True if the number is guessed correctly, False otherwise
    """
```

A main function is initializing the game play with intended settings.

```
def main(guess_number_call=guess_number, attempts_left=6, max_number=100):
    """ Main function to run the number guessing game

    :param guess_number_call: Function to guess the number
    :param attempts_left: Number of attempts left
    :param max_number: Maximum number to guess

    :return: True if the number is guessed correctly, False otherwise
    """
```

## Gherkin / Requirements

```
Feature: Player is guessing a secret number in specified range and gets hints on his guess.

Scenario: Test for correct number guessing

GIVEN a number to guess and the correct number
WHEN the user guesses the correct number
WHEN there are still attempts left
THEN the guess_number function should return True

Scenario: Test for number guessing too low

GIVEN a number to guess
AND a set of guesses finally listing the correct number
WHEN the user guesses a number lower followed by the correct number
WHEN there are still attempts left
THEN the function should call itself recursively
THEN the next user input is consumed
THEN the guess_number function should return True

Scenario: Test for number guessing too high

GIVEN a number to guess
AND a set of guesses finally listing the correct number
WHEN the user guesses a number higher followed by the correct number
WHEN there are still attempts left
THEN the function should call itself recursively
THEN the next user input is consumed
THEN the guess_number function should return True

Scenario: Test for running out of attempts

GIVEN a number to guess
AND a set of guesses that are all incorrect
WHEN the user runs out of attempts
THEN the guess_number function should return False

Scenario: Test for main function if guess is performed without attempts left

GIVEN the situation that the user has no attempts left
WHEN the main function is called
THEN the function should return False

```

# Pytest and Test Coverage

Find the tests implemented in the directory named _tests_

The line coverage of the tests will be close to 100%.
