import sys

sys.setrecursionlimit(10000)  # 런타임 에러 방지용

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())


def dfs(x, y):
    # 상,하,좌,우 확인
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if (0 <= nx < N) and (0 <= ny < M):
            if matrix[nx][ny] == 1:  # 상 하 좌 우 탐색하면서 1이 있으면 
                matrix[nx][ny] = -1  # -1로 변경해놓기
                dfs(nx, ny)


for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    cnt = 0

    # 행렬 생성
    for _ in range(K):
        m, n = map(int, input().split())
        matrix[n][m] = 1

    for i in range(N):  # 행 (바깥 리스트)
        for j in range(M):  # 열 (내부 리스트)
            if matrix[i][j] == 1:  # 1일때 dfs 탐색 시작
                dfs(i, j)  # 상하좌우 탐색해서
                cnt += 1

    print(cnt)
