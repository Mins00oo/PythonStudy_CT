from collections import deque

m, n = map(int, input().split())  # n은 행, m은 열
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]  # 상 하 좌 우 이동했을때
dy = [0, 0, -1, 1]
q = deque([])  # 좌표를 넣을거기 때문에 []로
result = 0  # 정답을 담을 변수

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])


def bfs():
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])


bfs()
for i in graph:
    for j in i:
        if j == 0:  # 익히지 못한 토마토가 있다면
            print(-1)
            exit()
    result = max(result, max(i))

print(result - 1)
