def power_of_2(n):
    if n <= 0:
        return 1
    return 2 * power_of_2(n - 1)


print(power_of_2(5))


def sum_integers(n):
    if n <= 1:
        return n

    return n + sum_integers(n - 1)


print(sum_integers(3))


def sum_array(array):
    # Base case
    if len(array) == 1:
        return array[0]

    return array[0] + sum_array(array[1:])


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print("Pass" if (1 == factorial(0)) else "Fail")
print("Pass" if (1 == factorial(1)) else "Fail")
print("Pass" if (120 == factorial(5)) else "Fail")


def reverse_string(input):
    if len(input) <= 1:
        return input

    first_char = input[0]
    reversed_string = reverse_string(input[1:])

    return reversed_string + first_char


print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
print(reverse_string("abc"))


def is_palindrome(input):
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]

        sub_input = input[1:-1]

        return (first_char == last_char) and is_palindrome(sub_input)


print("Pass" if (is_palindrome("")) else "Fail")
print("Pass" if (is_palindrome("a")) else "Fail")
print("Pass" if (is_palindrome("madam")) else "Fail")
print("Pass" if (is_palindrome("abba")) else "Fail")
print("Pass" if not (is_palindrome("Udacity")) else "Fail")


def add_one(arr):
    print(arr)
    if arr == [9]:
        print("if arr == [9]")
        return [1, 0]

    if arr[-1] < 9:
        print("simplist case")
        arr[-1] += 1

    else:
        print("else case")
        arr = add_one(arr[:-1]) + [0]

    return arr


# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    print('output: ' + str(output))
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

# print('# Test Case 1')
# arr = [0]
# solution = [1]
# test_case = [arr, solution]
# test_function(test_case)

# print('# Test Case 2')
# arr = [1, 2, 3]
# solution = [1, 2, 4]
# test_case = [arr, solution]
# test_function(test_case)

print('# Test Case 3')
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)