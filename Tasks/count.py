# Sum all number values in dictionary

def count(obj):
    sum_val = 0

    for key, value in obj.items():
        if isinstance(value, int):
            sum_val += value

    return sum_val
