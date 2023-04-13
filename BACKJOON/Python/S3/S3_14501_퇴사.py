"""수도코드
1. 입력받기: n은 상담기간, p는 이익을 담은 리스트 t와 p
2. 백트래킹 함수 정의하기 (현재 날짜, 현재 이익)
2.1 현재 날짜가 n + 1이면 최대 이익을 갱신해주고 종료
2.2 상담을 할 수 있는지 즉, 현재 날짜 + 걸리는 기간
"""


def backtrack(day, profit):
    global max_profit

    if day == N + 1:
        max_profit = max(max_profit, profit)
        return

    if day + T[day] <= N + 1:
        backtrack(day + T[day], profit + P[day])

    if day + 1 <= N + 1:
        backtrack(day + 1, profit)


# 입력 받기
N = int(input())
T, P = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

max_profit = 0
backtrack(1, 0)

print(max_profit)
