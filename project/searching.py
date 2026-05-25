def linear_search(target, data):
    for item in data:
        if item == target:
            return True
    return False