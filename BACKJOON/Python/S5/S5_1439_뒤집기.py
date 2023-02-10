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

s = list(input())  # 문자열 입력받아서 list에 저장
count: int = 0

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:  # 다음 문자열이 다른지 확인해서 다르면 count를 1씩 증가
        count += 1

print((count + 1) // 2)  # +1을 해서 2로 나눈 몫을 출력해야한다
