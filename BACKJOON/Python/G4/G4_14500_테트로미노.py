"""수도코드
1. 세로 n, 가로 m만큼 입력받고 그에 맞게 입력값들을 이차원 배열로 입력받는다.
2. 문제 풀이는 dfs로 해본다.
2.1 탐색 시작점으로부터 3번까지만 탐색한다.
2.2 탐색은 상하좌우 방향으로 이루어진다.
3. visited로 방문했던곳인지 확인을 해줘야하다!
3.1 visited는 graph의 크기만큼 똑같이 만들어서 전부 0으로 채워넣고 방문했다면 1로 바꾼다.
3.2 하지만 dfs함수를 나오고 나서는 다시 visited를 0으로 바꿔놓는다. -> 다른 dfs 탐색에서는 또 쓰일 수 있기 때문에
3.3 현재의 dfs에서 나머지 탐색까지 전부 최댓값으로 더한다고 가정해도 result를 넘지 못한다면 더 탐색할 필요가 없기 때문에 중단
4. 중요한 점은 ㅗ 모양을 제외하고는 전부 일반 dfs로 되지만 ㅗ 모양은 새로운 nx, ny에서 탐색하지 않는다.
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    graph[_] = list(map(int, input().split()))

result = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
max_graph = max(map(max, graph))


def dfs(x, y, cnt, total):
    global result
    # 최댓값으로 가정하고 더해도 result를 넘지 못한다면 그냥 dfs 중단
    if result >= total + max_graph * (3 - cnt):
        return
    if cnt == 3:
        result = max(result, total)
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if cnt == 1:
                visited[nx][ny] = 1
                dfs(x, y, cnt + 1, total + graph[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, total + graph[nx][ny])
            visited[nx][ny] = 0


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = 0

print(result)
