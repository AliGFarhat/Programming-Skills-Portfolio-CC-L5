# Imports a module called 'random' to generate random numbers when called.
import random

# loads the argument 'jokesfile'.
def load_jokes(jokesfile):

# Opens the jokesfile in 'r' meaning read mode.
    with open(jokesfile, 'r') as file:

# Reads all the lines from the 'jokesfile' and stores them in a list to be called randomly later on.
        jokes = file.readlines()

# Using the 'strip()' method this removes all the leading and trailing whitespaces.
    return [joke.strip() for joke in jokes]

# A function that tells a joke from the list of jokes.
def tell(jokes):

# Calling the module 'random' to select a random joke from the jokes list.
    joke = random.choice(jokes)

# Splits the selected random joke into two parts the setup, then the punchline.
    setup, punchline = joke.split('?')

# Prints the setup first, then user pressses Enter to proceed to the punchline, thus completing the joke.
    print(setup + '?')
    input("[Press Enter]")
    print(punchline)

def main():

# Loads the .txt file which contains the jokes list.
    jokes = load_jokes('C:\\Users\\User\\Documents\\GitHub\\CODELAB-2--A1\\Exercise 2 - Alexa tell me a joke\\randomJokes.txt')

# Starts the infinite loop until user says 'quit'. 
    while True:

# The .strip and .lower trims down the users input by making it lowercased when read by the code and makes it remove the leading and trailing whitespaces.
        command = input("Say 'Alexa tell me a Joke' or 'Quit' to exit: ").strip().lower()

        if command == 'alexa tell me a joke':
            tell(jokes)

# 'Else if' the user types quit, it will then proceed the 'break' statement which exits the loop and stopping the program. 
        elif command == 'quit':

            break

# If anything else is inputted besides the specified commands, it will print out "Invalid Input".
        else:
            print("Invalid Input")

# Ensures that the main() function runs only when the script is executed directly from the user starting the program.
if __name__ == "__main__":
    main()