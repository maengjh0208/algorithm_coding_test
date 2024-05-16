def floyd(graph):
    # 노드 개수
    N = len(graph)

    # k: 거쳐가는 노드
    for k in range(N):
        # i: 출발 노드
        for i in range(N):
            # j: 출발 노드
            for j in range(N):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph


if __name__ == "__main__":
    INF = 1e8

    graph = [
        [0, 5, INF, 8],
        [7, 0, 9, INF],
        [2, INF, 0, 4],
        [INF, INF, 3, 0]
    ]

    result = floyd(graph)
    for i in result:
        print(i)
