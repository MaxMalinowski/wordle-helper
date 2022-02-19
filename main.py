import re


def load_words():
    with open('words_extracted.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

# def extract_length_five_words(english_words):
#     extracted_words = []
#     for word in english_words:
#         if len(word) == 5:
#             extracted_words.append(word)
#     extracted_words.sort()
#     save_extracted_words(extracted_words)

# def save_extracted_words(extracted_words):
#     f = open("words_extracted.txt", "w")
#     for word in extracted_words:
#         f.write(word + '\n')
#     f.close()

def all_exist(string, list):
    for e in list:
        if e not in string:
            return False
    return True

def filter(filter_string, possible_string, known_string, word_list):
    filter_string = filter_string.replace('-', '[' + possible_string + ']')
    
    current_list = []
    for word in word_list:
        if re.search(filter_string, word) != None:
            if all_exist(word, known_string):
                current_list.append(word)

    return current_list

if __name__ == '__main__':
    word_list = load_words()
    print('Enter what you know about the word.')
    filter_string = input('Enter the word-structure: ')
    possible_string = input('Enter the chars that might be in the word: ')
    known_string = input('Enter the chars you know must be present: ')
    filtered_list = filter(filter_string, possible_string, known_string, word_list)
    print("\n".join(filtered_list))