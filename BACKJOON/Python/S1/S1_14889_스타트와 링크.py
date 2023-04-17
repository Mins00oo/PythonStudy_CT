"""수도코드
1. 입력받기: 사람의 수 n, 능력치 s는 이차원 배열로 받기
2.
"""
from itertools import combinations

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
player = [i for i in range(n)]
for _ in range(n):
    graph[_] = list(map(int, input().split()))

print(player)
print(list(combinations(player, 2)))
print(graph)