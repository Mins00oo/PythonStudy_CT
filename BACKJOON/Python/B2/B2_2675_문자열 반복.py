# 수도코드
# 1. 횟수와 문자열을 각각 입력받는다. 이때 횟수도 문자열형으로 받았기 때문에 나중에 정수형으로 변환해준다.(a만큼 곱해줘야해서)
# 2. 문자열을 반복하면서 빈 문자열에 a만큼 하나씩 채워나가는 느낌으로 푼다.

T = int(input())

for _ in range(T):
    a, b = map(str, input().split())  # a는 횟수, b는 문자열
    x = ''
    for i in b:  # for문을 통해 문자열을 하나씩 반복해서 출력하는데 횟수만 a를 정수형으로 변환해서
        x += int(a) * i  # a만큼 문자열을 반복해서
    print(x)  # 출력시킨다
