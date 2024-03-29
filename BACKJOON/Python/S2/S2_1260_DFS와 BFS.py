from collections import deque

n, m, v = map(int, input().split())  # n은 정점, m은 간선의 수, v는 시작 번호
graph = [[] for _ in range(n + 1)]
dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)
dfs_result = []
bfs_result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    dfs_visited[start] = 1
    dfs_result.append(start)

    for i in sorted(graph[start]):
        if dfs_visited[i] == 0:
            dfs(i)


def bfs(start):
    bfs_visited[start] = 1
    bfs_result.append(start)
    q = deque()
    q.append(start)

    while q:
        d = q.popleft()
        for i in sorted(graph[d]):
            if bfs_visited[i] == 0:
                bfs_visited[i] = 1
                bfs_result.append(i)
                q.append(i)


dfs(v)
print(*dfs_result)
bfs(v)
print(*bfs_result)
