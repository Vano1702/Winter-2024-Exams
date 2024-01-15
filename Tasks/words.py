# Count words in a string

def words(input_str):
    words_count = 0
    flag = False

    for char in input_str:
        if char == ' ':
            flag = False
        elif not flag:
            flag = True
            words_count += 1

    return words_count
