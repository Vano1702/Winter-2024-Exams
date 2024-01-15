# Increment all numbers in dictionary

def inc_numbers(input_dict):
    result = dict(input_dict)
    for key in result:
        if type(result[key]) == int:
            result[key] = result[key] + 1

    return result
