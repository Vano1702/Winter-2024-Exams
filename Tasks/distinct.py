# Return an array without duplicates

def distinct(data):
    A = []
    w = 0

    for a in data:
        if a in A:
            data[w] = None
        else:
            A.append(a)
        w += 1
    return list(filter(lambda x: isinstance(x, (int, float)), data))
