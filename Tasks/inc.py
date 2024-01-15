# Increment all numbers in dictionary

def inc_numbers(input_dict):
    for key in input_dict:
        if type(input_dict[key]) == int:
            input_dict[key] = input_dict[key] + 1

    return input_dict
