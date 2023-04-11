"""수도 코드이차원 배열을
1. n, m 입력받고 그만큼 이차원 배열을 생성해준다. 그러고 좌표 r,c 방향 d를 입력받고 그 다음줄에는 이차원 배열에 값을 넣는다.
2. (r,c) 좌표값이 0이면 cnt + 1을 해준다.
3. 그런다음, 상하좌우 탐색해서 0이 있다면, 현재 방향 d에서 왼쪽으로 튼다. 만약 그렇게 회전해서 0이면 그 칸으로 이동
4. 만약 0이 없다면, 현재 방향 d에서 후진한 칸이 1인지 탐색
4.1 1이라면 작동을 멈춤
4.2 1이 아니라면 좌표를 이동하고 좌표값이 0인지 본다.
4.3 애초에 상하좌우에 0이 하나도 없다는건 후진을 할 수 없다는게 아닌가 ? 그럼 작동 중지

"""

n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
r, c, d = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for _ in range(n):
    graph[_] = list(map(int, input().split()))


def clean(x, y, d):
    global cnt
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1
    # 4칸을 전부 탐색해보면서 청소할 수 있는지 확인해보고 재귀
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if graph[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    # 4칸중 청소되지 않은 칸이 없는 경우
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    # 후진했는데 그 벽도 1이면 종료
    if graph[nx][ny] == 1:
        return
    clean(nx, ny, d)


clean(r, c, d)
print(cnt)
