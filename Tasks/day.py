# Get day number

DAYS = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

def parse_day(day_string):
    for i, day in enumerate(DAYS, start=1):
        if day_string.startswith(day):
            return i
    return -1
