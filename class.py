import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the correct number. Let's start!")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 40)
    attempts = 10

    for attempt in range(1, attempts + 1):
        try:
            # Get the player's guess
            guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))

            # Check the guess
            if guess < target_number:
                print("Too low! Try a higher number.")
            elif guess > target_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempt} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

    else:
        # If the player uses all attempts without guessing correctly
        print(f"Sorry, you've used all your attempts. The number was {target_number}.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
