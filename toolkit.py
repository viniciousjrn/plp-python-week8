import random


# Tool 1: To-Do List Manager
# Stores tasks in a list that updates dynamically while the program runs.
def todo_list_manager(tasks):
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Back to main menu")

        action = input("Choose an action (1-4): ").strip()

        if action == "1":
            if len(tasks) == 0:
                print("Your to-do list is currently empty.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif action == "2":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Added '{new_task}' to your list!")
            else:
                print("Task cannot be empty.")

        elif action == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                choice = input("Enter the task number to remove: ").strip()
                if choice.isdigit():
                    num = int(choice)
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Removed '{removed}' from your list.")
                    else:
                        print("That task number does not exist.")
                else:
                    print("Please enter a valid number.")

        elif action == "4":
            print("Returning to the main menu...")
            break
        else:
            print(f"'{action}' is not a valid option. Please enter 1, 2, 3, or 4.")


# Tool 2: Number Guessing Game
# Generates a secret number from 1 to 20 and loops until the user guesses it.
def number_guessing_game():
    secret = random.randint(1, 20)
    attempts = 0
    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number between 1 and 20.")

    while True:
        guess_text = input("Take a guess: ").strip()
        if not guess_text.isdigit():
            print("Please enter a whole number between 1 and 20.")
            continue

        guess = int(guess_text)
        attempts += 1

        if guess < 1 or guess > 20:
            print("Stay within 1 to 20!")
        elif guess < secret:
            print(f"{guess} is too low! Try again.")
        elif guess > secret:
            print(f"{guess} is too high! Try again.")
        else:
            print(f"Spot on! You guessed {secret} in {attempts} attempts.")
            break


# Tool 3: Simple Calculator
# Performs basic arithmetic (+, -, *, /) on two numbers chosen by the user.
def simple_calculator():
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print(f"'{operator}' is not a supported operator. Use +, -, *, or /.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")


# Main Program Menu
# Welcomes the user and loops until they choose to quit.
def main():
    tasks = []
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n=== Personal Mini-Toolkit ===")
        print("1. To-Do List Manager")
        print("2. Number Guessing Game")
        print("3. Simple Calculator")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            todo_list_manager(tasks)
        elif choice == "2":
            number_guessing_game()
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            print("Thanks for using the Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' is not on the menu. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
