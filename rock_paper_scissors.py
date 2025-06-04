import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
        choice = input("Choose [rock, paper, scissors]: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please type rock, paper, or scissors.")

def decide_winner(user, computer):
    if user == computer:
        return 'draw'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_wins = 0
    computer_wins = 0
    rounds = 0

    print("🎮 Welcome to Rock, Paper, Scissors Game!")
    print("Type 'exit' anytime to stop playing.\n")

    while True:
        user_choice = input("Your choice (rock/paper/scissors or 'exit'): ").lower()
        if user_choice == 'exit':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("⚠️ Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"🧠 Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == 'user':
            print("✅ You win this round!\n")
            user_wins += 1
        elif result == 'computer':
            print("❌ Computer wins this round!\n")
            computer_wins += 1
        else:
            print("🤝 It's a draw!\n")

        rounds += 1

    print("\n📊 Final Results:")
    print(f"Rounds played: {rounds}")
    print(f"Your wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")

    if user_wins > computer_wins:
        print("🏆 You are the overall winner!")
    elif computer_wins > user_wins:
        print("💻 Computer is the overall winner!")
    else:
        print("🔁 It's a tie overall!")

if __name__ == "__main__":
    play_game()
