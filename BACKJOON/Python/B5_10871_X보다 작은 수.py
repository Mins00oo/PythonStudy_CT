# 수도코드
# 1. 전체 개수 N과 기준점 X, 두 수를 입력받는다.
# 2. 전체 값들을 입력받고 list에 담는다.
# 3. 전체 개수만큼 반복문을 통해 기준보다 작으면 출력하도록 한다.

a, b = map(int, input().split())
# 두 수를 입력받는다.
num = list(map(int, input().split()))
# 전체 개수만큼 값을 입력받고 list에 담기
for i in range(a):
    if num[i] < b:
        print(num[i], end= " ")
# 반복문을 통해 조건을 설정해 값보다 작을 시 공백을 두고 출력하도록 한다.