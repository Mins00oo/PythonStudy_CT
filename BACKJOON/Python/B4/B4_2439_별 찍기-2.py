# N = int(input())  # 마지막 줄에 찍어야하는 총 별의 개수
# for i in range(1, N + 1):
#     print(' ' * (N - i), '*' * i)

N = int(input())  # 마지막 줄에 찍어야하는 총 별의 개수
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)
