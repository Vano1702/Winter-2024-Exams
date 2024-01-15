# Get day number

DAYS = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

def parse_day(day_string):
    for i in range(len(DAYS)):
        if day_string.startswith(DAYS[i]):
            return i + 1
    return -1
