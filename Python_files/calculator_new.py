# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract_numbers(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply_numbers(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 / num2

# Main program
def main():
    print("Welcome to the Simple Calculator!")

    while True:
        # Get user input
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue  # Restart the loop for valid input

        # Choose operation
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            result = add_numbers(number1, number2)
            operation = "addition"
        elif choice == '2':
            result = subtract_numbers(number1, number2)
            operation = "subtraction"
        elif choice == '3':
            result = multiply_numbers(number1, number2)
            operation = "multiplication"
        elif choice == '4':
            result = divide_numbers(number1, number2)
            operation = "division"
        elif choice == '5':
            print("Thank you for using the calculator! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue  # Restart the loop for valid operation

        # Display the result
        print(f"\nThe result of {operation} between {number1} and {number2} is: {result}\n")

# Run the calculator
if __name__ == "__main__":
    main()
