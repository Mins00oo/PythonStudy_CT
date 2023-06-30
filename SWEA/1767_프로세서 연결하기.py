def length_wire(cores):
    total = 0


def dfs(depth, cnt):
    global ans, ans_total
    if depth >= core_len:
        if cnt > ans:
            ans = cnt
        return
    x, y, z = core[depth]
    if core[depth][2] == 5:
        dfs(depth + 1, cnt + 1)
    else:
        dfs(depth + 1, cnt)


t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[list(map(int, input().split()))] for _ in range(n)]
    core = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    core.append([i, j, 5])
                else:
                    core.append([i, j, - 1])
    core_len = len(core)
    ans = ans_total = 0
    dfs(0, 0)
