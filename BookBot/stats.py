def count_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    text = text.lower()
    character_counts = {}
    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def sort_on(item):
    return item[1]

def chars_dict_to_sorted_list(chars_dict):
    chars_list = []
    for char in chars_dict:
        chars_list.append((char, chars_dict[char]))
    return sorted(chars_list, reverse=True, key=sort_on)