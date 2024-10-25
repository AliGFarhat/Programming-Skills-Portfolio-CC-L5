import random

# Displays the Menu called "DIFFICULTY LEVEL"
def displayMenu():
    print("DIFFICULTY LEVEL")
    
    # Options given
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

# Defines the "randomInt" function and the parameter "difficulty".
def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(0, 9)
    
    elif difficulty == 2:
        return random.randint(10, 99)
    
    elif difficulty == 3:
        return random.randint(1000, 9999)

# Selects a Random Operation from the list. Either + or -
def decideOperation():
    return random.choice(['+', '-'])

# This function combines num1, num2, and operation which are all randomized respectively to their difficulty picked into a problem.
def displayProblem(num1, num2, operation):
    if operation == '+':
        return f"{num1} + {num2} = "
    
    else:
        return f"{num1} - {num2} = "

# This function checks if the input and answer parameters are the equal to each other.
def isCorrect(user_input, answer):
    return user_input == answer

# This function displays the total 'points' the user has gotten after all 10 questions are finished
def displayResults(points):
    print(f"Final Score: {points}/100")

    # The if statement will give a grading according to your total 'points'
    if points > 90:
        print("A+")
    elif points > 80:
        print("A")
    elif points > 70:
        print("B")
    elif points > 60:
        print("C")
    # Prints out fail if 'points' is below 60.
    else:
        print("F")

# The quiz function calls another function called displayMenu. The difficulty parameter takes integer user input and displays a prompt "Select a Difficulty Level: "
def quiz():
    displayMenu()

    difficulty = int(input("Select a Difficulty Level: "))
    points = 0

    for _ in range(10):

        num1 = randomInt(difficulty)
        num2 = randomInt(difficulty)
        operation = decideOperation()

        # If the operation is + it will tell the code that answer is equal to num1 + num2. Same with the '-' operator.
        if operation == '+':
            answer = num1 + num2

        else:
            answer = num1 - num2
        
        problem = displayProblem(num1, num2, operation)
        user_input = int(input(problem))
        
        # Awards 10 points upon inputting the correct answer.
        if isCorrect(user_input, answer):
            points += 10

        else:
            user_input = int(input("Wrong Answer, Try again: "))

            # Gives you 1 extra try for that question if you get it right on the second try, it will award 5 points.
            if isCorrect(user_input, answer):
                points += 5

    displayResults(points)

while True:
    quiz()

    # Asks the user if they want to replay the quiz, with only two inputs available being y for yes or n for no.
    again = input("Replay? (y/n): ").strip().lower()

    if again != 'y':

        break