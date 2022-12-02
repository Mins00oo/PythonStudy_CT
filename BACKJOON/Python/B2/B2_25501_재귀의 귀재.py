# 수도코드
# 1. 힌트에 있는 파이썬 함수를 활용하기 위해 먼저 가져온다
# 2. 문자열을 입력받은 후 넣어서 검증을 하면 판별은 가능하다
# 3. 횟수를 알기 위해서 세어주기 위한 변수를 생성한다
# 4. 전역변수로 사용하기 위해 global을 붙여주고 1씩 증가시켜준다.
import sys

N = int(input())


def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


# for _ in range(N):
#     cnt = 0
#     S = input()
#     print(isPalindrome(S), cnt)

for _ in range(N):
    cnt = 0
    print(isPalindrome(sys.stdin.readline().rstrip()), cnt)
