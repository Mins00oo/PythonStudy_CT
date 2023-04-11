"""수도코드
1. 입력값을 넣어주는데 범위가 커서 sys.stdin으로 받아준다.
2. 반복문을 통해 한 시험관씩 총 감독관이 가능한 수 만큼 빼주고 cnt를 1씩 증가시켜준다.
2.1 만약 빠진 뒤 값이 0보다 작거나 같으면 다음 값으로 넘어간다.
2.2 남은 값이 감독가능한 수 c보다 작거나 같으면 cnt를 1씩 증가시키고 값을 0으로 만든다.
2.3 그 외에는 c만큼 빼주면서 cnt에는 몫 + 1을 해준다.
"""
import sys

n = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
cnt = 0

for i in range(n):
    student[i] -= b
    cnt += 1
    if student[i] <= 0:
        continue
    while student[i] > 0:
        a = student[i] // c
        if student[i] <= c:
            cnt += 1
            student[i] = 0
        else:
            cnt += a
            student[i] -= a * c

print(cnt)
