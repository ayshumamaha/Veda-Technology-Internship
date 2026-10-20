# Word and Character Counter
# VEDA Technology - Python Programming Track, Level 1, Task 11

import re

def analyze_text(text):
    """Return character, word, sentence, and space counts for the given text."""
    characters = len(text)
    words = len(text.split())
    spaces = text.count(" ")

    # Count sentences ending in ., !, or ?, while avoiding empty matches.
    sentences = len(re.findall(r"[.!?]+(?=\s|$)", text.strip())) if text.strip() else 0

    return characters, words, sentences, spaces


def main():
    print("=== Word and Character Counter ===")
    print("Enter a paragraph (press Enter on an empty line to finish):")

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        lines.append(line)

    paragraph = "\n".join(lines)
    characters, words, sentences, spaces = analyze_text(paragraph)

    print("\n--- Text Statistics ---")
    print(f"Characters (including spaces and line breaks): {characters}")
    print(f"Words: {words}")
    print(f"Sentences: {sentences}")
    print(f"Spaces: {spaces}")


if __name__ == "__main__":
    main()
