# 수도코드
# 1. 숫자 5를 전부 6으로 바꿔서 두 수를 합한다면 최댓값이고, 6을 5로 바꾸면 최솟값이 된다.
# 2. replace함수를 사용해서 5를 6으로 6을 5로 바꾸면 된다

# a, b = map(int, input().split())  # 두 정수 a, b가 주어진다
# sum_max = a.replace('5', '6') + b.replace('5', '6')  # 합의 최댓값
# sum_min = a.replace('6', '5') + b.replace('6', '5')  # 합의 최솟값
#
# print(sum_min, sum_max)

a, b = input().split()  # 두 정수 a, b가 주어진다 -> replace 함수는 문자열에서 값을 바꿔주는 역할이라 그런지 문자열로 입력받도록
sum_max = int(a.replace('5', '6')) + int(b.replace('5', '6'))  # 합의 최댓값
sum_min = int(a.replace('6', '5')) + int(b.replace('6', '5'))  # 합의 최솟값

print(sum_min, sum_max)
