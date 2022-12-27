import sys

n = int(input())  # 길이
sys.setrecursionlimit(100000)

graph = [list(map(str, input())) for _ in range(n)]  # 색맹 아닌 사람이 볼 좌표평면
temp_graph = graph  # 색맹인 사람을 위한 좌표평면

not_weak_visited = [[0] * n for _ in range(n)]  # 색맹이 아닌사람
weak_visited = [[0] * n for _ in range(n)]  # 색맹인 사람

not_weak_cnt = 0  # 색맹이 아닌사람
weak_cnt = 0  # 색맹인 사람

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def not_weak_dfs(x, y):  # 색맹이 아닌 사람일 경우
    not_weak_visited[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if not_weak_visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:  # 방문하지 않은 노드 + 같은 색인지 확인
                not_weak_dfs(nx, ny)


def weak_dfs(x, y):  # 색맹일 사람의 경우
    weak_visited[x][y] = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if weak_visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                weak_dfs(nx, ny)


for i in range(n):  # 색맹이 아닌 사람일 경우
    for j in range(n):
        if not_weak_visited[i][j] == 0:
            not_weak_dfs(i, j)
            not_weak_cnt += 1

for i in range(n):  # 색맹인 사람일 경우, temp_graph를 사용하는데 초록색을 전부 빨간색으로 변경한 후 dfs 적용
    for j in range(n):
        if temp_graph[i][j] == 'G':
            temp_graph[i][j] = 'R'

for i in range(n):  # 색맹인 사람일 경우, dfs 시작
    for j in range(n):
        if weak_visited[i][j] == 0:
            weak_dfs(i, j)
            weak_cnt += 1


print(not_weak_cnt, weak_cnt)
