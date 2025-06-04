import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("🔢 Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("⚠️ Please guess a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try again.\n")
            elif guess > secret_number:
                print("📈 Too high! Try again.\n")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.\n")

if __name__ == "__main__":
    number_guessing_game()
