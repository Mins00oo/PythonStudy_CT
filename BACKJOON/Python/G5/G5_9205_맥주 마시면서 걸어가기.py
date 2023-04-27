"""수도코드
1. 입력받기: 테스트 케이수 개수 t, 편의점 개수 n, 상근이의 집, 편의점, 목적지 좌표가 주어진다.
2. bfs 함수정의
2.1 x, y 각각 현재 위치에서 이동한 좌표를 세어주어야 하고 갈 수 있는 최대거리는 1000이다
2.2 시작점을 큐에 담고 다음 편의점까지 갈 수 있는지 확인해준다. 그러기 위해 방문 확인을 하고 편의점의 좌표를 가져와 비교한다
2.3 현재 위치에서 편의점 좌표까지 x y 값이 1000이하면 갈 수 있기에 방문확인을 해주고 큐에 넣어준다.
2.4 만약 편의점에 갈 필요없이 목적지까지 현재 위치에서 바로 갈 수 있다면 happy를 출력하기에 먼저 가지치기를 해준다.
"""
from collections import deque


def solution():
    q = deque()
    q.append([x, y])
    while q:
        nx, ny = q.popleft()
        if abs(nx - fx) + abs(ny - fy) <= 1000:
            print('happy')
            return
        for d in range(n):
            if not visited[d]:
                dx, dy = graph[d]
                if abs(nx - dx) + abs(ny - dy) <= 1000:
                    visited[d] = 1
                    q.append([dx, dy])
    print('sad')
    return


t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    visited = [0] * n
    solution()
