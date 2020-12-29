import pytest
import conversion_logic

class TestValueMap:
    def test_mapping(self):
        values_map = conversion_logic.create_value_map("a, b, c")
        target_map = {'a': 0, 'b': 1, 'c': 2}
        assert values_map == target_map

    def test_remove_empty_elements(self):

        values_map = conversion_logic.create_value_map("a,b,c,")
        target_map = {'a': 0, 'b': 1, 'c': 2}
        assert values_map == target_map

        values_map = conversion_logic.create_value_map(",a,,b,c,")
        target_map = {'a': 0, 'b': 1, 'c': 2}
        assert values_map == target_map

class TestConversionOutput:

    def test_type(self):
        value_map = {"0": 0, "1": 1}
        output = conversion_logic.convert_to_int('100',value_map)
        assert type(output) == int

    def test_output(self):
        value_map = {"0": 0, "1": 1}
        output = conversion_logic.convert_to_int('100',value_map)
        assert  output == 4

        value_map = {'a': 0, 'b': 1, 'c': 2}
        output = conversion_logic.convert_to_int('bb', value_map)
        assert output == 4
