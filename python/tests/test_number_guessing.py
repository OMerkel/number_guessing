""" Tests for the number_guessing module. """
# pylint: disable=redefined-outer-name
# import pytest
from number_guessing import guess_number
from number_guessing import main


def test_number_guessing_correct(monkeypatch):
    """Test for correct number guessing

    GIVEN a number to guess and the correct number
    WHEN the user guesses the correct number
    WHEN there are still attempts left
    THEN the guess_number function should return True
    """
    expected_guess = 5
    expected_value = True
    attempts = 6
    inputs = iter([expected_guess])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert guess_number(expected_guess, attempts) is expected_value


def test_number_guessing_too_low(monkeypatch):
    """Test for number guessing too low

    GIVEN a number to guess
    AND a set of guesses finally listing the correct number
    WHEN the user guesses a number lower followed by the correct number
    WHEN there are still attempts left
    THEN the function should call itself recursively
    THEN the next user input is consumed
    THEN the guess_number function should return True
    """
    expected_guess = 5
    expected_value = True
    lower_guess = 3
    attempts = 6
    inputs = iter([lower_guess, expected_guess])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert guess_number(expected_guess, attempts) is expected_value


def test_number_guessing_too_high(monkeypatch):
    """Test for number guessing too high

    GIVEN a number to guess
    AND a set of guesses finally listing the correct number
    WHEN the user guesses a number higher followed by the correct number
    WHEN there are still attempts left
    THEN the function should call itself recursively
    THEN the next user input is consumed
    THEN the guess_number function should return True
    """
    expected_guess = 5
    expected_value = True
    higher_guess = 7
    attempts = 6
    inputs = iter([higher_guess, expected_guess])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert guess_number(expected_guess, attempts) is expected_value


def test_number_guessing_run_out_of_attempts(monkeypatch):
    """Test for running out of attempts

    GIVEN a number to guess
    AND a set of guesses that are all incorrect
    WHEN the user runs out of attempts
    THEN the guess_number function should return False
    """
    expected_guess = 10
    expected_value = False
    attempts = 6
    inputs = iter([1, 2, 3, 4, 5, 6])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert guess_number(expected_guess, attempts) is expected_value


def test_main(monkeypatch):
    """Test for main function if guess is performed without attempts left

    GIVEN the situation that the user has no attempts left
    WHEN the main function is called
    THEN the function should return False
    """
    inputs = iter([5])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert main(attempts_left=0) is False
