import sys


def solution(graph: list):
    # graph: 간선 정보 / n: 도시 개수
    n = len(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # 이동 불가 지역은 비용을 0 으로 설정
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                graph[i][j] = 0

    return graph


if __name__ == "__main__":
    INF = int(1e9)

    # 도시 개수
    N = int(input())

    graph = [[INF] * N for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0

    for _ in range(int(input())):
        start, end, cost = map(int, sys.stdin.readline().split())
        start -= 1
        end -= 1

        graph[start][end] = min(graph[start][end], cost)

    result = solution(graph)
    for i in result:
        sys.stdout.write(" ".join(map(str, i)) + "\n")