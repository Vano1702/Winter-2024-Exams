# Increment all numbers in dictionary

def inc_numbers(input_dict):
    result = dict(input_dict)
    for key, value in result.items():
        if type(value) == int:
            result[key] += 1

    return result
