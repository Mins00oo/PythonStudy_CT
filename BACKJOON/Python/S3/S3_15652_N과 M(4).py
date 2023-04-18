"""수도코드
1. 백트래킹 함수 정의
1.1 인덱스 값을 나타내기 위해 start를 함수에 받아준다
1.2 i가 2일때는 반복문이 2 ~ 4까지 , i가 3일때는 3 ~ 4까지 반복하면서 재귀를 반복하기 때문에 인덱스값만 조정해준다.
"""


def solution(start):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(start, n + 1):
        answer.append(i)
        solution(i)
        answer.pop()
    return


n, m = map(int, input().split())
answer = []
num = [i for i in range(1, n + 1)]
solution(1)
