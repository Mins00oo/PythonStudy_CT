from collections import deque

n, k = map(int, input().split())  # n은 수빈이의 현재 위치, k는 동생의 위치
visited = [0] * 100001  # 최대 개수만큼 방문할 곳을 0으로 생성
q = deque()
q.append(n)


def bfs():
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            exit()
        for i in (x - 1, x + 1, x * 2):
            if (0 <= i <= 100001) and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)


bfs()
