import sys

sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())  # 노드의 개수

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = []

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = start  # 방문한 노드에는 부모 노드의 번호를 적어놓는다
            dfs(i)


dfs(1)
for j in range(2, n + 1):
    print(visited[j])

