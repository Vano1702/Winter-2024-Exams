# Merge two dictionaries

def merge_two_objects(dict_1, dict_2):
    dict_3 = {}

    for key in dict_1:
        dict_3[key] = dict_1[key]

    for key in dict_2:
        dict_3[key] = dict_2[key]

    return dict_3
