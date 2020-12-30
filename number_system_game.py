import conversion_logic as conv

# starting message
print("""
This application helps you create and play around with you own number system. Let's get started!
To begin, you must insert a unique set of symbols you want to use to represent your numbers separated by a comma (,).
Start from the symbol you'd like to represent 0 with and then move onwards!

Psss... since we are seprating the symbols with the comma (,) unfortunately you will not be able to use it as a symbol in your number system ;)

Here, an EXAMPLE. Let's say we want to use the letters of the word 'game' to create your number system.
In this example we would say (starting from 0) that 'g' = 0, 'a'= 1, 'm' = 2, 'e' = 3.
So, to create this number system you'd have to type below: g,a,m,e.

Now, it's your turn! Create your own number system.
Insert below the symbols here - remember start from 0, and separate the symbols with a comma (,).""")

# users inserts inputs for new number system
symbols = input(">> ")

# users cannot continue playing until they insert a set of symbols
while not symbols:
    print("\nWhat, no input?! We need symbols to create your number system! Please insert the symbols you'd like to use. (Otherwise, no hard feelings. Enter CTRL + D to interrupt the game)")
    symbols = input(">> ")

# useres cannot continue playing until the set of symbols contains 2 or more elements
symbol_list = conv.clean_input(symbols)
while len(symbol_list) < 2:
    print("\nOops.. you must use 2 or more symbols to create for your own number system! Please insert a new set of symbols. (If you want to stop playing enter CTRL + D to interrupt the game)")
    symbols = input(">> ")
    symbol_list = conv.clean_input(symbols)

# users cannot continue playing until the symbols inserted are not unique
while conv.check_for_no_duplicates(symbol_list):
    print("\nATTENTION: You cannot have duplicates symbols of your number system! Otherwise how can you tell the difference between two numbers with the same symbol.")
    print("Just go ahead and insert a new set of symbols (Or, if you want to stop the game enter CTRL + D)")
    symbols = input(">> ")
    symbol_list = conv.clean_input(symbols)

# users cannot continue playing until the symbols inserted are not unique
while conv.check_for_no_double_symbols(symbol_list):
    print("\nWatch out! Your base numbers can be represented by only one symbol - no doubles allowed.")
    print("Just go ahead and insert a new set of symbols (Or, if you want to stop the game enter CTRL + D)")
    symbols = input(">> ")
    symbol_list = conv.clean_input(symbols)

# user can see the value map and can begin playing
value_map = conv.create_value_map(symbol_list)
print(f"""

Great you have created your number system. Here is the map of your number system:
{value_map}

Now, we can start playing. Let's see if you can create a number and guess it correctly.""")

# user guesses if the number inserted is correct until decides not to play again
def correct_guess_checker(value_map, number_input, correct_guess):

    for symbol in number_input:
        if not (symbol in value_map.keys()):
            print("You have used characters not included in your number system")
            return "wrong characters"

    number_int = conv.convert_to_int(number_input, value_map)
    result = number_int == correct_guess

    if result:
        print(f"Yes, the symbol '{number_input}' is equal to {correct_guess}.")
    else:
        print(f"Sorry, the symbol '{number_input}' is not equal to the number {correct_guess}, it actually represents the number {number_int}")
        print("Here is a reminder of the map of your number system")
        print(value_map)
    
    return result

again = "y"
while again == "y":
    number_input = input("Type a number using your number system here: ")
    correct_guess = int(input("So, what number was it? "))
    correct_guess_checker(value_map, number_input, correct_guess)
    again = input("\nDo you want to play again? [y/n]")

# user sees thank you message
print("Thanks for playing! See you next time")