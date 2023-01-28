t = int(input())  # 테스트 케이스 개수


def total(n):  # 0 과 1의 전체 개수를 구하는 함수
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return total(n - 1) + total(n - 2)


def sol(n):  # 1의 개수를 구하는 함수
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sol(n - 1) + sol(n - 2)


for _ in range(t):
    m = int(input())
    print(total(m) - sol(m), sol(m))  # 전체 개수에서 1의 개수를 빼주면 0의 개수를 알 수 있다.
