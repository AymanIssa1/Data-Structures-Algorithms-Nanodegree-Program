# imports for printing a matrix, nicely
import pprint
pp = pprint.PrettyPrinter()

def lps(input_string):
    n = len(input_string)
    L = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        L[i][i] = 1

    for s_size in range(2, n + 1):
        for start_idx in range(n - s_size + 1):
            end_index = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_index]:
                L[start_idx][end_index] = 2
            elif input_string[start_idx] == input_string[end_index]:
                L[start_idx][end_index] = L[start_idx + 1][end_index - 1] + 2
            else:
                L[start_idx][end_index] = max(L[start_idx][end_index - 1], L[start_idx + 1][end_index])


    pp.pprint(L)
    return L[0][n - 1]


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'BxAoNxAoNxA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)

[[1, 1, 1, 1, 1, 0],
 [0, 1, 1, 3, 3, 0],
 [0, 0, 1, 1, 5, 0],
 [0, 0, 0, 1, 1, 0],
 [0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 1]]
