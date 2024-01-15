# Return an array of duplicates

def duplicate(value, count):
    if count <= 0:
        return []
    else:
        result = [value for i in range(count)]
        return result
