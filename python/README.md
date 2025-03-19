# Number Guessing Game

This is an implementation of the good old Number Guessing game in Python.

[![Super-Linter](https://github.com/OMerkel/number_guessing/actions/workflows/super-linter.yml/badge.svg)](https://github.com/OMerkel/number_guessing/actions/workflows/super-linter.yml)
[![Flake8 Pytest Coverage](https://github.com/OMerkel/number_guessing/actions/workflows/py_flake8_pytest_cov.yml/badge.svg)](https://github.com/OMerkel/number_guessing/actions/workflows/py_flake8_pytest_cov.yml)
[![Pylint](https://github.com/OMerkel/number_guessing/actions/workflows/pylint.yml/badge.svg)](https://github.com/OMerkel/number_guessing/actions/workflows/pylint.yml)

## Rules

The player has to guess a secret number between 1 and 100. The player has a maximum of 6 attempts to guess the number. Hints are provided when the player's guess is too high or too low.

## Setup / Usage

Assumed you have Python 3 installed you can issue the following commands.

Prepare your environment and install site packages.

```bat
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pdm update
```

Run the unit tests only.

```bat
pdm run pytest -v
```

Run the unit tests and show line coverage.

```bat
pdm run pytest -v --cov=.
```

Actually play the Number Guessing game.

```bat
pdm run number_guessing.py
```

## Software Architecture Constraints

The implementation targets to follow functional programming interfaces.
As such any for-loops and while-loops are avoided. All variables are treated as immutable.
Once defined and initialized these are not allowed to be overwritten.

To implement unit tests a mocking of user inputs is used.
The possible IO side effects of user input and random number generation needs to be addressed.

Thus a recursive function guess_number is handling the gane play.

```Python
def guess_number(target, attempts):
    """Function to guess the number

    :param target: The number to guess
    :param attempts: Number of attempts left

    :return: True if the number is guessed correctly, False otherwise
    """
```

A main function is initializing the game play with intended settings.

```Python
def main(guess_number_call=guess_number, attempts_left=6, max_number=100):
    """Main function to run the number guessing game

    :param guess_number_call: Function to guess the number
    :param attempts_left: Number of attempts left
    :param max_number: Maximum number to guess

    :return: True if the number is guessed correctly, False otherwise
    """
```

## Gherkin / Requirements

```Gherkin
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

## Pytest and Test Coverage

Find the tests implemented in the directory named _tests_

The line coverage of the tests will be close to 100%.
