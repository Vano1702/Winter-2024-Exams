# Filter array by type name

def Filter(T, t):
    remove = []

    for C in T:
        x = T.index(C)
        if type(T[x]).__name__ != t:
            remove.insert(0, x)

    for x in remove:
        T.pop(x)

    return T
