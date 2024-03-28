def function():
    expression = input().split("-")

    for i in range(len(expression)):
        expression[i] = sum(map(int, expression[i].split("+")))

    print(expression[0] - sum(expression[1 : ]))


if __name__ == "__main__":
    function()