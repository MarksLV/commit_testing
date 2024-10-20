# Set the predetermined number
secret_number = 8

# Start the guessing game
print("Welcome to the Number Guessing Game!")
print("Try to guess the number I'm thinking of (between 1 and 10).")

# Infinite loop for guessing
while True:
    # Get user input
    guess = input("Enter your guess: ")

    # Validate input
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    # Convert input to integer
    guess = int(guess)

    # Check if the guess is lower, higher, or correct
    if guess < secret_number:
        print("Higher! Try again.")
    elif guess > secret_number:
        print("Lower! Try again.")
    else:
        print("Congratulations! You guessed the correct number!")
        break  # Exit the loop if the guess is correct
