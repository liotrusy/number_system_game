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

print("""
This application helps you create a number system. Let's get started!
To begin, insert the symbols you want to use to represent your numbers.
Please insert the symbols separated by a comma (,) starting from the one you'd like to represent 0.
NOTE: In this program the comma (,) cannot be a symbol ;)

Here, an example. Let's say we want to use the letters of the word 'hello' to create your number system.
In this example we would say (starting from 0) that 'h' = 0, 'e'= 1, 'l' = 2, 'l' = 3, 'o' = 4.
So, to create this number system you'd have to type below: h,e,l,l,o.

Now, it's your turn! Create your own number system.
Insert below the symbols here - remember start from 0, and separate the symbols with a comma (,).""")

symbols = input(">> ")
value_map = conv.create_value_map(symbols)

### must ensure that the input is clean


print("""
Great you have created your number system. Let's see if you can create and call correctly a number.
Now, type below a number using your number system.""")

again = "y"
while again == "y":
    number_input = input("Type your number here: ")
    correct_guess = int(input("So, what number was it? "))
    correct_guess_checker(value_map, number_input, correct_guess)
    again = input("\nDo you want to play again? [y/n]")


print("Thanks for playing! See you next time")




