from collections import deque


def bfs(x: int, y: int, checked: list, maps: list) -> tuple:
    row_length = len(maps)
    column_length = len(maps[0])

    # 왼, 위, 오른, 아래
    dxs = (-1, 0, 1, 0)
    dys = (0, -1, 0, 1)

    queue = deque([[x, y]])
    count = 0
    checked[x][y] = True

    while queue:
        x, y = queue.popleft()
        count += int(maps[x][y])

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if (0 <= new_x < row_length and 0 <= new_y < column_length
                and maps[new_x][new_y] != 'X' and checked[new_x][new_y] is False
            ):
                checked[new_x][new_y] = True
                queue.append([new_x, new_y])

    return count, checked


def solution(maps: list) -> list:
    checked = [[False] * len(maps[i]) for i in range(len(maps))]
    foods = []

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X' or checked[i][j] is True:
                continue

            food, checked = bfs(i, j, checked, maps)
            foods.append(food)

    return sorted(foods) if foods else [-1]


if __name__ == "__main__":
    result = solution(["X591X", "X1X5X", "X231X", "1XXX1"])
    print(result)
    print(result == [1, 1, 27])
