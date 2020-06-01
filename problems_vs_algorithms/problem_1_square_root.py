def sqrt(number):
    if number < 0:
        return None

    if number == 0 or number == 1:
        return number

    front = 1
    back = number // 2
    while front <= back:
        middle = (front + back) // 2

        if middle * middle == number:
            return middle

        if middle * middle < number:
            front = middle + 1
        else:
            back = middle - 1

    return middle - 1


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (None == sqrt(-27)) else "Fail")
