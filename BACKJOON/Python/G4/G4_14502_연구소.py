# 세로가 n, 가로가 m
import copy
from itertools import combinations

n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
empty_list = []
result = 0
for i in range(n):
    graph[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_list.append([i, j])


def dfs(x, y, z):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < m):
            if z[nx][ny] == 0:
                z[nx][ny] = 2
                dfs(nx, ny, z)
    return


def get_safe(w):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if w[i][j] == 0:
                cnt += 1
    return cnt


def solve():
    global result
    for wall in combinations(empty_list, 3):
        temp = copy.deepcopy(graph)
        for x, y in wall:
            temp[x][y] = 1
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    dfs(i, j, temp)
        result = max(result, get_safe(temp))


solve()
print(result)
