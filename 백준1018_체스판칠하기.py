def function():
    # N: 세로 길이 / M: 가로 길이
    N, M = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(input()))

    # board_b: 처음 'B'부터 시작될 경우 각 수정이 필요한 영역 표시 (수정이 필요하면 1, 아니면 0)
    # board_w: 처음 'W'부터 시작될 경우 각 수정이 필요한 영역 표시 (수정이 필요하면 1, 아니면 0)
    board_b = [[0 for i in range(M)] for j in range(N)]
    board_w = [[0 for i in range(M)] for j in range(N)]

    for i in range(N):
        for j in range(M):
            # board_b의 경우 'B'가 되는 영역 / board_w의 경우 'W"가 되는 영역
            if (i + j) % 2 == 0:
                if board[i][j] == "W":
                    board_b[i][j] = 1
                else:
                    board_w[i][j] = 1
            # board_b의 경우 'W'가 되는 영역 / board_w의 경우 'B"가 되는 영역
            else:
                if board[i][j] == "B":
                    board_b[i][j] = 1
                else:
                    board_w[i][j] = 1

    # 'B'로 시작하는 경우와 'W'로 시작하는 경우 모두 비교하여 최솟값 찾기
    min_value_b = 64
    min_value_w = 64

    for k in range(N - 7):
        for j in range(M - 7):
            temp_b = 0
            temp_w = 0

            for i in range(k, k + 8):
                temp_b += sum(board_b[i][j : j + 8])
                temp_w += sum(board_w[i][j: j + 8])

            min_value_b = temp_b if temp_b < min_value_b else min_value_b
            min_value_w = temp_w if temp_w < min_value_w else min_value_w

    print(min(min_value_b, min_value_w))


if __name__ == "__main__":
    function()