from heapq import heappush, heappop

INF = 1e7


def solution(N, road, K):
    # 시작 노드 1 고정
    # 시작 노드로부터 다른 노드까지의 최단 거리 저장
    distance = [INF] * (N + 1)
    distance[1] = 0

    graph = [[] for _ in range(N + 1)]

    # 도로는 양방향
    for start, end, value in road:
        graph[start].append([end, value])
        graph[end].append([start, value])

    queue = []
    for end, value in graph[1]:
        heappush(queue, [value, end])

    while queue:
        cost, node = heappop(queue)

        if cost <= distance[node]:
            distance[node] = cost

            for next_node, next_cost in graph[node]:
                if cost + next_cost <= distance[next_node]:
                    heappush(queue, [cost + next_cost, next_node])

    return sum(1 for n in distance if n <= K)


result = solution(
    N=5,
    road=[[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]],
    K=3,
)

print(result)  # 정답: 4
