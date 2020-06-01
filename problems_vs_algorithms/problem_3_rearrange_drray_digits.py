def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if input_list is None or len(input_list) <= 1:
        return [-1, -1]

    sorted_list = mergesort(input_list)
    value1 = ''
    value2 = ''

    for element in sorted_list:
        if element % 2 == 1:
            value1 += str(element)
        else:
            value2 += str(element)

    return [int(value1), int(value2)]


def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[: mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    left_index = 0
    right_index = 0

    result = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return result


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[], [-1, -1]])
test_function([None, [-1, -1]])
test_function([[9, 8, 7, 6, 5, 4], [975, 864]])
test_function([[9, 8, 7, 1, 5, 4], [9751, 84]])
