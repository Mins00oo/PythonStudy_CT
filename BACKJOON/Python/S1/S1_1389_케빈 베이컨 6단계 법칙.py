import sys
from collections import deque

n, m = map(int, input().split())

# 2차원 그래프를 표현
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 케빈 베이컨의 수를 담는 리스트
res = []


# bfs 탐색
def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()

        # 친구 관계를 확인하고 탐색하지 않은 친구라면 탐색한다.
        for d in graph[target]:
            if visited[d] == 0:
                # 탐색하기 위한 횟수를 체크한다.
                visited[d] = visited[target] + 1
                queue.append(d)


# 반복문을 통해 모든 친구를 탐색한다. 0~n까지 있는데 0번째는 값이 없기에 1부터!
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i)

    # 각각의 방문 횟수를 더해서 res에 추가
    res.append(sum(visited))

# 가장 작은 케빈 베이컨의 수를 가지고 있는 사람의 인덱스 + 1 을 해주어 출력한다. 같은 값이어도 앞의 인덱스가 뽑혀 나온다.
print(res.index(min(res)) + 1)
