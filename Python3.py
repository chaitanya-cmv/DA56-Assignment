# ==================================================
# PYTHON ASSIGNMENT 3
# WHILE LOOP, FOR LOOP AND FUNCTION
# ==================================================


# ==================================================
# 1. NUMBER GUESSING GAME - WHILE LOOP
# ==================================================

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Maximum number of attempts
attempts = 3

print("Welcome to the Number Guessing Game!")

while attempts > 0:

    guess = int(input("Guess the number (between 1 and 10): "))

    # Check if the guess is out of range
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    # Check if the guess is too high
    elif guess > secret_number:
        print("Too high. Try again.")

    # Check if the guess is too low
    else:
        print("Too low. Try again.")

    # Reduce attempts
    attempts -= 1

    print("Attempts remaining:", attempts)

else:
    print("Better luck next time!")
    print("The secret number was:", secret_number)


# ==================================================
# 2. MULTIPLICATION TABLE - FOR LOOP
# ==================================================

number = int(
    input("\nEnter the number for which you want the multiplication table: ")
)

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


# ==================================================
# 3. BMI CALCULATOR - FUNCTION
# ==================================================

# Define the function
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


# Ask the user for weight and height
weight = float(input("\nEnter your weight in kg: "))
height = float(input("Enter your height in meters: "))


# Call the function
bmi_result = calculate_bmi(weight, height)


# Display the BMI
print("Your BMI is:", round(bmi_result, 2))