def solution(arr1, arr2):
    row = len(arr1)
    column = len(arr2[0])

    answer = [[0] * column for _ in range(row)]

    for i in range(row):
        for j in range(column):
            answer[i][j] = sum([arr1[i][k] * arr2[k][j] for k in range(len(arr2))])

    return answer


if __name__ == "__main__":
    result = solution(
        arr1=[[1, 4], [3, 2], [4, 1]],
        arr2=[[3, 3], [3, 3]],
    )

    print(result)
