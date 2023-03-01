# 노드의 개수 n, 간선의 수 m
import heapq

n, m = map(int, input().split())
# 간선 정보
graph = [[] for _ in range(n + 1)]
inf = 1000000000
distance = [inf for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

s, t = map(int, input().split())


def dijkstra(start):
    heap = []
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
print(distance[t])
