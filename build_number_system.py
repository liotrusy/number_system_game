def separate_symbols(symbols:str, separator:str):
    """Returns clean symbol list from a string of symbols"""
    symbols_list = symbols.split(separator)

    empty_count = symbols_list.count("")
    for empty_element in range(empty_count):
        symbols_list.remove("")

    for index, symbol in enumerate(symbols_list):
        symbols_list[index] = symbol.strip()

    return symbols_list
    
def check_for_no_duplicate_symbols(symbol_list:list):
    """control that a given list of symbos does not contain duplicate values"""
    if len(symbol_list) != len(set(symbol_list)):
        return True
    return False

def check_for_no_double_symbols(symbol_list:list):
    """check for no dobule symbols in the new number system"""
    for symbol in symbol_list:
        if len(symbol) > 1:
            return True
    return False

def create_value_map(symbol_list:list):  
    """creates a value map from a given symbol list of unique values"""
    value_map = {}
    for value, symbol in enumerate(symbol_list):
        value_map[symbol] = value
    return value_map

def convert_to_int(number_repr:str, value_map: dict):
    """converts a number from newly created number system to integer"""
    string_repr = str(number_repr)
    integer = 0
    base = len(value_map)
    for place_value, symbol in enumerate(string_repr[::-1]):
        value = value_map[symbol]
        integer += value * base ** place_value
    return integer