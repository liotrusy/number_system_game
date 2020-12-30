def clean_input(a_string):
    symbols_list = a_string.split(",")
    empty_count = symbols_list.count("")
    for empty_element in range(empty_count):
        symbols_list.remove("")
    return symbols_list
    
def check_for_no_duplicates(symbol_list):
    """control that a given list of symbos does not contain duplicate values"""
    if len(symbol_list) != len(set(symbol_list)):
        return False
    return True


# def create_value_map(a_string):
#     """creates a value map from a given string of unique values"""
#     value_map = {}
#     for value, symbol in enumerate(symbols_list):
#         value_map[symbol.strip()] = value

#     return value_map

# # return numbers in the new number system
# def convert_to_int(number_repr, value_map):

#     """converts a number from newly created number system to integer"""
#     string_repr = str(number_repr)
#     integer = 0
#     base = len(value_map)
#     for place_value, symbol in enumerate(string_repr[::-1]):
#         value = value_map[symbol]
#         integer += value * base ** place_value
#     return integer