# Return an array without duplicates

def distinct(data):
    uniques = []

    for element in data:
        if element not in uniques:
            uniques.append(element)

    return uniques