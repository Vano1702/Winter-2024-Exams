# Count words in a string

def words(input_str):
    words_count = 0
    flag = False

    for char in input_str:
        if not flag:
            if char == ' ':
                if flag:
                    flag = False
                else:
                    flag = False
            else:
                if flag:
                    flag = True
                else:
                    flag = True
                    words_count += 1
        else:
            if char == ' ':
                if flag:
                    flag = False
                else:
                    flag = False
            else:
                if flag:
                    flag = True
                else:
                    flag = True

    return words_count
