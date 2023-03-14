# 오영석이 가지고 있는 랜선 k개, 만들어야 하는 랜선의 개수 n개
k, n = map(int, input().split())
k_len = []

for _ in range(k):
    k_len.append(int(input()))

start, end = 1, max(k_len)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in k_len:
        lines += i // mid
    # 랜선이 목표 랜선 개수의 이상이면 mid + 1을 시작점으로 두고 반복
    if lines >= n:
        start = mid + 1
    # 랜선이 목표 랜선 개수보다 적으면 mid - 1을 끝점으로 두고 반복
    else:
        end = mid - 1

print(end)
