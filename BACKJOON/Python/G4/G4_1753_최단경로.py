# 정점의 개수 v, 간선의 개수 e
import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# 시작정점
s = int(input())
# 그래프
INF = 1000000000
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


def dijkstra(start):
    heap = []
    # 시작 정점에 해당하는 곳은 0
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(heap, (dist + i[1], i[0]))


dijkstra(s)

for _ in range(1, n + 1):
    if distance[_] == 1000000000:
        print("INF")
    else:
        print(distance[_])
