# t = int(input())  # 테스트 케이스 개수
#
#
# def total(n):  # 0 과 1의 전체 개수를 구하는 함수
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return total(n - 1) + total(n - 2)
#
#
# def sol(n):  # 1의 개수를 구하는 함수
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return sol(n - 1) + sol(n - 2)
#
#
# for _ in range(t):
#     m = int(input())
#     cnt_0 = total(m)
#     cnt_1 = sol(m)
#     print(cnt_0 - cnt_1, cnt_1)  # 전체 개수에서 1의 개수를 빼주면 0의 개수를 알 수 있다.
#
#

t = int(input())

for _ in range(t):
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    n = int(input())
    if n > 1:
        for i in range(n - 1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2] + cnt_1[-1])

    print(cnt_0[n], cnt_1[n])
