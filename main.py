from stats import dict_list 
from stats import word_count
from stats import char_count
def get_book_text(path):
    current_book =""
    with open(path) as f:
        current_book = f.read()
    return current_book

def sort_on(dict):
    return dict["num"]


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_num = word_count(book_text)
    sorted = dict_list(char_count(get_book_text(book_path)))
    sorted.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")
    for dic in sorted:
        if dic['char'].isalpha():
            print(f"{dic['char']}: {dic['num']}")
    print("============= END ===============")
main()
