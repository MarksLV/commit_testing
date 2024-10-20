# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main program
def main():
    print("Welcome to the Simple Calculator!")

    # Get user input
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        # Calculate the sum
        result = add_numbers(number1, number2)
        
        # Display the result
        print(f"The sum of {number1} and {number2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

# Run the calculator
if __name__ == "__main__":
    main()
