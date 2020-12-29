import pytest
import number_system_apps as numapp

def test_knowledge_test():
    value_map = {"0": 0, "1": 1}
    number_input = "10"
    guess = 2
    output = numapp.guess_checker(value_map, number_input, guess)
    assert output == True

    value_map = {"0": 0, "1": 1}
    number_input = "100"
    guess = 2
    output = numapp.guess_checker(value_map, number_input, guess)
    assert output == False