"""수도코드
1. 입력받기: 세로의 길이 r, 가로의 길이 c, 다음 줄에서는 이차원 배열안에 기호 값을 넣어준다
2. 각 영역을 탐색하여 늑대와 양의 수를 확인함
2.1 bfs를 사용해서 울타리가 아니고 방문하지 않은 좌표라면 queue에 추가해주면서 반복문 돌림
"""
from collections import deque


def solution(x, y):
    sheep, wolf = 0, 0
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        if graph[x][y] == 'v':
            wolf += 1
        elif graph[x][y] == 'k':
            sheep += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0
    return sheep, wolf


r, c = map(int, input().split())
graph = [[0 for _ in range(c)] for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
result_sheep, result_wolf = 0, 0
for _ in range(r):
    graph[_] = list(map(str, input().rstrip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] in ('v', 'k') and visited[i][j] == 0:
            a, b = solution(i, j)
            result_sheep += a
            result_wolf += b
print(result_sheep, result_wolf)
