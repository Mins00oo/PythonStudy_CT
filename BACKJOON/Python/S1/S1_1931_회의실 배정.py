n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: a[0])  # 시작 시간을 먼저 정렬
s = sorted(s, key=lambda a: a[1])  # 종료 시간을 그 다음으로 정렬

# print(s)
last = 0
cnt = 0
for i, j in s:
    # print("i:", i)
    # print("j:", j)
    if i >= last:
        cnt += 1
        last = j
print(cnt)
