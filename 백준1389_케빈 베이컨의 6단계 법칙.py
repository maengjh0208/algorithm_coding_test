# 모든 사람은 친구 관계로 연결되어져 있다.

import sys


def solution():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


if __name__ == "__main__":
    INF = 1e6

    # N: 사람 수 / M: 친구 관계 수
    N, M = map(int, input().split())

    # 친구 연결 관계
    graph = [[INF] * N for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0

    # 친구 연결 관계 초기 세팅
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1

        graph[a][b] = 1
        graph[b][a] = 1

    # 최단 관계수 구하기
    solution()

    min_value = INF
    result = 0
    for idx, friend_info in enumerate(graph):
        sum_value = sum(friend_info)
        if sum_value < min_value:
            min_value = sum_value
            result = idx

    print(result + 1)
