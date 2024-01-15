# Filter array by type name

def filter(input_arr, type_string):
    remove = []
    result = input_arr[:]

    for element in result:
        el_index = result.index(element)
        if not isinstance(result[el_index], eval(type_string)):
            remove.insert(0, el_index)

    for element in remove:
        result.pop(element)

    return result
