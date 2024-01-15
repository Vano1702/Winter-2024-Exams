# Return an array of duplicates

def duplicate(value, N):
    if N <= 0:
        return []
    else:
        res = []
        for i in range(N):
            res.append(value)
        return res
