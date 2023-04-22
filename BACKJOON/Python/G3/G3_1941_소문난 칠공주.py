"""수도코드
1. 입력받기: 문자열을 받을 graph, 상하좌우로 움직일 방향 설정
2. solution 함수 정의
2.1 먼저, dfs를 통해 문자열을 만들어 본 다음에 7개의 문자열이 된다면 인접해있는지 확인한다
-> 인접한 문자열만 넣으려고 하다보면 dfs로는 안되는 부분들이 있을 수 있기 때문에 전부 다 해보면서 가지치기를 한다
2.2 dfs 재귀를 하는 과정에서 임도연파를 세어주는데 만약 4명 이상이 나오면 그 즉시 리턴해주며 가지치기를 한다.
2.3 5*5 이차원 배열로 생각하지 않고 1차원 배열로 생각해서 풀어야해서 행 r은 i // 5, 열 c는 i % 5로 나타낸다.
3. check 함수 정의
3.1 7명의 학생들이 인접한지 확인하기 위해서 방문확인을 위한 visited를 만들어준다
3.2 상하좌우로 탐색하며 범위내에 존재하고 7명의 학생들일때만 cnt+1을 해주면서 최종적으로 cnt가 7일때 True를 리턴하도록 한다.
"""
from collections import deque


def check():
    q = deque()
    q.append(answer[0])
    visited = [[-1 for _ in range(5)] for _ in range(5)]
    for i in answer:
        visited[i[0]][i[1]] = 0
    visited[answer[0][0]][answer[0][1]] = 1
    cnt = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dx[d]
            nc = c + dy[d]
            if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] == 0:
                cnt += 1
                visited[nr][nc] = 1
                q.append([nr, nc])
    if cnt == 7:
        return True
    else:
        return False


def solution(depth, idx, count):
    global result
    if count >= 4:
        return
    if depth == 7:
        if check():
            result += 1
        return
    for i in range(idx, 25):
        r = i // 5
        c = i % 5
        answer.append([r, c])
        solution(depth + 1, i + 1, count + (graph[r][c] == 'Y'))
        answer.pop()


graph = [list(input()) for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []
result = 0
solution(0, 0, 0)
print(result)
