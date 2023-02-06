# 10,007로 나누어서 오르막 수를 구해야하는 길이 n
n = int(input())
num = [1] * 10

for i in range(n - 1):
    for j in range(1, 10):
        num[j] += num[j - 1]

print(sum(num) % 10007)
