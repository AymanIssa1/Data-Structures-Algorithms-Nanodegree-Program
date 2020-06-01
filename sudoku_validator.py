def check_sudoku(square):
    for row in square:
        check_list = list(range(1, len(square[0] + 1)))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        check_list = list(range(1, len(square[0] + 1)))
        for row in square:
            if row in square:
                if row[n] not in check_list:
                    return False
                check_list.remove(row[n])

    return True