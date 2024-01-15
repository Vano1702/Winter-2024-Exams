# Sum all numbers from an array

def k(s=lambda: None):
    sum_array = [0]
    k = 5

    for i in s:
        t = type(i).__name__
        if t == 'int':
            if len(sum_array) > 0:
                new_sum = sum_array[-1] + i
                sum_array.append(new_sum)

    return sum_array[-1]
