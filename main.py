def count_words(str):
    return len(str.split())
def count_characters(str):
    char_counter = {}
    for c in file_contents.lower():
        if not c.isalpha():
            continue
        if c in char_counter:
            char_counter[c] += 1
        else:
            char_counter[c] = 1
    my_list = list(char_counter.items())
    my_list.sort(key=lambda e:e[0])
    return my_list

with open('./books/frankenstein.txt') as f:
    file_contents = f.read()
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count_words(file_contents)} words found in the document')
    print('')
    print(count_characters(file_contents))
    for arr in count_characters(file_contents):
        print(f"The '{arr[0]}' character was found {arr[1]} times")
    print('--- End report ---')
    