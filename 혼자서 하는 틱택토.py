# 선공 O, 후공 X, 서로 번갈아가면서 표시
# 가로, 세로, 대각선 등 3개가 같은 표시가 만들어지면 승리

# 규칙 실수
# 1. O를 표시할 차례인데 X를 표시하거나 혹은 그 반대
# 2. 누군가 이미 승리해서 게임이 종료된 상태인데도 계속 게임을 진행하는 경우
def solution(board):
    count_O = 0
    count_X = 0
    bingo_count = {"O": 0, "X": 0}

    for array in board:
        count_O += array.count("O")
        count_X += array.count("X")

    if count_O not in (count_X, count_X + 1):
        return 0

    # 가로로 같은 표시 만들어지는지 확인
    count = 0
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ".":
            bingo_count[board[i][0]] += 1
            count += 1

    if count > 1:
        return 0

    # 세로로 같은 표시 만들어지는지 확인
    count = 0
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != ".":
            bingo_count[board[0][j]] += 1
            count += 1

    if count > 1:
        return 0

    # 대각선으로 같은 표시 만들어지는지 확인
    if board[0][0] == board[1][1] == board[2][2] != "." or board[0][2] == board[1][1] == board[2][0] != ".":
        bingo_count[board[1][1]] += 1

    # "O"가 이긴 경우엔 "O" 개수가 "X" 개수보다 많아야 함
    # "X"가 이긴 경우엔 "O" 개수와 "X" 개수가 같아야 함
    if (bingo_count["O"] > 0 and count_O <= count_X) or (bingo_count["X"] > 0 and count_O != count_X):
        return 0
    else:
        return 1


if __name__ == "__main__":
    result = solution(["XXO", ".OX", "O.."])
    print(result)
