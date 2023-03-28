t = int(input())
t_li = [int(input()) for _ in range(t)]
dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in t_li:
    for j in range(6, i + 1):
        dp[j] = dp[j - 5] + dp[j - 1]

    print(dp[i])
