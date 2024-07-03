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


def solution(n: int, edges: list) -> int:
    # 부모 테이블
    parents = [i for i in range(n + 1)]

    # 비용 적은 순으로 정렬
    edges.sort()

    total_cost = 0  # 총 연결된 간선 비용
    edge_count = 0  # 연결된 간선 개수

    for cost, node_a, node_b in edges:
        if edge_count == n - 2:
            break

        a_parent = find_parent(node_a, parents)
        b_parent = find_parent(node_b, parents)

        # 사이클이 생기지 않는다면 해당 간선을 포함시킨다.
        if a_parent != b_parent:
            # 부모 테이블 업데이트
            union_parent(parents, a_parent, b_parent)

            total_cost += cost
            edge_count += 1

    return total_cost


if __name__ == "__main__":
    # n: 정점 개수 / m: 간선 개수
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        node_a, node_b, cost = map(int, sys.stdin.readline().split())
        edges.append((cost, node_a, node_b))

    result = solution(n, edges)
    print(result)
