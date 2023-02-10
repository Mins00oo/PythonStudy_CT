# n, m = map(int, input().split())  # n은 노드의 개수, m은 서로 연결된 간선의 개수
# graph = [[] * n for _ in range(n + 1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [0] * (n + 1)
# cnt = 0
#
#
# def dfs(start):
#     global cnt
#     visited[start] = 1
#     for d in graph[start]:
#         if visited[d] == 0:
#             cnt += 1
#             dfs(d)
#
#
# dfs(1)
# print(cnt)
# 1차 런타임 에러 발생


# import sys
#
# sys.setrecursionlimit(10 ** 6)
# n, m = map(int, input().split())  # n은 노드의 개수, m은 서로 연결된 간선의 개수
# graph = [[] * n for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [0] * (n + 1)
# cnt = 0
#
#
# def dfs(start):
#     global cnt
#     visited[start] = 1
#     for d in graph[start]:
#         if visited[d] == 0:
#             dfs(d)
#
#
# for i in range(1, n + 1):
#     if visited[i] == 0:
#         cnt += 1
#         dfs(i)
# print(cnt)
# 2차 시간 초과 발생

import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())  # n은 노드의 개수, m은 서로 연결된 간선의 개수
graph = [[] * n for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
cnt = 0


def dfs(start):
    global cnt
    visited[start] = 1
    for d in graph[start]:
        if visited[d] == 0:
            dfs(d)


for i in range(1, n + 1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)
