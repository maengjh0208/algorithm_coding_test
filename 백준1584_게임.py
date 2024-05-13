import sys
from heapq import heappush, heappop

INF = 1e9


def update_graph(danger_value, *args):
    global graph

    x1, y1, x2, y2 = args

    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            graph[i][j] = danger_value


def solution():
    # 최단 거리 정보
    distance = [[INF] * 501 for _ in range(501)]

    # 시작 위치 거리 설정
    distance[0][0] = 0

    # 방향: 왼쪽, 오른쪽, 아래, 위
    dxs = (0, 0, 1, -1)
    dys = (-1, 1, 0, 0)

    # 시작 위치에 대한 다음 최단 거리 구하기 / heap: (거리, x좌표, y좌표) 들의 리스트
    heap = []
    for x, y in [(0, 1), (1, 0)]:
        if graph[x][y] != 2:
            heappush(heap, (graph[x][y], x, y))

    while heap:
        value, x, y = heappop(heap)

        # 최단 거리 구하기
        if value < distance[x][y]:
            distance[x][y] = value

            if x == 500 and y == 500:
                break

            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx > 500 or ny < 0 or ny > 500:
                    continue

                if graph[nx][ny] != 2 and value + graph[nx][ny] < distance[nx][ny]:
                    heappush(heap, (value + graph[nx][ny], nx, ny))

    return -1 if distance[500][500] == INF else distance[500][500]


if __name__ == "__main__":
    # 0: 자유 롭게 다닐수 있는 곳, 1: 위험 지역, 2: 죽음 지역
    graph = [[0] * 501 for _ in range(501)]

    # 위험 구역 정보
    for _ in range(int(input())):
        update_graph(1, *map(int, sys.stdin.readline().split()))

    # 죽음 구역 정보
    for _ in range(int(input())):
        update_graph(2, *map(int, sys.stdin.readline().split()))

    print(solution())
