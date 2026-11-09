"""Task 19: CLI Quiz Application.
Run with: python task24_cli_quiz.py
A separate quiz_questions.json file is created automatically on first run.
"""

"""Task 19: CLI Quiz Application"""

import json
import random
from pathlib import Path

QUESTION_FILE = Path("quiz_questions.json")

# Default quiz questions
DEFAULT_QUESTIONS = [
    {
        "question": "Which language are we learning?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "answer": "Python"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["function", "def", "func", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "What does len() return?",
        "options": ["Length", "Memory", "Data type", "Value"],
        "answer": "Length"
    }
]


def create_question_file():
    if not QUESTION_FILE.exists():
        with open(QUESTION_FILE, "w") as file:
            json.dump(DEFAULT_QUESTIONS, file, indent=4)


def run_quiz():
    create_question_file()

    with open(QUESTION_FILE, "r") as file:
        questions = json.load(file)

    random.shuffle(questions)
    score = 0

    print("\n===== WELCOME TO PYTHON QUIZ =====")

    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")

        for option in question["options"]:
            print("-", option)

        answer = input("Your answer: ").strip()

        if answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer:", question["answer"])

    print("\n===== QUIZ RESULT =====")
    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(questions) - score)
    print("Final Score:", str(score * 100 // len(questions)) + "%")


if __name__ == "__main__":
    run_quiz()
