def coin_change(coins, amount):
    memo = {}

    def return_change(remaining):
        print("return_char(remaining=",remaining,")")
        print("meme=",memo)
        # base cases
        if remaining < 0: return float('inf')
        if remaining == 0: return 0

        # Check if we have already calculated
        if remaining not in memo:
            # If not previously calculated, calculate it by calling return_change with the remaining amount
            memo[remaining] = min(return_change(remaining - coin) + 1 for coin in coins)
        return memo[remaining]

    res = return_change(amount)
    print("final meme=",memo)
    return -1 if res == float('inf') else res


def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1, 4, 5, 6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5, 7, 8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)
