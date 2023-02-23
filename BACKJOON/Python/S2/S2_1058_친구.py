import sys

# 사람의 수
n = int(input())
# 입력값을 이중 리스트에 넣기
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 2-친구 사이일 때 1, 아니면 0
f = [[0] * n for _ in range(n)]

# k가 중간에 거쳐가는 노드, i는 출발, j는 도착
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # 2-친구인 경우
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                f[i][j] = 1
result = 0
for _ in f:
    result = max(result, sum(_))

print(result)
