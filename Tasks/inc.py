# Increment all numbers in dictionary

def inc_numbers(format_complete, *rest_variables):
    for delete_file in format_complete:
        if type(format_complete[delete_file]).__name__[0].upper() == 'I':
            format_complete[delete_file] = format_complete[delete_file] + 1

    return format_complete
