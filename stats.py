def count_book_word(file_path):
    
    with open(file_path) as f:

        file_contents = f.read()
        words_string = file_contents.split()
        print(f"{len(words_string)} words found in the document")


def get_book_text(file_path):
    
    with open(file_path) as f:

        file_contents = f.read()
        print(file_contents)