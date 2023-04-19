"""수도코드
1. 입력받기: 행을 나타내는 n, 열을 나타내는 m, 높이를 나타내는 h / 토마토에 대한 정보는 h만큼 반복해서 받는다.
2. h만큼 graph를 만들어놓고 입력값은 위에서부터 순서대로 주어지니깐 순서대로 graph에 입력값을 넣는걸로
3. bfs 함수 정의
3.1 박스안에서 익은 토마토가 존재하는 좌표라면 queue에 넣어준다. -> 이 익은 토마토의 좌표를 통해 퍼트리는거기 때문에
3.2 다음으로 갈 방향으로 앞전에 설정해놓은 방향 6개를 통해 잡아주고 범위안에 속하며 그 좌표값의 토마토 상태가 익지 않았는지 확인한다
3.3 조건에 만족하면 해당 좌표값을 익었다고 즉 ,1로 바꿔주고 queue에 넣어주고 출력해야하는 총 일수에 걸린 횟수 + 1을 해준다.
3.4 while문을 전부 돌아서 토마토 상태를 바꿨지만 아직 토마토 상태가 안 익은게 있다면 -1을 리턴한다.
"""
from collections import deque


def solution():
    global cnt
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    q.append([i, j, k, 0])

    while q:
        x, y, z, day = q.popleft()
        for dx, dy, dz in direction:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = 1
                cnt = day + 1
                q.append([nx, ny, nz, day + 1])

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return -1
    return cnt


m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
direction = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
cnt = 0
print(solution())
