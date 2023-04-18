"""수도코드
1. 입력받기: n, m 그리고 숫자 1부터 n까지 받는다
2. 백트래킹 함수 정의
2.1 처음에 1을 넣고 재귀를 통해 나머지 값들을 넣어주면서 길이가 m가 같을때마다 answer을 출력하게 한다.
2.2 재귀에서 빠져나오면 pop을 통해 넣은 값을 제거한다.
"""


def solution():
    if len(answer) == m:
        print(*answer)
        return
    for i in range(1, n + 1):
        answer.append(i)
        solution()
        answer.pop()
    return


n, m = map(int, input().split())
answer = []
num = [i for i in range(1, n + 1)]
solution()
