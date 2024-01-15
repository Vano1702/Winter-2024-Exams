# Return an array without duplicates

def distinct(data):
    uniques = []
    index = 0

    for element in data:
        if element in uniques:
            data[index] = None
        else:
            uniques.append(element)
        index += 1
    return list(filter(lambda x: isinstance(x, (int, float)), data))
