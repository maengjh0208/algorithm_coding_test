from heapq import heappop, heappush
INF = 1e9


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    summits_set = set(summits)

    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    heap_queue = []  # (intensity, node)
    distance = [INF] * (n + 1)

    # 모든 출발지를 우선순위 큐에 삽입
    for gate in gates:
        heappush(heap_queue, (0, gate))
        distance[gate] = 0

    while heap_queue:
        intensity, node = heappop(heap_queue)

        # 산봉우리이거나 intensity가 더 크다면 이동하지 않음
        if node in summits_set or distance[node] < intensity:
            continue

        #  해당 노드에서 이동할 수 있는 곳으로 이동
        for next_node, weight in graph[node]:
            new_intensity = max(intensity, weight)
            if distance[next_node] > new_intensity:
                distance[next_node] = new_intensity
                heappush(heap_queue, (new_intensity, next_node))

    min_node = 0
    min_intensity = INF
    summits.sort()

    for summit in summits:
        if distance[summit] < min_intensity:
            min_node = summit
            min_intensity = distance[summit]

    return [min_node, min_intensity]


if __name__ == "__main__":
    result = solution(
        n=7,
        paths=[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]	,
        gates=[3, 7],
        summits=[1, 5]
    )

    print(result)