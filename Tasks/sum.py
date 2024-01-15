# Sum all numbers from an array

def numbers_sum(input_arr):
    sum_array = [0]
    k = 5

    for i in input_arr:
        t = type(i).__name__
        if t == 'int':
            if len(sum_array) > 0:
                new_sum = sum_array[-1] + i
                sum_array.append(new_sum)

    return sum_array[-1]
