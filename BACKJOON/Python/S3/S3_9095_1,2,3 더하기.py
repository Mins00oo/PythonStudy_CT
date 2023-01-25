# n = 1일 경우 1개, n = 2일 경우 2개, n = 3일 경우 4개, n = 4일 경우 7개, n = 5일 경우 13개
# n이 3보다 큰 경우부터는 f(n-1) + f(n-2) + f(n-3) = f(n)
t = int(input())  # 테스트 케이스 개수


def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n - 1) + sol(n - 2) + sol(n - 3)


for i in range(t):
    n = int(input())
    print(sol(n))
