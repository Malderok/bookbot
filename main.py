from stats import count_characters
from stats import display_count
from stats import count_book_word
from stats import get_book_text
import sys

def main():

    if len(sys.argv) != 2:

        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    conteo = count_characters(sys.argv[1])
    total_words = count_book_word(sys.argv[1])


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for line in display_count(conteo):
        print(f"{line["char"]}: {line["num"]}")

    return


main()