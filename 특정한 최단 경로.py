import sys
from heapq import heappop, heappush

INF = 1e9


# n: 정점 개수 / start_node: 시작 지점 / graph: 연결 정보 (연결 노드 및 비용)
def solution(n: int, start_node, graph: list) -> list:
    distances = [INF] * (n + 1)

    queue = [(0, start_node)]

    while queue:
        cost, node = heappop(queue)

        if cost < distances[node]:
            distances[node] = cost

            for next_node, next_cost in graph[node]:
                new_cost = cost + next_cost

                if new_cost < distances[next_node]:
                    heappush(queue, (new_cost, next_node))

    return distances


if __name__ == "__main__":
    # n: 정점 개수 / e: 간선 개수
    n, e = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().split())

    start_distances = solution(n, 1, graph)
    v1_distances = solution(n, v1, graph)
    v2_distances = solution(n, v2, graph)

    case_1 = start_distances[v1] + v1_distances[v2] + v2_distances[n]
    case_2 = start_distances[v2] + v2_distances[v1] + v1_distances[n]

    if start_distances[n] == INF:
        print(-1)
    else:
        print(min(case_1, case_2))
