#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Number Guessing Game

This is a simple number guessing game.
The player has to guess a number between 1 and 100.
The player has a maximum of 6 attempts to guess the number.
Hints are provided when the player's guess is too high or too low."""

import random


def guess_number(target, attempts):
    """ Function to guess the number

    :param target: The number to guess
    :param attempts: Number of attempts left

    :return: True if the number is guessed correctly, False otherwise
    """
    if attempts == 0:
        return False
    guess = int(input(f"Attempt {7 - attempts}: Enter your guess: "))
    if guess < target:
        print("Too low!")
        return guess_number(target, attempts - 1)
    if guess > target:
        print("Too high!")
        return guess_number(target, attempts - 1)
    print("You guessed it! The number was", target)
    return True


def main(guess_number_call=guess_number, attempts_left=6, max_number=100):
    """ Main function to run the number guessing game

    :param guess_number_call: Function to guess the number
    :param attempts_left: Number of attempts left
    :param max_number: Maximum number to guess

    :return: True if the number is guessed correctly, False otherwise
    """
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {max_number}.")
    print("Try to guess the number.", end=" ")
    print(f"You have got a maximum of {attempts_left} attempts.")

    target = random.randint(1, max_number)

    guessed_correctly = guess_number_call(target, attempts_left)
    if not guessed_correctly:
        print("Sorry, you have run out of attempts. The number was", target)
    return guessed_correctly


if __name__ == "__main__":
    main()  # pragma: no cover
