import sys


def function():
    numbers = []

    for _ in range(int(input())):
        word = sys.stdin.readline().strip()

        check = []

        for i in word:
            if not i.isalpha():
                check.append(i)
            elif check:
                numbers.append(int("".join(check)))
                check = []

        if check:
            numbers.append(int("".join(check)))

    for i in sorted(numbers):
        print(i)


if __name__ == "__main__":
    function()