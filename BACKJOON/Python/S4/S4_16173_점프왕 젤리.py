n = int(input())  # 구역의 크기
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0]  # 아래, 오른쪽으로 움직였을때의 방향
dy = [0, 1]
visited = [[0] * n for _ in range(n)]


def dfs(x, y):
    if x >= n or x <= -1 or y >= n or y <= -1:  # 범위를 벗어나지 않도록
        return False
    if visited[x][y] == 1:
        return False

    if graph[x][y] == -1:
        print('HaruHaru')
        exit()  # 종료

    visited[x][y] = 1

    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]
        dfs(nx, ny)
    return True


if dfs(0, 0):
    print('Hing')

