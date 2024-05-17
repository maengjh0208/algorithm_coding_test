from collections import deque


def solution(grid: list) -> int:
    def bfs(x: int, y: int) -> int:
        # 위 / 아래 / 오른쪽 / 왼쪽
        dxs = (-1, 1, 0, 0)
        dys = (0, 0, 1, -1)

        queue = deque([[x, y]])
        count = 0
        checked[x][y] = True

        while queue:
            cx, cy = queue.popleft()
            count += 1

            for dx, dy in zip(dxs, dys):
                new_x = cx + dx
                new_y = cy + dy

                # grid 범위를 벗어나지 않고 + grid 섬 + 아직 방문하지 않은 경우
                if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 1 and not checked[new_x][new_y]:
                    checked[new_x][new_y] = True
                    queue.append([new_x, new_y])

        return count

    M = len(grid)  # 행 개수
    N = len(grid[0])  # 열 개수
    checked = [[False] * N for _ in range(M)]

    max_area = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1 and not checked[i][j]:
                max_area = max(bfs(i, j), max_area)

    return max_area


if __name__ == "__main__":
    result = solution(
        [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]]
    )

    print(result)
