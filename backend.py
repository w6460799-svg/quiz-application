# Quiz Application - Backend Logic
# Extracted from main.py for reuse with GUI frontend
# Uses built-in Python modules only


def get_questions():
    """Return all quiz questions with options and answers."""
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


def validate_answer(answer):
    """Validate if answer is one of A, B, C, or D."""
    return answer.strip().upper() in ["A", "B", "C", "D"]


def check_answer(user_answer, correct_answer):
    """Check if user answer matches correct answer."""
    return user_answer.strip().upper() == correct_answer


def calculate_score(answers, questions):
    """Calculate score based on user answers."""
    score = 0
    for user_answer, question_data in zip(answers, questions):
        if check_answer(user_answer, question_data["answer"]):
            score += 1
    return score


def get_result_message(score, total):
    """Get motivational message based on score."""
    if score == total:
        return "Excellent! You got a perfect score!"
    elif score >= 7:
        return "Great job! You did very well."
    elif score >= 4:
        return "Good effort! You passed."
    else:
        return "Keep practicing! You can do better next time."


def get_percentage(score, total):
    """Calculate percentage score."""
    if total == 0:
        return 0
    return round((score / total) * 100, 1)
