def function():
    N = int(input())

    factorial_result = 1

    if N == 0:
        print(factorial_result)
    else:
        for i in range(1, N + 1):
            factorial_result *= i

        print(factorial_result)


if __name__ == "__main__":
    function()