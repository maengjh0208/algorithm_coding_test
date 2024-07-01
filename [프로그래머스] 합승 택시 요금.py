# https://school.programmers.co.kr/learn/courses/30/lessons/72413

from heapq import heappush, heappop

INF = 1e9


# n: 지점 개수 / s: 출발 지점 / fares: 각 지점 간 택시 요금
def dijkstra(n: int, s: int, fare_graph: list) -> list:
    distances = [INF] * (n + 1)

    queue = [(0, s)]

    while queue:
        cost, node = heappop(queue)

        if cost < distances[node]:
            distances[node] = cost

            for next_node, next_cost in fare_graph[node]:
                new_cost = cost + next_cost
                if new_cost < distances[next_node]:
                    heappush(queue, (new_cost, next_node))

    return distances


# n: 지점 개수 / s: 출발 지점 / a: A의 도착 지점 / b: B의 도착 지점 / fares: 각 지점 간 택시 요금
def solution(n: int, s: int, a: int, b: int, fares: list) -> int:
    fare_graph = [[] for _ in range(n + 1)]

    for start, end, cost in fares:
        fare_graph[start].append((end, cost))
        fare_graph[end].append((start, cost))

    s_distances = dijkstra(n, s, fare_graph)
    a_distances = dijkstra(n, a, fare_graph)
    b_distances = dijkstra(n, b, fare_graph)

    minimum_cost = s_distances[a] + s_distances[b]
    for i in range(1, n + 1):
        common_cost = s_distances[i]
        rest_a_cost = a_distances[i]
        rest_b_cost = b_distances[i]

        minimum_cost = min(minimum_cost, common_cost + rest_a_cost + rest_b_cost)

    return minimum_cost


result = solution(
    n=6,
    s=4,
    a=6,
    b=2,
    fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
)

print(result)  # 정답: 82
