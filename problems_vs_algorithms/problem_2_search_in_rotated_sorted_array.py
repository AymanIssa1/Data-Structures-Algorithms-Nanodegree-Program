def rotated_array_search(input_list, number):
    front_index = 0
    back_index = len(input_list) - 1

    while front_index <= back_index:
        mid_index = (back_index + front_index) // 2
        # print("front_index = " + str(front_index) + " back_index = " + str(back_index) + " mid_index = " + str(mid_index))
        if input_list[front_index] == number:
            return front_index
        elif input_list[back_index] == number:
            return back_index
        elif input_list[mid_index] == number:
            return mid_index
        elif input_list[mid_index] >= input_list[front_index]:
            if input_list[front_index] <= number < input_list[mid_index]:
                back_index = mid_index - 1
            else:
                front_index = mid_index + 1
        elif input_list[mid_index] < input_list[back_index]:
            if input_list[back_index] > number >= input_list[mid_index]:
                front_index = mid_index - 1
            else:
                back_index = mid_index + 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])
test_function([[], None])
test_function([[0], -1])
test_function([[-1], -1])
test_function([[-1, 0, 1, 2, -9, -8, -7, -6, -5, -4, -3, -2], -1])
test_function([[1, 2, 3, 4, 5, 6, 7, 9, 0], 9])
