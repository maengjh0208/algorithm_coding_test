import sys
from heapq import heappop, heappush

INF = 1e6


def solution(N: int, M: int, K: int, X: int, graph: list):
    # 최단 거리 테이블 (출발 노드는 거리 0으로 설정, 그 외에는 무한대로 설정)
    distance = [INF] * (N + 1)
    distance[X] = 0

    # 출발 노드와 연결된 최단 노드 확인
    queue = []
    for node in graph[X]:
        heappush(queue, (1, node))

    # 최단 거리 테이블 계산
    while queue:
        value, node = heappop(queue)
        next_value = value + 1

        if value < distance[node]:
            distance[node] = value

            for next_node in graph[node]:
                if next_value < distance[next_node]:
                    heappush(queue, (next_value, next_node))

    # 최단 거리가 K인 도시 개수 구하기
    cities = []
    for i in range(1, N + 1):
        if distance[i] == K:
            cities.append(str(i))

    if cities:
        print("\n".join(cities))
    else:
        print(-1)


if __name__ == "__main__":
    # N: 도시 개수, M: 도로 개수, K: 거리, X: 출발 도시 번호
    N, M, K, X = map(int, sys.stdin.readline().split())

    # 도로 정보
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)

    solution(N, M, K, X, graph)