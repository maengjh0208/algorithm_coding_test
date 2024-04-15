# 늑대에게 잡아먹히지 않는 최대한 많은 수의 양은 리턴
# 양의 수보다 늑대의 수가 같거나 더 많아지면 모든 양이 잡아먹힘
# 0은 양, 1은 늑대
# info[0]은 항상 0(=양)


from collections import defaultdict

SHEEP = 0
WOLF = 1


def solution(info: list, edges: list):
    graph = defaultdict(list)

    for parent, child in edges:
        graph[parent].append(child)

    max_sheep = 0

    # dfs를 위한 스택, (현재 노드, 이동가능한 노드, 양의 수, 늑대 수)
    stack = [[0, graph[0], 1, 0]]

    while stack:
        current_node, possible_nodes, sheep_count, wolf_count = stack.pop()

        max_sheep = max(max_sheep, sheep_count)

        for idx, next_node in enumerate(possible_nodes):
            new_sheep_count = sheep_count + (info[next_node] == SHEEP)
            new_wolf_count = wolf_count + (info[next_node] == WOLF)

            if new_sheep_count > new_wolf_count:
                stack.append([
                    next_node,
                    possible_nodes[:idx] + possible_nodes[idx + 1:] + graph[next_node],
                    new_sheep_count,
                    new_wolf_count
                ])

    return max_sheep


if __name__ == "__main__":
    result = solution(
        info=[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        edges=[[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]],
    )

    print(result)
