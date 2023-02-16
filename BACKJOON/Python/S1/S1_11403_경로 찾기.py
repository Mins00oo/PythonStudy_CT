# 정점의 개수 n
n = int(input())
# 그래프
graph = []
# 좌표 입력받기
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [0 * n for _ in range(n)]


def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


for m in range(n):
    dfs(m)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for _ in range(n)]
