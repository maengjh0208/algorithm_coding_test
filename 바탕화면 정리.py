# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/161990

# 컴퓨터 바탕화면은 각 칸이 정사각형인 격자판이며, 파일들은 바탕화면의 격자판 위에 존재한다.
# wallpaper: 컴퓨터 바탕화면의 상태를 나타낸 문자열 배열
# 바탕화면의 가장 왼쪽 위 위치: (0, 0)
# 빈칸은 ".", 파일이 있는 칸은 "#"
# 드래그하면 파일 선택 가능. 선택된 파일 삭제 가능
# 최소한의 이동거리를 갖는 한 번의 드래그로 모든 파일을 선택해서 한번에 지우려고 한다.
# 점 S(lux, luy)에서 점 E(rdx, rdy)로 드래그를 할 때, "드래그 한 거리"는 |rdx - lux| + |rdy - luy|로 정의


def solution(wallpaper):
    # board 생성
    board = [list(i) for i in wallpaper]

    lux, luy, rdx, rdy = len(board), len(board[0]), 0, 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "#":
                # 가장 왼쪽 위 점 찾기 (lux, luy)
                if i <= lux:
                    lux = i

                if j <= luy:
                    luy = j

                # 가장 오른쪽 아래 점 찾기 (rdx, rdy)
                if rdx <= i:
                    rdx = i

                if rdy <= j:
                    rdy = j

    rdx += 1
    rdy += 1

    # [lux, luy, rdx, rdy] 반환하기
    return [lux, luy, rdx, rdy]


if __name__ == "__main__":
    wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
    result = solution(wallpaper)
    print(result)