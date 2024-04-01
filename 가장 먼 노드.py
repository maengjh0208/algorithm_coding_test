# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 노드개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지 return

from collections import deque


def solution(n: int, edge: list) -> int:
    # 간선 정보
    graph = [[] for _ in range(n + 1)]
    for node_a, node_b in edge:
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    max_value = 0
    max_value_count = 0

    checked = [False] * (n + 1)  # 방문 여부
    distance = [-1] * (n + 1)  # 각 노드까지 거리 (간선 개수)

    node_queue = deque()  # 큐
    distance_queue = deque()

    # 1번 노드 방문
    checked[1] = True
    distance[1] = 0
    for node in graph[1]:
        node_queue.append(node)  # 다음 노드 정보
        distance_queue.append(1)  # 간선 개수

    # 각 노드별 간선 길이 구하기 (distance 객체 업데이트 목적)
    while node_queue:
        node = node_queue.popleft()
        d = distance_queue.popleft()

        max_value = max(max_value, d)

        # node 방문
        checked[node] = True
        distance[node] = d
        for next_node in graph[node]:
            if not checked[next_node] and next_node not in node_queue:
                node_queue.append(next_node)
                distance_queue.append(d + 1)

    # max_value 간선 길이를 갖는 노드 개수 구하기
    for i in distance[1:]:
        if i == max_value:
            max_value_count += 1

    return max_value_count


if __name__ == "__main__":
    result = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

    print(result)
    print(result == 3)