def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_counter(text)
    print(f"{num_words} words found in the document")
    
    
## A function to count the words in the file that was read
def word_counter(text):
    words = text.split()
    return len(words)

## Read a file from the books directory and save it into a string variable
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()