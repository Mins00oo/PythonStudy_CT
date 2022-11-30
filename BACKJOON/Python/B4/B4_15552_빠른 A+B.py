# 수도코드
# 1. 테스트케이스의 개수를 입력받는다.
# 2. 개수만큼 반복하여 두 정수를 입력받고 합을 출력한다.
import sys

cnt = int(input())
# 테스트케이스의 개수를 입력받음

for i in range(cnt):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
# 두 정수를 입력받은 후 합을 출력
