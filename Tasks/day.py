# Get day number

DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def parse_day(day_string):
    for i in range(len(DAYS)):
        if day_string.startswith(DAYS[i].lower()):
            return i + 1
    return -1
