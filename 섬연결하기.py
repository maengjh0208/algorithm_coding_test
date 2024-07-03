def find_parent(node: int, parent: list) -> int:
    if parent[node] != node:
        parent[node] = find_parent(parent[node], parent)

    return parent[node]


def union_parent(a_parent: int, b_parent: int, parent: list) -> None:
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


def solution(n: int, costs: list):
    # 부모 테이블 (초기 세팅: 자기 자신이 부모)
    parent = [i for i in range(n + 1)]

    # 비용 작은 순서대로 정렬
    costs.sort(key=lambda x: x[2])

    total_cost = 0  # 총 비용
    connect_edge = 0  # 연결된 간선 수

    for node_a, node_b, cost in costs:
        # 사이클이 생기지 않을 경우 해당 간선을 선택한다.
        a_parent = find_parent(node_a, parent)
        b_parent = find_parent(node_b, parent)

        if a_parent != b_parent:
            union_parent(a_parent, b_parent, parent)

            connect_edge += 1
            total_cost += cost

        if connect_edge == n - 1:
            break

    return total_cost


if __name__ == "__main__":
    result = solution(
        n=4,
        costs=[[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]],
    )

    print(result)  # output: 4
