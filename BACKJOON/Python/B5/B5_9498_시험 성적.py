# 수도코드
# 1. 성적을 입력받는다.
# 2. 입력받은 점수에 따라 조건문을 설정하여 출력값을 지정해준다.

score = int(input())
# 성적값 입력받는다

if score >= 90:
    print('A')
    # 90점 이상이면 A
elif score >= 80:
    print('B')
    # 80~89점은 B
elif score >= 70:
    print('C')
    # 70~79점은 C
elif score >= 60:
    print('D')
    # 60~69점은 D
else:
    print('F')
    # 그 외에 점수는 F
