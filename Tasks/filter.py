# Filter array by type name

def filter(input_arr, type_string):
    remove = []

    for element in input_arr:
        el_index = input_arr.index(element)
        if not isinstance(input_arr[el_index], eval(type_string)):
            remove.insert(0, el_index)

    for element in remove:
        input_arr.pop(element)

    return input_arr
