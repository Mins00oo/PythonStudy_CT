import heapq

# 지름길의 개수 n, 고속도로의 길이 k
n, k = map(int, input().split())
road = [[] for _ in range(k + 1)]
INF = 1000000000
dist = [INF for _ in range(k + 1)]
for _ in range(n):
    # 출발 노드 a, 도착 노드 b, 거리 c
    a, b, c = map(int, input().split())
    if b <= k:
        road[a].append([b, c])
for i in range(k):
    road[i].append([i + 1, 1])


def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    dist[start] = 0
    while heap:
        d, now = heapq.heappop(heap)

        if dist[now] != d:
            continue

        for j in road[now]:
            cost = d + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost
                heapq.heappush(heap, [cost, j[0]])


dijkstra(0)
print(dist[k])
