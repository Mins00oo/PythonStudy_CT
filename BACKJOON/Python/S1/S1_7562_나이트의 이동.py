# 테스트 케이스 개수
from collections import deque

t = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(st_x, st_y, tar_x, tar_y):
    # a, b, c, d 순서대로 현재 x, y좌표 / 목표 x, y 좌표
    q = deque()
    q.append([st_x, st_y])
    s[st_x][st_y] = 1
    while q:
        a, b = q.popleft()
        if a == tar_x and b == tar_y:
            print(s[tar_x][tar_y] - 1)
            return
        for d in range(8):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0 <= nx < i and 0 <= ny < i and s[nx][ny] == 0:
                q.append([nx, ny])
                s[nx][ny] = s[a][b] + 1


for _ in range(t):
    # 체스판 한 변의 길이 (4 <= i <= 300) 체스판은 정사각형
    i = int(input())
    # 현재 좌표
    nx, ny = map(int, input().split())
    # 도달해야하는 좌표
    tx, ty = map(int, input().split())
    s = [[0] * i for _ in range(i)]
    bfs(nx, ny, tx, ty)
