# 컴퓨터의 수
from collections import deque

n = int(input())
# 쌍의 개수
m = int(input())
graph = [[] for _ in range(n + 1)]
dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0


# def dfs(start):
#     global cnt
#     dfs_visited[start] = 1
#     for i in graph[start]:
#         if dfs_visited[i] == 0:
#             cnt += 1
#             dfs(i)
#
#
# dfs(1)
# print(cnt)

def bfs(start):
    q = deque()
    q.append(start)
    bfs_visited[start] = 1
    global cnt
    while q:
        d = q.popleft()
        for i in graph[d]:
            if bfs_visited[i] == 0:
                bfs_visited[i] = 1
                cnt += 1
                q.append(i)


bfs(1)
# print(bfs_visited)
print(cnt)
