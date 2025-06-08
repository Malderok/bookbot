from stats import count_characters
from stats import display_count
from stats import count_book_word
from stats import get_book_text

def main():

    f = "/home/curbal/github.com/Malderok/bookbot/books/frankenstein.txt"

    conteo = count_characters(f)
    total_words = count_book_word(f)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for line in display_count(conteo):
        print(f"{line["char"]}: {line["num"]}")

    return


main()