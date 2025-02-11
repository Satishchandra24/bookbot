def output_text(path_to_file) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents) -> int:
    contents_list = file_contents.split()
    return len(contents_list)

def count_characters(file_contents) ->dict:
    char_count= {}
    for char in file_contents:
        if char.lower() not in char_count:
            char_count[char.lower()] = 1
        else:
            char_count[char.lower()] += 1
    return char_count
def print_report(path_to_file,word_count,char_count) ->None:
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print("")
    for chars in char_count:
        if chars.isalpha() == True:
            print(f"The '{chars}' character was found {char_count[chars]} times")
    print("--- End report ---")

def main(path_to_file):
    file_contents = output_text(path_to_file)
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    return file_contents, word_count , char_count
    
        
        
path_to_file = "books/frankenstein.txt"
file_contents, word_count, char_count = main(path_to_file)
print_report(path_to_file,word_count,char_count)