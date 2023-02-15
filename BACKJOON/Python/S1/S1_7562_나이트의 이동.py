# 테스트 케이스 개수
from collections import deque

t = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(a, b, c, d):
    # a, b, c, d 순서대로 현재 x, y좌표 / 목표 x, y 좌표
    q = deque([a, b])
    s[a][b] = 1


for _ in range(t):
    # 체스판 한 변의 길이 (4 <= i <= 300) 체스판은 정사각형
    i = int(input())
    # 현재 좌표
    nx, ny = map(int, input().split())
    # 도달해야하는 좌표
    tx, ty = map(int, input().split())
    s = [[0] * i for _ in range(i)]
