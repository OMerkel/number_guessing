# Number Guessing Game

This is an implementation of the good old Number Guessing game.

[![Super-Linter](https://github.com/OMerkel/number_guessing/actions/workflows/super-linter.yml/badge.svg)](https://github.com/OMerkel/number_guessing/actions/workflows/super-linter.yml)
[![Flake8 Pytest Coverage](https://github.com/OMerkel/number_guessing/actions/workflows/py_flake8_pytest_cov.yml/badge.svg)](https://github.com/OMerkel/number_guessing/actions/workflows/py_flake8_pytest_cov.yml)


## Rules

* The player has to guess a number between 1 and 100.
* The player has a maximum of 6 attempts to guess the number.
* Hints are provided when the player's guess is too high or too low.

## Subdirectory Python

The implementation in Python targets to follow functional programming interfaces.
To implement unit tests a mocking of user inputs is used.
The test files contain the unit test with requirements formulated using Gherkin.
Find the tests implemented in the directory named _tests_.
The line coverage of the tests will be close to 100%.
