import conversion_logic as conv

def correct_guess_checker(value_map, number_input, correct_guess):

    if set(number_input) != set(value_map.keys()):
        print("You have used characters not included in your number system")
        return "wrong characters"

    number_int = conv.convert_to_int(number_input, value_map)
    result = number_int == correct_guess

    if result:
        print(f"Yes, the number {number_input} is equal to {correct_guess}.")
    else:
        print(f"Sorry, the number {number_input} is not equal to {correct_guess}, it is actually {number_int}")
        print("Here is a map of your number system")
        print(value_map)
    
    return result

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

# capture inputs from player
symbols = input(">> ")

# ensure that input is not empty
while not symbols:
    print("\nWhat, no input?! We need symbols to create your number system! Please insert the symbols you'd like to use. (Otherwise, no hard feelings. Enter CTRL + D to interrupt the game)")
    symbols = input(">> ")

# ensure that the symbol list includese more 2 or more characters
symbol_list = conv.clean_input(symbols)
while len(symbol_list) < 2:
    print("\nOops.. you must use 2 or more symbols to create for your own number system! Please insert a new set of symbols. (If you want to stop playing enter CTRL + D to interrupt the game)")
    symbols = input(">> ")
    symbol_list = conv.clean_input(symbols)

# prevent player to move on if inputs are not unique symbols
while conv.check_for_no_duplicates(symbol_list):
    print("\nATTENTION: You cannot have duplicates symbols of your number system! Otherwise how can you tell the difference between two numbers with the same symbol.")
    print("Just go ahead and insert a new set of symbols (Or, if you want to stop the game enter CTRL + D)")
    symbols = input(">> ")
    symbol_list = conv.clean_input(symbols)

print("Thanks, let's continue!")

# create a value map


# value_map = conv.create_value_map(symbols)

# ### must ensure that the input is clean


# print("""
# Great you have created your number system. Let's see if you can create and call correctly a number.
# Now, type below a number using your number system.""")

# again = "y"
# while again == "y":
#     number_input = input("Type your number here: ")
#     correct_guess = int(input("So, what number was it? "))
#     correct_guess_checker(value_map, number_input, correct_guess)
#     again = input("\nDo you want to play again? [y/n]")


# print("Thanks for playing! See you next time")




