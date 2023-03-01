# 정점의 개수 n, 간선의 개수 m
import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
inf = 1000000000
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [inf] * (n + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(heap, (dist + i[1], i[0]))
    return distance


start_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

# 1 -> v1 -> v2 하고 1 -> v2 -> v1 둘 다 고려해야한다
v1_path = start_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = start_distance[v2] + v2_distance[v1] + v1_distance[n]

res = min(v1_path, v2_path)
print(res if res < inf else -1)
