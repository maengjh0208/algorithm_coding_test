import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

"""
기본 세팅
"""
# n:노드개수, m:간선개수
n, m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 각 노드별 연결되어 있는 노드에 대한 정보
graph = [[] for _ in range(n + 1)]

# 해당 노드를 방문한 적이 있는지 확인하는 목적의 리스트 (False로 세팅)
visited = [False] * (n + 1)

# 최단 거리 리스트 (무한으로 세팅)
distance = [INF] * (n + 1)

"""
모든 간선 정보 받기
"""
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 비용이 c 라는 의미
    graph[a].append((b, c))


"""
방문하지 않은 노드 중, 가장 최소 비용인 노드 구하기
"""
def get_smallest_node():
    min_value = INF

    index = 0
    for node in range(1, n + 1):
        if not visited[node] and distance[node] < min_value:
            min_value = distance[node]
            index = node

    return index


"""
다익스트라 알고리즘 
- 최단 경로 구하기. 매 순간 가장 최적의 값을 구하기 때문에 그리디 분류에 속함.
- 간선 비용이 음의 값이면 안됨. 간선은 양방향, 단방향 상관 없음
- 정해진 하나의 노드로부터, 다른 노드(=정해진 특정 노드가 아니어도 됨)까지의 최단 경로 구할 때 용이
"""
def dijkstra(start):
    # 시작 노드 설정
    visited[start] = True
    distance[start] = 0

    for i in graph[start]:
        distance[i[0]] = i[1]

    # 시작 노드 제외한 전체 n - 1개의 노드에 대해서 반복
    for _ in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼냄
        node = get_smallest_node()

        # 방문 처리
        visited[node] = True

        # 현재 노드와 연결된 다른 노드 확인
        for connect_node, cost in graph[node]:
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
            if distance[connect_node] > distance[node] + cost:
                distance[connect_node] = distance[node] + cost


dijkstra(start)


for i in range(1, n + 1):
    print(f"{start} -> {i} : {distance[i]}")


