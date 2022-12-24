# TODO
# 제곱해주는 역할
def cal(N, M):
    n = str(N)
    res = 0
    for i in n:
        res += pow(int(i), M)
    return res


def dfs(N, M, iteration, check):
    # 이미 한 번 계산 됬다면, 이제 반복된다고 판단
    if check[N] != 0:
        # print(N)
        return check[N] - 1

    check[N] = iteration
    # print(N)
    daum = cal(N, M)
    iteration += 1
    return dfs(daum, M, iteration, check)


N, M = map(int, input().split())
check = [0] * 236197  # 9 ** 5 + 9 ** 5 + 9 ** 5 + 9 ** 5 최대 인덱스의 값이기 때문
iteration = 1

print(dfs(N, M, iteration, check))
