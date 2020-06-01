def add_one(arr):
    size = len(arr) - 1
    num = 0

    for i in range(len(arr)):
        print(i)
        num += arr[i] * pow(10, size)
        size -= 1

    num += 1
    new_arr = []

    for i in range(len(str(num))):
        digit = num % 10
        num = int(num / 10)
        print("digit: " + str(digit) + ", " + "num: " + str(num))
        new_arr.insert(0, digit)

    return new_arr


print(add_one([9, 9, 9, 9]))


def duplicate_number(arr):
    current_sum = 0
    expected_sum = 0

    for num in arr:
        current_sum += num

    for i in range(len(arr) - 1):
        expected_sum += i

    print("current_sum: " + str(current_sum))
    print("expected_sum: " + str(expected_sum))

    return current_sum - expected_sum


print(duplicate_number([0, 2, 3, 1, 4, 5, 5]))


def max_sum_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for element in arr[1:]:
        print('current_sum(current_sum + element: ' + str(current_sum + element) + ", element: " + str(
            element) + '): ' + str(max(current_sum + element, element)))
        current_sum = max(current_sum + element, element)

        print('max_sum(current_sum: ' + str(current_sum) + ", max_sum: " + str(max_sum) + '): ' + str(
            max(current_sum, max_sum)))
        max_sum = max(current_sum, max_sum)

        print("--------------------")

    return max_sum


print(max_sum_subarray([1, 2, 3, -4, 6]))
print(max_sum_subarray([-12, 15, -13, 14, -1, 2, 1, -5, 4]))


def nth_row_pascal(n):
    pascal = []
    pascal.append([1])
    pascal.append([1, 1])

    for i in range(2, n + 1, 1):
        previous_array = pascal[i - 1]
        row = [1]
        for inner_array_index in range(1, len(previous_array)):
            value = previous_array[inner_array_index - 1] + previous_array[inner_array_index]
            row.append(value)

        row.append(1)
        pascal.append(row)

    return pascal[n]


print(nth_row_pascal(0))


def nth_row_pascal2(n):
    if n == 0:
        return [1]

    current_row = [1]

    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            next_number = previous_row[j] + previous_row[j-1]
            current_row.append(next_number)

        current_row.append(1)

    return current_row
