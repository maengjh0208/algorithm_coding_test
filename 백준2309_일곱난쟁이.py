from itertools import combinations


def function():
    heights = [int(input()) for _ in range(9)]

    for array in combinations(heights, 7):
        if sum(array) == 100:
            temp = sorted(list(array))

            for j in temp:
                print(j)

            break


if __name__ == "__main__":
    function()