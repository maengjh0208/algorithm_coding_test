INF = 1e9


def get_smallest_node(visited, distance):
    min_value = INF
    index = 0

    for node in range(1, len(distance)):
        if not visited[node] and distance[node] < min_value:
            min_value = distance[node]
            index = node

    return index


def solution(N, road, K):
    # 노드별로, 해당 노드를 방문한 적 있는지 체크하는 목적의 리스트
    visited = [False] * (N + 1)

    # 최단 거리 리스트 (1번 노드로부터 최단 거리)
    distance = [INF] * (N + 1)

    # 임의 두 노드를 연결하는 도로는 2개 이상 존재 가능. 그 중 최단 거리 구하기
    temp_graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
    for a, b, c in road:
        # a <-> b 이동 비용 : c
        if c < temp_graph[a][b]:
            temp_graph[a][b] = c
            temp_graph[b][a] = c

    # 각 노드별 연결되어 있는 노드에 대한 정보
    graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if temp_graph[i][j] != INF:
                graph[i].append((j, temp_graph[i][j]))

    # 1번 노드 방문 & 거리 세팅
    visited[1] = True
    distance[1] = 0
    for connect_node, cost in graph[1]:
        distance[connect_node] = cost

    # 1번 노드 제외한 나머지 노드에 대해서 최단 거리 갱신
    for _ in range(N - 1):
        # 방문하지 않은 노드 중 가장 거리가 짧은 노드
        node = get_smallest_node(visited, distance)

        # 노드 방문 및 거리 세팅
        visited[node] = True
        for connect_node, cost in graph[node]:
            # 현재 노드를 방문해서 지나는 경우가 더 짧은 경우 갱신
            if distance[node] + cost < distance[connect_node]:
                distance[connect_node] = distance[node] + cost

    # k 시간 이하로 배달이 가능한 노드 개수
    count = 0
    for i in distance[1:]:
        if i <= K:
            count += 1

    return count


if __name__ == "__main__":
    result = solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
    print(result)