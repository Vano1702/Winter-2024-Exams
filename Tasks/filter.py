# Filter array by type name

def filter(input_arr, type_string):
    result = input_arr[:]

    for element in reversed(result):
        if not isinstance(element, eval(type_string)):
            result.remove(element)


    return result
