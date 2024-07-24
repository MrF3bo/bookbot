def main():

    ## Function calls
    book_path = "books/frankenstein.txt"                            ## path to the file we want to read
    text = get_book_text(book_path)                                 ## a variable to store the contents of the file in
    num_words = word_counter(text)                                  ## count words using word_counter function and store it in a variable
    character_occurance = character_counter(text)                   ## count characters using the character_occurance function and store it in a variable
    list_of_dict = convert_to_list(character_occurance)             ## convert the dictionary of characters to a list and store it in a variable
    sorted = sort_char_list(list_of_dict)

    ## Print statements
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for list_item in sorted:
        print(f"The '{list_item['char']}' character was found {list_item['count']} times")
    print("--- End report ---")
    
    
## A function to count the words in the file that was read
def word_counter(text):
    words = text.split()
    return len(words)

## A function to count how many times each character appears in the text
def character_counter(text):
    chars = {}
    for letter in text:
        if letter.isalpha():
            lowered = letter.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

## A function to convert the dictionary above to a list
def convert_to_list(dict):
    char_list = []
    for char, count in dict.items():
        char_list.append({"char": char, "count": count})
    return char_list

def sort_char_list(char_list):
    def sort_on(dict_item):
        return dict_item["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

## A function to read a file from the books directory and save it into a string variable
def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()