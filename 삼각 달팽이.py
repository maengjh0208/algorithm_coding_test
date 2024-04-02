def solution(n: int) -> list:
    dxs = (1, 0, -1)
    dys = (0, 1, -1)

    triangle_graph = [[0] * (i + 1) for i in range(n)]

    x, y = -1, 0
    count = 0
    for idx, loop in enumerate(range(n, 0, -1)):
        for _ in range(loop):
            x += dxs[idx % 3]
            y += dys[idx % 3]
            count += 1

            triangle_graph[x][y] = count

    result = []
    for array in triangle_graph:
        result += array

    return result


if __name__ == "__main__":
    result = solution(4)

    print(result)
    print(result == [1,2,9,3,10,8,4,5,6,7])