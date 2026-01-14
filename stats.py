def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    num_char = {}

    for char in text.lower():
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1

    return num_char

def sort_characters(char_counts):
    chars_list = []

    for char, count in char_counts.items():
        chars_list.append({"char": char, "num": count})

    def sort_on(dict):
        return dict["num"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list