
import sys

from stats import get_num_words, get_num_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # CH2L3 Reads file
    # book_text = get_book_text("books/frankenstein.txt")
    # print(book_text)

    # CH2L4 Counts Words
    # num_words = get_num_words(book_text)
    # print(f"Found {num_words} total words")

    # CH2L6 Count Characters
    # num_char = get_num_characters(book_text)
    # print(num_char)

    # CH3L1
    # path = "books/frankenstein.txt"
    # book_text = get_book_text(path)
    # word_count = get_num_words(book_text)
    # char_counts = get_num_characters(book_text)
    # sorted_chars = sort_characters(char_counts)

    # print("============ BOOKBOT ============")
    # print(f"Analyzing book found at {path}...")
    # print("----------- Word Count ----------")
    # print(f"Found {word_count} total words")
    # print("--------- Character Count -------")

    # for item in sorted_chars:
    #     char = item["char"]
    #     count = item["num"]

    #     if not char.isalpha():
    #        continue

    #     print(f"{char}: {count}")

    # print("============= END ===============")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    char_counts = get_num_characters(book_text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        count = item["num"]

        if not char.isalpha():
            continue

        print(f"{char}: {count}")

    print("============= END ===============")

main()