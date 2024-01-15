# Sum all number values in dictionary

def count(obj):
    sum_val = 0
    keys = obj.keys()

    for key in keys:
        value = obj[key]
        if isinstance(value, int) or isinstance(value, float):
            sum_val += value

    return sum_val
