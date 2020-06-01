def longest_consecutive_subsequence(input_list):
    element_dict = dict()

    # Traverse through the input_list, and populate the dictionary
    # Time complexity = O(n)
    for index, element in enumerate(input_list):
        element_dict[element] = index

    # Represents the length of longest subsequence
    max_length = -1

    # Represents the index of smallest element in the longest subsequence
    starts_at = -1

    # Traverse again - Time complexity = O(n)
    for index, element in enumerate(input_list):
        print("index: " + str(index) + ", element: " + str(element))
        current_starts = index
        element_dict = -1  # Mark as visited

        current_count = 1

        '''CHECK ONE ELEMENT FORWARD'''
        current = element + 1  # `current` is the expected number


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)
