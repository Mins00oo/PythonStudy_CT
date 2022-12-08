# import sys
#
# S = sys.stdin.readline().rstrip()
# z_cnt = 0
#
# for i in S:
#     if i == '0':
#         z_cnt += 1
#
# if len(S) == z_cnt or z_cnt == 0:
#     print(0)
#
# todo
S = input()
count = 0

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:  # 현재 문자와 다음 문자열이 다르면 +1 을 해준다
        count += 1

print((count + 1) // 2)
