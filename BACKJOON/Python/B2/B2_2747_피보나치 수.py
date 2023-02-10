# 구해야 할 n번째 피보나치 수
n = int(input())
# 메모이제이션을 활용해 기본 값 미리 저장
dp = [0, 1]

for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[n])
