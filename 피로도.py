max_cnt = 0


def dfs(k: int, dungeons: list, visited: list, cnt: int):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    if max_cnt == len(dungeons):
        return

    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= k:
            visited[i] = True
            dfs(k - dungeons[i][1], dungeons, visited, cnt + 1)
            visited[i] = False


def solution(k, dungeons):
    global max_cnt
    visited = [False] * len(dungeons)

    dfs(k, dungeons, visited, 0)
    return max_cnt


if __name__ == "__main__":
    result = solution(80, [[80,20],[50,40],[30,10]])

    print(result)
    print(result == 3)
