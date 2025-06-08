def count_book_word(file_path):
    
    with open(file_path) as f:

        file_contents = f.read()
        words_string = file_contents.split()
        #print(f"{len(words_string)} words found in the document")
        return len(words_string)


def get_book_text(file_path):
    
    with open(file_path) as f:

        file_contents = file_path.read()
        print(file_contents)



def count_characters(file_path):
    character_count = {}

    with open(file_path) as f:

        file_contents = f.read()

        file_contents = file_contents.lower()

        for character in file_contents:
            

            if character in character_count:

                character_count[character] += 1

            else:

                character_count[character] = 1
                
    return character_count

def sort_on(dict):
    return dict["num"]


def display_count(character_count):

    dictionaty_list = []


    for character in character_count:


        if character.isalpha():

            dictionaty_list.append({"char": character , "num" : character_count[character]})



    dictionaty_list.sort(reverse=True , key=sort_on )


    return dictionaty_list