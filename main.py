import sys 
from stats import get_num_words, get_character_occurrences, sort_occurrences 

def get_book_text(file_path):
    with open(file_path) as file:
        return(file.read())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    occurrences = get_character_occurrences(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sort_occurrences(occurrences):
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
    
main()