def solution(array, commands):
    result = []
    for i, j, k in commands:
        result.append(sorted(array[i - 1:j])[k - 1])

    return result


if __name__ == "__main__":
    result = solution(
        array=[1, 5, 2, 6, 3, 7, 4],
        commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]],
    )

    print(result)
