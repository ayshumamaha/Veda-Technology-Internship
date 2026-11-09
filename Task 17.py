"""
Task 17: Read and Process a Text File

Reads a text file and reports its line, word, and character counts.
Handles missing files gracefully and processes the file line by line.
"""

from pathlib import Path

def process_text_file(filename):
    line_count = 0
    word_count = 0
    character_count = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_count += 1
                word_count += len(line.split())
                character_count += len(line)

        print("\n--- File Details ---")
        print("File:", filename)
        print("Lines:", line_count)
        print("Words:", word_count)
        print("Characters:", character_count)

    except OSError as error:
        print("Error:", error)


def main():
    filename = "sample.txt"

    # Automatically create a sample text file
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Python is easy to learn.\n")
        file.write("I am learning file handling.\n")
        file.write("This is Task 17 of my internship.")

    print("Sample text file created successfully!")

    process_text_file(filename)


if __name__ == "__main__":
    main()
