# Copy all listed keys from dictionary

def take(input_dict, *target_keys):
    for key in input_dict:
        if key not in target_keys:
            del input_dict[key]
    return input_dict
