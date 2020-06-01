def get_min_max(ints):
    if len(ints) == 0:
        return None
    if len(ints) == 1:
        return (ints[0])

    min_value = float('inf')
    max_value = float('-inf')
    for i in ints:
        min_value = min(min_value, i)
        max_value = max(max_value, i)

    return (min_value, max_value)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((0) == get_min_max([0])) else "Fail")
print("Pass" if (None == get_min_max([])) else "Fail")
print("Pass" if ((-6, -2) == get_min_max([-2, -3, -4, -6])) else "Fail")
