# Quiz Application - Terminal Version
# Backend only in Python
# Uses built-in Python modules only

import sys


def print_welcome_message():
    print("=" * 50)
    print("Welcome to the Quiz App!")
    print("Answer 10 multiple-choice questions.")
    print("Type the letter of your answer: A, B, C, or D")
    print("=" * 50)


def get_questions():
    # Each question is a dictionary:
    # - question: question text
    # - options: list of 4 choices
    # - answer: correct option letter
    questions = [
        {
            "question": "What does CPU stand for?",
            "options": [
                "A. Central Processing Unit",
                "B. Computer Personal Unit",
                "C. Central Program Utility",
                "D. Control Processing Unit"
            ],
            "answer": "A"
        },
        {
            "question": "Which language is used to create Python programs?",
            "options": [
                "A. Java",
                "B. Python",
                "C. C++",
                "D. HTML"
            ],
            "answer": "B"
        },
        {
            "question": "Which of these is a valid Python data type?",
            "options": [
                "A. Integer",
                "B. Cardboard",
                "C. Floaty",
                "D. Boolean"
            ],
            "answer": "A"
        },
        {
            "question": "What symbol is used for comments in Python?",
            "options": [
                "A. //",
                "B. #",
                "C. /* */",
                "D. --"
            ],
            "answer": "B"
        },
        {
            "question": "Which function is used to print output in Python?",
            "options": [
                "A. print()",
                "B. echo()",
                "C. display()",
                "D. show()"
            ],
            "answer": "A"
        },
        {
            "question": "Which of the following is used to store a collection of items in Python?",
            "options": [
                "A. Function",
                "B. Loop",
                "C. List",
                "D. Variable"
            ],
            "answer": "C"
        },
        {
            "question": "What is the result of 10 % 3 in Python?",
            "options": [
                "A. 3",
                "B. 1",
                "C. 0",
                "D. 10"
            ],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "A. func",
                "B. define",
                "C. def",
                "D. function"
            ],
            "answer": "C"
        },
        {
            "question": "Which of these is used to check a condition in Python?",
            "options": [
                "A. loop",
                "B. if",
                "C. print",
                "D. else"
            ],
            "answer": "B"
        },
        {
            "question": "What does 'len()' do in Python?",
            "options": [
                "A. Deletes an item",
                "B. Converts a value",
                "C. Finds the length of a string or list",
                "D. Sorts numbers"
            ],
            "answer": "C"
        }
    ]
    return questions


def ask_question(question_data):
    print("\n" + "-" * 50)
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    print("-" * 50)

    while True:
        answer = input("Your answer (A, B, C, or D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid input! Please enter only A, B, C, or D.")


def run_quiz():
    questions = get_questions()
    score = 0

    print_welcome_message()

    for index, question_data in enumerate(questions, start=1):
        user_answer = ask_question(question_data)
        correct_answer = question_data["answer"]

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
            print(f"Your answer was {user_answer}.")

    print("\n" + "=" * 50)
    print("Quiz Complete!")
    print(f"Your final score is: {score}/{len(questions)}")
    print("=" * 50)

    # Show correct answers
    print("\nCorrect answers:")
    for index, question_data in enumerate(questions, start=1):
        print(f"{index}. {question_data['answer']}")

    # Final result summary
    if score == len(questions):
        print("\nExcellent! You got a perfect score!")
    elif score >= 7:
        print("\nGreat job! You did very well.")
    elif score >= 4:
        print("\nGood effort! You passed.")
    else:
        print("\nKeep practicing! You can do better next time.")


def main():
    while True:
        run_quiz()

        while True:
            restart = input("\nWould you like to restart the quiz? (yes/no): ").strip().lower()
            if restart in ["yes", "y"]:
                print("\nRestarting the quiz...\n")
                break
            elif restart in ["no", "n"]:
                print("Thank you for playing!")
                sys.exit(0)
            else:
                print("Invalid input! Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
