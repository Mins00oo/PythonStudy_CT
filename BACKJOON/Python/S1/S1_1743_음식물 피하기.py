"""수도코드
1. 입력받기: n행, m열, 음식물 쓰레기 개수 k
2. 함수정의(bfs)
2.1 그래프를 탐색하면서 값이 '#'이 나오면 함수를 실행
2.2 함수실행시 받은 x,y좌표는 방문체크해주고 큐에 넣어준다.
2.3 큐를 반복하면서 값을 꺼내고 상하좌우로 판단하면서 값이 '#'인지 확인하고 맞으면 cnt+1 해주고 방문체크해준후에 큐에 넣는다
2.4 끝나면 cnt를 리턴한다
3. 함수 종료시 cnt를 받을 변수 생성해주고 최댓값을 출력해야하므로 큰 값이 리턴되면 그 값으로 바꿔주도록 한다.
"""
import sys
from collections import deque


def solution(x, y):
    visited[x][y] = 1
    q = deque()
    cnt = 0
    q.append([x, y])
    cnt += 1
    while q:
        nx, ny = q.popleft()
        for d in range(4):
            ndx = nx + dx[d]
            ndy = ny + dy[d]
            if 0 <= ndx < n and 0 <= ndy < m and graph[ndx][ndy] == '#' and visited[ndx][ndy] == 0:
                cnt += 1
                visited[ndx][ndy] = 1
                q.append([ndx, ndy])
    return cnt


input = sys.stdin.readline
n, m, k = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
graph = [['.' for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = '#'

for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            res = solution(i, j)
            if res >= answer:
                answer = res

print(answer)
