N = int(input())  # 입력받은 값을 int로 바꿈
num = N  # 변하는 값
count = 0  # 몇 번 사이클인지

while True:
    a = num // 10  # 10으로 나눴을 때 몫
    b = num % 10  # 나머지
    c = (a + b) % 10  # 두 수를 더했을 때의 나머지
    num = (b * 10) + c  # 변하는 값은 b가 먼저오고 c가 1의 자리수가 되기 때문에 b * 10
    count += 1  # 사이클 증가
    if num == N:
        break

print(count)
