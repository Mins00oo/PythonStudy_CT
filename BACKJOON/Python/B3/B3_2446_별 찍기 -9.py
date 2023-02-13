# n번째 줄까지 규칙을 찾기 위함
n = int(input())
# 규칙은 첫 줄부터 9개, 7개 이렇게 줄어나가고 빈칸을 i값만큼 더해주면 된다
for i in range(n):
    print(" " * i + "*" * ((n - i) * 2 - 1))
for i in range(n - 2, -1, -1):
    print(" " * i + "*" * ((n - i) * 2 - 1))
