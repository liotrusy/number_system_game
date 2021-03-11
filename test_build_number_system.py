import pytest
import build_number_system

class TestInputCorrections:

    def test_separate_symbols(self):
        separator = ","
        assert build_number_system.separate_symbols(",a,,b,c,", separator) == ['a', 'b', 'c']
        assert build_number_system.separate_symbols("h,e,l,l,o,", separator) == ['h', 'e', 'l', 'l', 'o']
        assert build_number_system.separate_symbols("a ,b, c  ", separator) == ['a', 'b', 'c']

    def test_stop_duplicate_values(self):
        assert build_number_system.check_for_no_duplicate_symbols(['h', 'e', 'l', 'l', 'o']) == True
        assert build_number_system.check_for_no_duplicate_symbols(['h', 'e', 'l', 'o']) == False

    def test_stop_doubple_symbols(self):
        assert build_number_system.check_for_no_double_symbols(['he', 'l', 'o']) == True
        assert build_number_system.check_for_no_double_symbols(['h', 'l', 'o']) == False

class TestValueMap:

    def test_mapping_only_characters(self):
        values_map = build_number_system.create_value_map(['a', 'b', 'c'])
        target_map = {'a': 0, 'b': 1, 'c': 2}
        assert values_map == target_map

    def test_mapping_only_numbers(self):
        values_map = build_number_system.create_value_map(['0','1','2'])
        target_map = {'0': 0, '1': 1, '2': 2}
        assert values_map == target_map

    def test_mapping_mix_numbers_and_characters(self):
        values_map = build_number_system.create_value_map(['a', '0', 'h'])
        target_map = {'a': 0, '0': 1, 'h': 2}
        assert values_map == target_map

class TestConversionOutput:

    def test_type(self):
        value_map = {"0": 0, "1": 1}
        output = build_number_system.convert_to_int('100',value_map)
        assert type(output) == int

    def test_output(self):
        value_map = {"0": 0, "1": 1}
        output = build_number_system.convert_to_int('100',value_map)
        assert  output == 4

        value_map = {'a': 0, 'b': 1, 'c': 2}
        output = build_number_system.convert_to_int('bb', value_map)
        assert output == 4
