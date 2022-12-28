import sys

input = sys.stdin.readline


def comb(a, b):
    if a == 6:
        print(*order)
        return
    for i in range(b, k):
        order.append(lottos[i])
        comb(a + 1, i + 1)  # 재귀
        order.pop()  # 제거해가면 백트래킹 , 전 단계로 돌아감


while True:
    lottos = list(map(int, input().split()))
    k = lottos.pop(0)

    if not lottos:
        break

    order = []
    comb(0, 0)
    print()
