"""수도코드
1. 입력받기: 스카이 콩콩의 힘 a, b 동규의 위치 n, 주미의 위치 m
2. bfs함수 정의
2.1 노드에 위치하면 갈 수 있는 방법은 8가지 이므로 queue에 각 연산을 해서 넣어준다,
2.2 반복해서 popleft한 후, 계속 넣어주는데 주미의 위치가 있다면 그만둔다.
2.3 이동 횟수를 세어야 하므로 while문에서 queue에 넣어줄 때 +1을 해준다.
"""
from collections import deque


def solution(start):
    q = deque()
    q.append(start)
    graph[start] = 0

    while q:
        l = q.popleft()
        for i in (l - 1, l + 1, l - a, l + a, l - b, l + b, l * a, l * b):
            if 0 <= i <= 100000 and graph[i] == -1:
                q.append(i)
                graph[i] = graph[l] + 1
                if i == m:
                    print(graph[m])
                    exit()


a, b, n, m = map(int, input().split())
graph = [-1] * 100001
solution(n)
