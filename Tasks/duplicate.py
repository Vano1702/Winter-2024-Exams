# Return an array of duplicates

def duplicate(value, count):
    if count <= 0:
        return []
    else:
        result = []
        for i in range(count):
            result.append(value)
        return result
