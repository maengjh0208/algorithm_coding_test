import sys
from heapq import heappush, heappop

INF = 1e9


def solution(v: int, start_node: int, graph: list) -> list:
    distances = [INF] * (v + 1)

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


def convert(distances):
    new_distances = []

    for cost in distances[1:]:
        if cost == INF:
            new_distances.append("INF")
        else:
            new_distances.append(str(cost))

    return new_distances


if __name__ == "__main__":
    # v: 정점 개수 / e: 간선 개수
    v, e = map(int, input().split())

    # 시작 지점
    start_node = int(input())

    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start].append((end, cost))

    distances = solution(v, start_node, graph)
    new_distances = convert(distances)

    print("\n".join(new_distances))
