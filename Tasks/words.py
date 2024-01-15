# Count words in a string

def words(input_str):
    words_count = 0
    flag = False

    for char in input_str:
        if not flag:
            if char == ' ':
                flag = False
            else:
                flag = True
                words_count += 1
        else:
            if char == ' ':
                flag = False

    return words_count
