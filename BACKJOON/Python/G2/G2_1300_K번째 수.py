# 배열의 크기 n, k번째 인덱스
n, k = int(input()), int(input())
start, end = 1, n**2
answer = 0
length = 0
while start <= end:
    mid = (start + end) // 2
    temp = 0

    for i in range(1, n + 1):
        temp += min(mid // i, n)

    if temp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
