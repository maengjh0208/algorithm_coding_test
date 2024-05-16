# 가장 비용이 낮은 선 부터 선택하되, 사이클이 생기지 않도록 한다.
# union-find를 이용해서 사이클 생기지 않도록 방지

import sys


def solution(N: int, links: list):
    # union-find 중 find 함수
    def get_parent(node: int) -> int:
        if node == parents[node]:
            return node
        else:
            return get_parent(parents[node])

    # union-find 중 union 함수
    def union_parent(parent_node_a: int, parent_node_b: int):
        nonlocal parents
        parents[max(parent_node_a, parent_node_b)] = min(parent_node_a, parent_node_b)

    # 연결된 부모 노드 (초기엔 자기 자신으로 초기화)
    parents = [i for i in range(N + 1)]

    # 비용 낮은 순서로 정렬
    links.sort(key=lambda x: x[2])

    count = 0  # 연결된 선 개수
    result = 0  # 총 비용
    for node_a, node_b, cost in links:
        # 부모 노드 확인
        parent_node_a = get_parent(node_a)
        parent_node_b = get_parent(node_b)

        # 사이클이 생기지 않는다면 연결한다.
        if parent_node_a != parent_node_b:
            result += cost
            count += 1
            # 부모 노드 변경
            union_parent(parent_node_a, parent_node_b)

        # 선은 N-1개 만큼 연결함
        if count == N - 1:
            break

    return result


if __name__ == "__main__":
    # 컴퓨터 수
    N = int(input())

    # 연결할 수 있는 선의 수
    M = int(input())

    # 연결 비용 정보 (비용, 시작지점, 도착지점)
    links = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

    print(solution(N, links))
