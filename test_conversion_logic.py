import pytest
import conversion_logic

class TestInputCorrections:

    def test_input_cleaning(self):
        assert conversion_logic.clean_input(",a,,b,c,") == ['a', 'b', 'c']
        assert conversion_logic.clean_input("h,e,l,l,o,") == ['h', 'e', 'l', 'l', 'o']
        assert conversion_logic.clean_input("a ,b, c  ") == ['a', 'b', 'c']

    def test_stop_duplicate_values(self):
        assert conversion_logic.check_for_no_duplicates(['h', 'e', 'l', 'l', 'o']) == True
        assert conversion_logic.check_for_no_duplicates(['h', 'e', 'l', 'o']) == False

class TestValueMap:

    def test_mapping_only_characters(self):
        values_map = conversion_logic.create_value_map(['a', 'b', 'c'])
        target_map = {'a': 0, 'b': 1, 'c': 2}
        assert values_map == target_map

    def test_mapping_only_numbers(self):
        values_map = conversion_logic.create_value_map(['0','1','2'])
        target_map = {'0': 0, '1': 1, '2': 2}
        assert values_map == target_map

    def test_mapping_mix_numbers_and_characters(self):
        values_map = conversion_logic.create_value_map(['a', '0', 'hel'])
        target_map = {'a': 0, '0': 1, 'hel': 2}
        assert values_map == target_map


# class TestConversionOutput:

#     def test_type(self):
#         value_map = {"0": 0, "1": 1}
#         output = conversion_logic.convert_to_int('100',value_map)
#         assert type(output) == int

#     def test_output(self):
#         value_map = {"0": 0, "1": 1}
#         output = conversion_logic.convert_to_int('100',value_map)
#         assert  output == 4

#         value_map = {'a': 0, 'b': 1, 'c': 2}
#         output = conversion_logic.convert_to_int('bb', value_map)
#         assert output == 4
