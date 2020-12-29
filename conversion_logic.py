# create the value map from a list of symbols
def create_value_map(a_string):
    symbols_list = a_string.split(",")

    empty_count = symbols_list.count("")
    for empty_element in range(empty_count):
        symbols_list.remove("")

    value_map = {}
    for value, symbol in enumerate(symbols_list):
        value_map[symbol.strip()] = value

    return value_map

# return numbers in the new number system
def convert_to_int(number_repr, value_map):
    string_repr = str(number_repr)
    integer = 0
    base = len(value_map)
    for place_value, symbol in enumerate(string_repr[::-1]):
        value = value_map[symbol]
        integer += value * base ** place_value
    return integer