import pytest
import answer_checker

class TestCorrectSymbol:

    def test_are_symbols_correct(self):
        value_map = {"0": 0, "1": 1}
        number_input = "100a"
        check_outcome = answer_checker.are_the_symbols_correct(value_map, number_input)
        assert check_outcome == False

class TestGuessChecker():

    def test_true(self):
        value_map = {"0": 0, "1": 1}
        number_input = "10"
        guess = 2
        output = answer_checker.correct_guess_checker(value_map, number_input, guess)
        assert output == True

    def test_false(self):
        value_map = {"0": 0, "1": 1}
        number_input = "100"
        guess = 2
        output = answer_checker.correct_guess_checker(value_map, number_input, guess)
        assert output == False


    