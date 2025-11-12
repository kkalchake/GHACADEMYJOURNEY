import sys
import re
import logging
from collections import Counter

# Configure logging to stderr
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(message)s')

TOKEN_REGEX = r"(?:[A-Za-z]\.){2,}[A-Za-z]?\.?|\d+\.\d+|(?:[#@]?\w+(?:[-']\w+)*)|[A-Za-z]+"

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        sys.exit(1)

def tokenize(text):
    tokens = re.findall(TOKEN_REGEX, text)
    return [token.lower() for token in tokens]

def count_words(tokens):
    return Counter(tokens)

def word_count_main(text):
    tokens = tokenize(text)
    if not tokens:
        print("The text does not have any words.")
        return

    word_counts = count_words(tokens)
    total_words = sum(word_counts.values())
    unique_words = len(word_counts)

    logging.info(f"Tokenized Words: {tokens}")
    logging.info(f"Word Count: {len(tokens)}")

    print(f"Total Words: {total_words}")
    print(f"Unique Words: {unique_words}")
    print("\nTop 5 most repeated unique words and their occurrences:")
    print("-" * 45)
    for word, count in word_counts.most_common(5):
        print(f"{word:<20} {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = read_file(file_path)
    word_count_main(text)

if __name__ == '__main__':
    main()
