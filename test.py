# 특정 원소가 속한 집합 찾기
def find_parent(parent: list, x: int):
    # 루트 노드 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a_parent, b_parent):
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent

    return parent


# v: 노드 개수, edges: 간선에 대한 정보(비용, 연결된노드1, 연결된노드2)
def solution(v: int, edges: list):
    # 부모 테이블 자기자신으로 초기화 (사이클 여부 확인 목적)
    parent = [i for i in range(v + 1)]

    # 간선을 비용순으로 정렬
    edges.sort()

    result = 0
    count = 0
    for cost, a, b in edges:
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        a_parent = find_parent(parent, a)
        b_parent = find_parent(parent, b)

        if a_parent != b_parent:
            union_parent(parent, a_parent, b_parent)
            result += cost
            count += 1

        # 간선 숫자 = 노드 개수 - 1
        if count == v - 1:
            break

    print(parent)

    return result


if __name__ == "__main__":
    result = solution(
        v=5,
        edges=[(1, 1, 2), (2, 3, 4), (3, 2, 4), (4, 1, 3), (5, 3, 5), (2, 2, 3)]
    )

    print(result) # output: 10