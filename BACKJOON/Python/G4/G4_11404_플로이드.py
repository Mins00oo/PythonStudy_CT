# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())
INF = 1000000000
graph = [[INF] * n for _ in range(n)]
for i in range(m):
    s, e, c = map(int, input().split())
    if graph[s - 1][e - 1] > c:
        graph[s - 1][e - 1] = c

# 거쳐가야 하는 노드
for k in range(n):
    # 출발점
    for a in range(n):
        # 도착점
        for b in range(n):
            if a == b:
                graph[a][b] = 0
            if graph[a][b] > graph[a][k] + graph[k][b] and a != b:
                graph[a][b] = graph[a][k] + graph[k][b]

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

for _ in graph:
    print(*_)
