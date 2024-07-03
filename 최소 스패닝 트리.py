import sys


def find_parent(node: int, parents: list) -> int:
    if parents[node] != node:
        parents[node] = find_parent(parents[node], parents)

    return parents[node]


def union_parent(parents: list, a_parent: int, b_parent: int) -> None:
    if a_parent < b_parent:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent


def solution(v: int, edges: list) -> int:
    # 부모 테이블
    parents = [i for i in range(v + 1)]

    # 비용 적은 순으로 정렬
    edges.sort()

    edges_count = 0  # 선택된 간선 개수
    total_cost = 0  # 선택된 간선에 대한 총 비용
    for cost, node_a, node_b in edges:
        a_parent = find_parent(node_a, parents)
        b_parent = find_parent(node_b, parents)

        # 사이클이 생기지 않을 경우 해당 간선을 선택한다.
        if a_parent != b_parent:
            # 부모 테이블 업데이트
            union_parent(parents, a_parent, b_parent)

            edges_count += 1
            total_cost += cost

        if edges_count == v - 1:
            break

    return total_cost


if __name__ == "__main__":
    # v: 정점 개수 / e: 간선 개수
    v, e = map(int, input().split())

    edges = []
    for _ in range(e):
        node_a, node_b, cost = map(int, sys.stdin.readline().split())
        edges.append((cost, node_a, node_b))

    result = solution(v, edges)
    print(result)
