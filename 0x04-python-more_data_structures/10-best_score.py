def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if not a_dictionary:
        return None

    max_key = None
    max_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value

    return max_key
