# 학생들의 수, 키를 비교한 횟수
import sys

input = sys.stdin.readline
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

answer = 0
for i in range(n):
    result = 0
    for j in range(n):
        result += graph[i - 1][j - 1] + graph[j - 1][i - 1]
    if result == n - 1:
        answer += 1

print(answer)
