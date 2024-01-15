# Increment all numbers in dictionary

def inc_numbers(input_dict, *rest_variables):
    for key in input_dict:
        if type(input_dict[key]).__name__[0].upper() == 'I':
            input_dict[key] = input_dict[key] + 1

    return input_dict
