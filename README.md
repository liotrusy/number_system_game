# Game to create a number system and test its logic

This small application allow the user to create a number system and check his/her/their knowledge of this new number system. This means that the user will be able to:

* create a number system from a sequence of unique single characters separated by a comma
* ensure that the sequence inputted by the user does not include duplicates, or double symbols to represent base numbers.
* test the new number system by inputting a number using the new notation, inputting a guess (as integer) and checking whether the guess corresponds to the right number

## Installation and Exectution

```bash 
# clone repository
git clone https://github.com/liotrusy/number_system_game.git

```

### Prerequisites

* Python 3 - here is the [download link](https://www.python.org/downloads/). Make sure that python is added to PATH variable.
* Pip. If you install a Python version greater than 3.4 pip is installed together with your Python distribution.<
* Pytest. Run the following command in the prompt: `` pip install pytest ``

### Run the application

Type the following command in the prompt opened in the same directory (folder) where you've cloned the repository.

```bash
# for Windows
python play_game.py

# for Linux or Mac
python3 play_game.py

```

## Development notes

The application has been written in Python and tested on a Windows machine with a Python 3.9 installation.

The conversion logic and input cleaning components are stored in the file "conversion_logic.py". This was done primarily to isolate the number system creation logic from the main game application - this would help further development and modifications.

The development of the game function and core conversion logic has been done using TDD techniques.

To run the tests on the conversion logic, type the following command in the prompt opened in the same directory (folder) where you've cloned the repository: 

```bash
# for number system conversion logic
pytest test_conversion_logic.py

# for answer checking
pytest test_answer_checker.py

```