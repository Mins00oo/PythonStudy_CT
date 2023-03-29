n = int(input())

wine = []

for i in range(n):
    wine.append(int(input()))

wine.insert(0, 0)
dp = [0 for _ in range(n)]

dp[1] = wine[1]
if n > 1:
    dp[2] = wine[1] + wine[2]

if n > 2:
    dp[3] = max(wine[3] + wine[2], wine[3] + wine[1], dp[2])

for i in range(4, n):
    dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])

print(dp[n - 1])
