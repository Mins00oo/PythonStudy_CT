# n = int(input())  # 전체 사람의 수
# a, b = map(int, input().split())  # 촌수를 계산해야 하는 두 사람
# m = int(input())  # 부모 자식간의 관계 수
#
# graph = [[] * n for _ in range(n + 1)]  # 2차원 배열 그래프 선언
# visited = [0] * (n + 1)  # 방문했는지 확인을 위해
# result = []
# cnt = 0
#
# for i in range(m):  # 입력값들 추가
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)
#
#
# def dfs(start):
#     global cnt
#     cnt += 1
#     visited[start] = 1
#
#     if start == b:
#         result.append(cnt)
#
#     for d in graph[start]:
#         if visited[d] == 0:
#             dfs(d)
#
#
# dfs(a)
# if len(result) == 0:
#     print(-1)
# else:
#     print(result[0] - 1)
#  틀린 답

n = int(input())  # 전체 사람의 수
a, b = map(int, input().split())  # 촌수를 계산해야 하는 두 사람
m = int(input())  # 부모 자식간의 관계 수

graph = [[] * n for _ in range(n + 1)]  # 2차원 배열 그래프 선언
visited = [0] * (n + 1)  # 방문했는지 확인을 위해
result = []

for i in range(m):  # 입력값들 추가
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(start, cnt):
    cnt += 1
    visited[start] = 1

    if start == b:
        result.append(cnt)

    for d in graph[start]:
        if visited[d] == 0:
            dfs(d, cnt)


dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
