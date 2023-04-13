"""수도코드
1. 입력받기: n, m과 연구소의 지도 graph
2. graph에 저장하기
3. 세 개의 벽을 세울 수 있는 모든 조합을 찾는다.
3.1 각 조합에 대해서 벽을 세우고
3.2 바이러스를 퍼뜨린다.
3.3 안전 영역을 계산한다.
3.4 원래대로 지도로 다시 계속 반복
4. 이런식으로 최대 크기를 저장하면서 교체해주고 결과 출력
"""

# 세로가 n, 가로가 m
import copy
from itertools import combinations

n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
empty_list = []
result = 0
for i in range(n):
    graph[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_list.append([i, j])


def dfs(x, y, z):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < m):
            if z[nx][ny] == 0:
                z[nx][ny] = 2
                dfs(nx, ny, z)
    return


def get_safe(w):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if w[i][j] == 0:
                cnt += 1
    return cnt


def solve():
    global result
    for wall in combinations(empty_list, 3):
        temp = copy.deepcopy(graph)
        # 벽 세우고
        for x, y in wall:
            temp[x][y] = 1
        for i in range(n):
            for j in range(m):
                # 바이러스 퍼트리기
                if temp[i][j] == 2:
                    dfs(i, j, temp)
        result = max(result, get_safe(temp))


solve()
print(result)
