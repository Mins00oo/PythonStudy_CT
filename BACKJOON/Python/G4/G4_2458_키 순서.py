# 학생들의 수, 키를 비교한 횟수
n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1


print(graph)
