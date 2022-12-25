import sys

sys.setrecursionlimit(10 ** 6)
one = [-1, 1, 0, 0, 1, 1, -1, -1]
two = [0, 0, -1, 1, 1, -1, 1, -1]


def dfs(a, b):
    graph[a][b] = -1

    for i in range(8):  # 상하좌우와 대각선 방향까지
        if 0 <= a + one[i] < y and 0 <= b + two[i] < x:
            if graph[a + one[i]][b + two[i]] == 1:
                dfs(a + one[i], b + two[i])
    return


while True:
    x, y = map(int, sys.stdin.readline().split())

    if x == 0 and y == 0:
        break

    graph = []
    count = 0

    for _ in range(y):
        line = list(map(int, sys.stdin.readline().split()))
        graph.append(line)

    for t in range(y):
        for r in range(x):
            if graph[t][r] == 1:
                dfs(t, r)
                count += 1

    print(count)
