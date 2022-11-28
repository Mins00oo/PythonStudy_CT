# 수도코드 작성
# 1. 두 수를 서로 띄워서 입력받는다
# 2. 실수형으로 변환시켜준다
# 3. 각 줄에 해당하는 연산을 출력시킨다.

a, b = map(int, input().split())
# split의 결과를 모두 int형으로 변환시키기 위해 작성

print(a+b)
# 덧셈
print(a-b)
# 뺄셈
print(a*b)
# 곱셈
print(a//b)
# 몫
print(a%b)
# 나머지
