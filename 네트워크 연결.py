# 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력
# 모든 컴퓨터를 연결할 수 없는 경우는 없음

import sys


def find_parent(node: int, parents: list) -> int:
    if parents[node] != node:
        parents[node] = find_parent(parents[node], parents)

    return parents[node]


def union_parent(parent_node_1: int, parent_node_2: int, parents: list) -> None:
    if parent_node_1 < parent_node_2:
        parents[parent_node_2] = parent_node_1
    else:
        parents[parent_node_1] = parent_node_2


# n: 총 정점 개수 / costs: 간선, 비용 정보
def solution(n: int, costs: list):
    # 비용 적은 순으로 정렬
    costs.sort()

    # 부모 테이블
    parents = [i for i in range(n + 1)]

    total_cost = 0  # 총 비용
    edge_count = 0  # 선택된 간선 수

    for cost, node_a, node_b in costs:
        # 부모 노드 확인
        a_parent = find_parent(node_a, parents)
        b_parent = find_parent(node_b, parents)

        # 사이클이 생기지 않을 경우 간선 선택
        if a_parent != b_parent:
            # 부모 노드 업데이트
            union_parent(a_parent, b_parent, parents)

            # 비용, 간선 개수 업데이트
            total_cost += cost
            edge_count += 1

        if edge_count == n - 1:
            break

    return total_cost


if __name__ == "__main__":
    # 컴퓨터 수
    n = int(input())

    # edge 수
    m = int(input())

    costs = []
    for _ in range(m):
        node_a, node_b, cost = map(int, sys.stdin.readline().split())

        if node_a != node_b:
            costs.append((cost, node_a, node_b))

    result = solution(n, costs)
    print(result)
