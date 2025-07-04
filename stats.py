def get_num_words(book_text):
    return len(book_text.split())

def get_character_occurrences(book_text):
    occurrences = {}
    for char in book_text:
        key = char.lower()
        num = 1
        if key in occurrences:
            occurrences[key] += num
        else:
            occurrences[key] = num
    return occurrences
    
def sort_occurrences(occurrences):
    char_list = []
    for char in occurrences:
        if char.isalpha(): 
            char_list.append({"char": char, "num": occurrences[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
def sort_on(char_dict):
    return char_dict["num"]
