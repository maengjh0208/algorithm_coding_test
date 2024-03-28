def function():
    while(1):
        numbers = input()

        if numbers == "0":
            break

        if numbers == numbers[::-1]:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    function()