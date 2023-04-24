"""수도코드
1. 입력받기: 행의 개수 n, 열의 개수 m, 초록 배양액 g개, 빨간 배양액 r개
2. 주어지는 값에 따라 2차원 배열에 해당하는 값을 넣어서 생성 (0은 호수, 1은 배양이 불가능한 땅, 2는 배양이 가능한 땅)
3. 입력받은 그래프 값 중 배양액을 뿌리기 위해 값이 2인 좌표들을 전부 가져오고 뿌려야 하는 개수만큼 조합을 한다
4.

"""
import copy
from collections import deque
from itertools import combinations


def solution(arr, selected, green_li):
    print(green_li)
    green_q = deque()
    red_q = deque()
    for row, col in selected:
        if [row, col] in green_li:
            green_q.append([row, col])
            graph[row][col] = 3
        else:
            red_q.append([row, col])
            graph[row][col] = 4

    while green_q:
        green_temp = set()
        red_temp = set()
        while green_q:
            x, y = green_q.popleft()
            graph[x][y] = 3
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 or graph[nx][ny] == 2:
                        green_temp.add((nx, ny))

        while red_q:
            x, y = red_q.popleft()
            graph[x][y] = 4
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 or graph[nx][ny] == 2:
                        red_temp.add((nx, ny))


n, m, g, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = []
dx = [-1, 1, 0, 0]
answer = 0
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            temp.append([i, j])
for c in list(combinations(temp, (g + r))):
    for green in list(combinations(c, g)):
        copy_graph = copy.deepcopy(green)
        solution(copy_graph, c, green)
