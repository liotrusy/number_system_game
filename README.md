# Game to create a number system and test its logic

This small application allow the user to create a number system and check his/her/their knowledge of this new number system. This means that the user will be able to:

* create a number system from a sequence of unique single characters separated by a comma
* ensure that the sequence inputted by the user does not include duplicates, or double symbols to represent base numbers.
* test the new number system by inputting a number using the new notation, inputting a guess (as integer) and checking whether the guess corresponds to the right number

To run the game on your machine, download the files (save them in the same folder):

* conversion_logic.py
* number_syste_app.py - run this file to play the game

---

## Components

The application has been written in Python and tested on a Windows machine with a Python 3.9 installation.

The conversion logic and input cleaning components are stored in the file "conversion_logic.py". This was done primarily to isolate the number system creation logic from the main game application - this would help further development and modifications.

The development of the game function and core conversion logic has been done using TDD techniques. The test runner used in this case is pytest. The test files are:
* test_conversion_logic
* test_number_system_game

The user experience of the main game has been tested mannually, both on a Linux and a Windows machine.
