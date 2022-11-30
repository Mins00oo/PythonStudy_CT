# 수도코드
# 1. 좌표값 x, y 두 값을 입력받는다.(실수형 변환)
# 2. 값들의 부호에 따라 사분면이 달라지기 때문에 조건문을 통해 사분면 출력

x = float(input())
y = float(input())

if x > 0 and y > 0:
    print('1')
    # x,y: 양수
elif x < 0 and y > 0:
    print('2')
    # x:음수, y:양수
elif x < 0 and y < 0:
    print('3')
    # x,y: 음수
else:
    print('4')
