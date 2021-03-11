import conversion_logic as conv

def are_the_symbols_correct(value_map:dict, user_answer:str):
    """ Returns true if symbols used in user_answer are part of the value map """

    check_outcome = True
    for symbol in user_answer:
        if not (symbol in value_map.keys()):
            print("You have used characters not included in your number system")
            check_outcome = False
    return check_outcome

def correct_guess_checker(value_map:dict, user_answer:str, correct_guess:str):
    """ Check user_answer against value map. Returns true if answer is correct """

    number_int = conv.convert_to_int(user_answer, value_map)
    check_result = number_int == correct_guess

    if check_result:
        print(f"Yes, the symbol '{user_answer}' is equal to {correct_guess}.")
    else:
        print(f"Sorry, the symbol '{user_answer}' is not equal to the number {correct_guess}, it actually represents the number {number_int}")
        print("Here is a reminder of the map of your number system")
        print(value_map)
    
    return check_result