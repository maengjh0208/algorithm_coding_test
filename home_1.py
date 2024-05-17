def solution(arr: list) -> int:
    def check(i: int, j: int):
        check_count = 0
        # i행 확인
        for idx in range(N):
            if arr[i][idx] == "B":
                check_count += 1
                board[i][idx] = 0

        # j열 확인
        for idx in range(M):
            if arr[idx][j] == "B":
                check_count += 1
                board[idx][j] = 0

        return check_count == 2

    # (arr 2차원 배열) M: 행 개수 / N: 열 개수
    M = len(arr)
    N = len(arr[0])

    board = [[1] * N for _ in range(M)]

    count = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == "B" and board[i][j] and check(i, j):
                count += 1

    return count


if __name__ == "__main__":
    result = solution([["B", "B", "W"], ["B", "B", "W"], ["B", "B", "W"]])
    print(result)
