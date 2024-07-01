from heapq import heappop, heappush

INF = 1e9


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    summits_set = set(summits)
    gates_set = set(gates)
    distance = [INF] * (n + 1)
    queue = []  # [ [intensity, node], ... ]

    for node_1, node_2, cost in paths:
        graph[node_1].append([node_2, cost])
        graph[node_2].append([node_1, cost])

    for start_node in gates:
        heappush(queue, [0, start_node])

    while queue:
        intensity, node = heappop(queue)

        if intensity < distance[node]:
            distance[node] = intensity

            if node in summits_set:
                continue

            for next_node, next_cost in graph[node]:
                new_intensity = max(next_cost, intensity)
                heappush(queue, [new_intensity, next_node])

    summits.sort()
    min_summit = 0
    min_intensity = INF

    for summit in summits:
        if distance[summit] < min_intensity:
            min_summit = summit
            min_intensity = distance[summit]

    return [min_summit, min_intensity]


result = solution(
    n=6,
    paths=[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
    gates=[1, 3],
    summits=[5],
)

print(result)  # 정답: [5, 3]
