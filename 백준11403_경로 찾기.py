import sys


def solution(graph):
    N = len(graph)

    is_exist = "1"

    # k: 거쳐가는 노드
    for k in range(N):
        # i: 출발 노드
        for i in range(N):
            #  j: 도착 노드
            for j in range(N):
                # k를 거쳐가는 노드가 있는지 구한다.
                if graph[i][k] == is_exist and graph[k][j] == is_exist:
                    graph[i][j] = is_exist

    return graph


if __name__ == "__main__":
    # 정점의 개수
    N = int(input())

    # 노드 간 연결 정보
    graph = []
    for i in range(N):
        graph.append(sys.stdin.readline().split())

    result = solution(graph)
    for row in result:
        sys.stdout.write(" ".join(row) + "\n")
