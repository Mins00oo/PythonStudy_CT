# 우리의 크기 n
n = int(input())
# n = 0, 1 일 경우 가능한 경우의 수가 1, 3이기 때문에 넣어놓고 나머지는 0으로 초기화
dp = [1, 3] + [0] * (n - 1)
# 2번째 인덱스부터는 규칙에 따라서 값을 바꿔준다
for i in range(2, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1] * 2) % 9901
print(dp[n])
