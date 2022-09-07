def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0 or not all(isinstance(x, int) for x in ints):
        return -1,-1
    minimum_number = ints[0]
    maximum_number = ints[0]
    for num in ints:
        if num > maximum_number:
            maximum_number = num
        elif num < minimum_number:
            minimum_number = num

    return minimum_number, maximum_number

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

empty = []

print ("Pass" if ((-1,-1) == get_min_max(empty)) else "Fail")

invalid = [""]

print ("Pass" if ((-1,-1) == get_min_max(invalid)) else "Fail")

string_empty = ""

print ("Pass" if ((-1,-1) == get_min_max(string_empty)) else "Fail")