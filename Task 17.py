"""
Task 19: Read and Process a Text File

Reads a text file and reports its line, word, and character counts.
Handles missing files gracefully and processes the file line by line.
"""

from pathlib import Path


def process_text_file(filename):
    """Return line, word, and character counts for a text file."""
    line_count = 0
    word_count = 0
    character_count = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_count += 1
                word_count += len(line.split())
                character_count += len(line)

        print(f"File: {filename}")
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters: {character_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except OSError as error:
        print(f"Error reading file: {error}")


def main():
    filename = input("Enter the path to a text file: ").strip()
    process_text_file(filename)


if __name__ == "__main__":
    main()
