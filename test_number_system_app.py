import pytest
import number_system_apps as numapp

class TestGuessChecker():

    def test_true(self):
        value_map = {"0": 0, "1": 1}
        number_input = "10"
        guess = 2
        output = numapp.guess_checker(value_map, number_input, guess)
        assert output == True

    def test_false(self):
        value_map = {"0": 0, "1": 1}
        number_input = "100"
        guess = 2
        output = numapp.guess_checker(value_map, number_input, guess)
        assert output == False

    def test_stop(self):
        value_map = {"0": 0, "1": 1}
        number_input = "100a"
        guess = 10
        output = numapp.guess_checker(value_map, number_input, guess)
        assert output == "wrong characters"


    