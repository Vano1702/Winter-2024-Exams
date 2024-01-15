# Copy all listed keys from dictionary

def take(input_dict, *target_keys):
    result = dict(input_dict)
    for key in input_dict:
        if key not in target_keys:
            del result[key]
    return result
