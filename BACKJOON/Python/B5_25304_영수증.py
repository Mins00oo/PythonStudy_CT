# 수도코드
# 1. 총합 가격부터 개수와 각 물건의 가격과 개수를 입력받는다.
# 2. 조건문을 사용해 물건의 개수*가격을 합한 금액이 총합과 일치하는지 판단한다.

total = int(input())
# 영수증의 총 금액
tc = int(input())
# 물건의 종류의 수
sum = 0
# 각 물건들을 총 합한 금액
for i in range(tc):
    a, b = map(int, input().split())
    sum += a*b
# 물건 종류의 수만큼 각각 금액과 수량을 입력받고 sum에 더해준다.
if total == sum:
    print("Yes")
else:
    print("No")
# 처음 입력받은 영수증의 총 금액과 같다면 Yes, 다르면 No
