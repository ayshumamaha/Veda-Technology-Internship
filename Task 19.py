"""Task 19: CLI Quiz Application.
Run with: python task24_cli_quiz.py
A separate quiz_questions.json file is created automatically on first run.
"""
import json
import random
from pathlib import Path

QUESTION_FILE = Path(__file__).with_name("quiz_questions.json")

DEFAULT_QUESTIONS = [
    {"question": "Which language is this quiz application written in?",
     "options": {"A": "Java", "B": "Python", "C": "C++", "D": "Ruby"}, "answer": "B"},
    {"question": "Which keyword defines a function in Python?",
     "options": {"A": "function", "B": "func", "C": "def", "D": "define"}, "answer": "C"},
    {"question": "Which Python data type stores key-value pairs?",
     "options": {"A": "List", "B": "Tuple", "C": "Set", "D": "Dictionary"}, "answer": "D"},
    {"question": "Which symbol starts a single-line comment in Python?",
     "options": {"A": "#", "B": "//", "C": "/*", "D": "--"}, "answer": "A"},
    {"question": "What does len() return?",
     "options": {"A": "Data type", "B": "Number of items", "C": "Largest item", "D": "Memory size"}, "answer": "B"},
    {"question": "Which list method adds an item to the end?",
     "options": {"A": "add()", "B": "insert_end()", "C": "append()", "D": "push()"}, "answer": "C"},
    {"question": "Which loop is commonly used to iterate over a sequence?",
     "options": {"A": "for", "B": "switch", "C": "repeat-until", "D": "do-while"}, "answer": "A"},
    {"question": "Which function converts a string to an integer?",
     "options": {"A": "str()", "B": "float()", "C": "number()", "D": "int()"}, "answer": "D"},
    {"question": "What is the result of 3 ** 2 in Python?",
     "options": {"A": "6", "B": "9", "C": "8", "D": "5"}, "answer": "B"},
    {"question": "Which block is used to handle exceptions?",
     "options": {"A": "if/else", "B": "for/in", "C": "try/except", "D": "def/return"}, "answer": "C"}
]


def create_question_file():
    if not QUESTION_FILE.exists():
        with QUESTION_FILE.open("w", encoding="utf-8") as file:
            json.dump(DEFAULT_QUESTIONS, file, indent=4)
        print(f"Created question bank: {QUESTION_FILE.name}")


def load_questions():
    create_question_file()
    try:
        with QUESTION_FILE.open("r", encoding="utf-8") as file:
            questions = json.load(file)
        if not isinstance(questions, list) or not questions:
            raise ValueError("The question bank must be a non-empty list.")
        for item in questions:
            if (not isinstance(item, dict) or not item.get("question")
                    or not isinstance(item.get("options"), dict)
                    or item.get("answer") not in item.get("options", {})):
                raise ValueError("A question has an invalid format.")
        return questions
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Could not load question bank: {error}")
        return []


def ask_question(question, number, total):
    print(f"\nQuestion {number} of {total}")
    print(question["question"])
    for letter, text in question["options"].items():
        print(f"  {letter}. {text}")

    valid = {letter.upper() for letter in question["options"]}
    while True:
        answer = input("Your answer: ").strip().upper()
        if answer in valid:
            break
        print("Invalid choice. Enter one of the displayed option letters.")

    if answer == question["answer"].upper():
        print("Correct!")
        return True
    correct = question["answer"]
    print(f"Incorrect. Correct answer: {correct}. {question['options'][correct]}")
    return False


def run_quiz():
    questions = load_questions()
    if not questions:
        print("No valid questions are available. Quiz cannot start.")
        return

    random.shuffle(questions)
    score = 0
    total = len(questions)

    print("\n" + "=" * 40)
    print("       CLI QUIZ APPLICATION")
    print("=" * 40)
    print(f"There are {total} questions. Choose the correct option.")

    for number, question in enumerate(questions, start=1):
        if ask_question(question, number, total):
            score += 1

    percentage = score / total * 100
    print("\n" + "=" * 40)
    print("             FINAL RESULT")
    print("=" * 40)
    print(f"Total questions : {total}")
    print(f"Correct answers : {score}")
    print(f"Incorrect       : {total - score}")
    print(f"Final score     : {percentage:.1f}%")
    if percentage == 100:
        print("Excellent! Perfect score.")
    elif percentage >= 70:
        print("Great work!")
    elif percentage >= 40:
        print("Good effort. Keep practising!")
    else:
        print("Keep learning and try again!")
    print("=" * 40)


if __name__ == "__main__":
    run_quiz()
