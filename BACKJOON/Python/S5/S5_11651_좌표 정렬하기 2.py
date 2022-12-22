import sys

N = int(input())  # 점의 개수
li = [[0 for _ in range(2)] for _ in range(N)]

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    li[i][0] = a
    li[i][1] = b
li.sort(key=lambda x: (x[1], x[0]))  # y좌표 먼저 오름차순 정렬 후 x좌표 정렬
for k in range(len(li)):  # k 0 ~ 3까지
    print(li[k][0], li[k][1])
