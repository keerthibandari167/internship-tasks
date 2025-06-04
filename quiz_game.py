# Python Quiz Game

def ask_question(question, options, correct_option):
    print("\n" + question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    try:
        answer = int(input("Enter your answer (1-4): "))
        if options[answer - 1].lower() == correct_option.lower():
            print("Correct!")
            return 1
        else:
            print(f"Wrong! Correct answer was: {correct_option}")
            return 0
    except (ValueError, IndexError):
        print("Invalid input. No marks awarded for this question.")
        return 0

def run_quiz():
    print("Welcome to the Python Quiz Game!")
    score = 0
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Which language is used to write Python?",
            "options": ["C++", "Java", "Python", "English"],
            "answer": "Python"
        },
        {
            "question": "What does CPU stand for?",
            "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Panel Unit"],
            "answer": "Central Processing Unit"
        },
        {
            "question": "What is 5 * 6?",
            "options": ["11", "30", "56", "65"],
            "answer": "30"
        },
    ]

    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer"])

    print(f"\nQuiz finished! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()
