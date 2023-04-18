"""수도코드
1. 입력받기: 사람의 수 n, 능력치 s는 이차원 배열로 받기
2.
"""


def dfs(depth, index):
    global res
    if depth == n // 2:
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 1 and visited[j] == 1:
                    a += graph[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    b += graph[i][j]
        res = min(res, abs(a - b))
        return

    for i in range(index, n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
res = 1000000000
visited = [0] * n
dfs(0, 0)
print(res)
