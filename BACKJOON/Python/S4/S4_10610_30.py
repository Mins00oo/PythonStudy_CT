# 수도코드
# 1. 양수 N을 구성하는 숫자들을 섞어서 30의 배수가 되는 최댓값을 구해야한다
# 2. 30의 배수가 되려면 우선 양수 N에서 0이 없다면 30의 배수가 아니므로 -1을 출력하면 된다.
# 3. 0이 있다면 제일 오른쪽으로 우선 빼놓고 나머지 수들의 합이 3의 배수인지 확인한다.
# 4. 3의 배수가 아니라면 -1을 출력하고 3의 배수라면 나머지 수들을 내림차순 정렬해서 수를 구성한다.

N = input()  # 숫자 N을 입력받는다
li = []  # 숫자 N을 구성하는 숫자들을 쪼개서 담을 공간

for i in N:
    li.append(i)  # li에 담는다
# print(li)

cnt_zero = li.count('0')  # 0의 개수를 세어본다
# print(cnt_zero)

N_sum = 0  # N을 구성하는 숫자들의 합

for j in N:
    N_sum += int(j)

if cnt_zero == 0:  # 0이 하나도 없다면 -1을 출력
    print(-1)
elif N_sum % 3 != 0:  # N을 구성하는 수들을 합해서 3으로 나눈 나머지가 0이 아니라면 -1을 출력
    print(-1)
else:
    li.sort(reverse=True)
    print(''.join(li))  # join 함수를 이용해 문자열을 합쳐서 출력
# print(N_sum)
