# 지도에서 강철부대가 위치한 지역을 포함한 각 지역은 유일한 번호로 구분
# 두 지역 간의 길을 통과하는 데 걸리는 시간은 모두 1로 동일
# 최단시간에 부대로 복귀 /  적군의 방해 / 임무의 시작 때와 다르게 되돌아오는 경로가 없어져 복귀가 불가능한 경우 존재


from heapq import heappush, heappop

INF = int(1e6)


def solution(n, roads, sources, destination):
    distance = [INF] * (n + 1)

    graph = [[] for _ in range(n + 1)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    # 초기 세팅 (destination으로부터 다른 지점까지의 최단 거리 구하기)
    heap = []
    distance[destination] = 0
    for i in graph[destination]:
        distance[i] = 1
        heappush(heap, (1, i))

    while heap:
        value, region = heappop(heap)
        value += 1

        for i in graph[region]:
            if value < distance[i]:
                distance[i] = value
                heappush(heap, (value, i))

    return [distance[source] if distance[source] != INF else -1 for source in sources]


if __name__ == "__main__":
    result = solution(
        n=5,
        roads=[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],
        sources=[1, 3, 5],
        destination=5
    )
    print(result)
