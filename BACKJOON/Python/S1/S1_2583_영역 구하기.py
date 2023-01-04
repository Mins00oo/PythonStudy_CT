from collections import deque

m, n, k = map(int, input().split())  # m은 행, n은 열, k는 직사각형의 개수
graph = [[0] * n for _ in range(m)]
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())  # x가 행, y가 열
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1


def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if (0 <= nx < m) and (0 <= ny < n) and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
                cnt += 1
    return cnt


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))
