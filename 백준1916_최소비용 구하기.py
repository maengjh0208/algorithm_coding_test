import sys
from heapq import heappop, heappush

INF = 1e9


# N: 도시 개수 / start: 시작 도시 번호 / end: 도착 도시 번호
# start -> end 까지의 최단 거리 구하기
def solution(N: int, start: int, end: int) -> int:
    # 시작 위치 기준 최소 거리
    distance = [INF] * (N + 1)
    distance[start] = 0

    queue = []
    for node, value in graph[start]:
        heappush(queue, (value, node))

    while queue:
        value, node = heappop(queue)

        if value < distance[node]:
            distance[node] = value

            for next_node, next_value in graph[node]:
                if value + next_value < distance[next_node]:
                    heappush(queue, (value + next_value, next_node))

    return distance[end]


if __name__ == "__main__":
    # 도시 개수
    N = int(input())

    # 버스 개수
    M = int(input())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        start, end, value = map(int, sys.stdin.readline().split())
        graph[start].append((end, value))

    start, end = map(int, sys.stdin.readline().split())

    print(solution(N, start, end))
