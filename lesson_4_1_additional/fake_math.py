import numbers


def divide(first, second):
    if isinstance(first, numbers.Number) and isinstance(second, numbers.Number):
        if second == 0:
            return "Error"
        else:
            return first/second
    else:
        return "Error"