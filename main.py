def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_counter(text)
    character_occurance = character_counter(text)
    print(f"{num_words} words found in the document")
    print(character_occurance)
    
    
## A function to count the words in the file that was read
def word_counter(text):
    words = text.split()
    return len(words)

## Read a file from the books directory and save it into a string variable
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
## A function to count how many times each character appears in the text
def character_counter(text):
    chars = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()