# Count words in a string

def Words(s):
    number_of_words_in_s = 0
    flag = False

    for c in s:
        if not flag:
            if c == ' ':
                if flag:
                    flag = False
                else:
                    flag = False
            else:
                if flag:
                    flag = True
                else:
                    flag = True
                    number_of_words_in_s += 1
        else:
            if c == ' ':
                if flag:
                    flag = False
                else:
                    flag = False
            else:
                if flag:
                    flag = True
                else:
                    flag = True

    return number_of_words_in_s
