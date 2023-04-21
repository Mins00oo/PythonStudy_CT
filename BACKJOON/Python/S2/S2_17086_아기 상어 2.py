"""수도코드
1. 입력받기: 행 n과 열 m 그리고 그에 따라 값을 입력받을 공간 graph, 방문체크를 위한 visited, 8가지 방향을 설정할 리스트
2. bfs 함수정의
2.1 좌표값이 1인 좌표들만 큐에 넣어놓고 함수안에서는 그 좌표값들로 다른 0인 좌표들을 +1을 해주면서 반복
2.3 출력할때는 최댓값 -1을 해준다. 처음 시작을 1로 하기 때문에
"""
from collections import deque


def solution():
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    q.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
answer = 0
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

solution()
print(max(map(max, graph)) - 1)
