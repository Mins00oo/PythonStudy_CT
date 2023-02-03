# 테스트 케이스 개수
import sys

input = sys.stdin.readline

t = int(input())
# 메모이제이션으로 값을 넣기 위한 변수
dp = [0] * 1000001
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009


for i in range(t):
    n = int(input())
    print(dp[n])
