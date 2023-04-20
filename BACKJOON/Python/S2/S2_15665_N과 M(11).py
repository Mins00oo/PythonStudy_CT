"""수도코드
1. 입력받기: n, m 그리고 숫자 리스트는 정렬해서 받는다.
2. 함수정의
2.1 반복해서 계속 answer에 넣어주고 재귀를 걸어주는데 중복이 되면 안되므로 append한 값을 check에 넣어놓고 반복문에서 확인
2.2 m값과 길이가 같아지면 그대로 출력하고 return
"""


def solution():
    check = 0
    if len(answer) == m:
        print(*answer)
        return
    for i in range(n):
        if check != num[i]:
            check = num[i]
            answer.append(num[i])
            solution()
            answer.pop()


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
answer = []
solution()