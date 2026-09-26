import sys
from stats import count_words, count_character, chars_dict_to_sorted_list

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    number_of_words = count_words(text)
    character_counts = count_character(text)
    sorted_chars = chars_dict_to_sorted_list(character_counts)
    print_report(path_to_file, number_of_words, sorted_chars)


if __name__ == '__main__':
    main()
