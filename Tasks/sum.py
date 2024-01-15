# Sum all numbers from an array

def numbers_sum(input_arr):
    sum_val = 0

    for element in input_arr:
        if type(element) == int:
            sum_val += element

    return sum_val
