"""
최소 신장 트리(Minimum Spanning Tree, MST) 문제
- 최소 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 "최소 비용"을 리턴

크루스칼 알고리즘 적용
- 선택될 간선의 숫자 = 노드 개수 - 1
- 최소 비용의 간선부터 선택하되, 사이클이 형성되지 않도록 주의한다.
"""


def solution(n: int, costs: list) -> int:
    # 사이클 존재 여부를 확인할 수 있는 리스트
    cycle = [i for i in range(n)]

    costs.sort(key=lambda x: x[2])

    # count:사용된 간선 개수 / min_value: 모든 섬이 서로 통행 가능한 최소 비용
    count = 0
    min_value = 0

    for i, j, cost in costs:
        # 사이클이 생기지 않는다는 조건
        if cycle[i] != cycle[j]:
            parent = min(cycle[i], cycle[j])
            child = max(cycle[i], cycle[j])

            for idx, node in enumerate(cycle):
                if node == child:
                    cycle[idx] = parent

            count += 1
            min_value += cost

        if count == (n - 1):
            break

    return min_value


if __name__ == "__main__":
    result = solution(
        n=4,
        costs=[[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    )

    print(result)