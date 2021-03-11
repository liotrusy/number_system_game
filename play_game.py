import conversion_logic as conv
import answer_checker

def get_opening_message(file_name:str):
    with open(file_name, encoding="utf8") as message_file:
        opening_message = message_file.read()
    return opening_message

def prevent_passing_of_empty_answer(symbols:str):
    """ Prevent user to continue without inserting symbols"""
    while not symbols:
        print("\nNo input?! We need symbols to create your number system! Please insert the symbols you'd like to use.")
        symbols = input(">> ")
    return symbols 

def return_clean_symbol_list(symbols:str, separator:str):
    """ Returns list with more than 2 values, no duplicate symbols or double symbols"""

    symbols = prevent_passing_of_empty_answer(symbols)
    symbol_list = conv.separate_symbols(symbols, separator)

    while len(symbol_list) < 2:
        print("\nWe need at least 2 symbols in your number system! Please insert a new set of symbols.")
        symbols = input(">> ")
        symbol_list = conv.separate_symbols(symbols, separator)

    while conv.check_for_no_duplicate_symbols(symbol_list):
        print("\nYou've inseted duplicates. If your system has duplicates you can't you tell the difference between two numbers.")
        print("Just go ahead and insert a new set of symbols-")
        symbols = input(">> ")
        symbol_list = conv.separate_symbols(symbols, separator)

    while conv.check_for_no_double_symbols(symbol_list):
        print("\nWatch out! Your base numbers can be represented by only one symbol - no double symbols allowed.")
        print("Just go ahead and insert a new set of symbols")
        symbols = input(">> ")
        symbol_list = conv.separate_symbols(symbols, separator)

    return symbol_list

def play_game(play="y"):
    """ Runs game. Player can choose to play again"""
    opening_message = get_opening_message("opening_message.txt")

    print(opening_message)
    symbols = input(">> ")
    separator = ","

    symbol_list = return_clean_symbol_list(symbols, separator)
    value_map = conv.create_value_map(symbol_list)
    print("Great, now you've got a number system. Here it is:",value_map, sep="\n")
    print("Now, we can start playing. Create a number and guess it correctly!")
    
    while play == "y":
        number_input = input("Type a number using your number system here: ")
        correct_symbols = answer_checker.are_the_symbols_correct(value_map, number_input)
        if not correct_symbols:
            play = input("\nDo you want to try again? [y/n] >> ")
        else:
            correct_guess = int(input("So, what number was it? "))
            answer_checker.correct_guess_checker(value_map, number_input, correct_guess)
            play = input("\nDo you want to play again? [y/n] >> ")

    # user sees thank you message
    print("Thanks for playing! See you next time")

    return True

if __name__ == '__main__':
    play_game()
