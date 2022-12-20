import sys

N = int(sys.stdin.readline())
total = [[0 for _ in range(4)] for _ in range(N)]

for i in range(N):
    name, kor, eng, m = sys.stdin.readline().split()
    total[i][0] = name
    total[i][1] = kor
    total[i][2] = eng
    total[i][3] = m

# print(total)

total.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for k in range(len(total)):
    print(total[k][0])
