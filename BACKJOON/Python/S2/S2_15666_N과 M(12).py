"""수도코드
1. 입력받기: n, m 숫자를 입력받을 num은 정렬해서 입력받기
2. 함수정의
2.1 재귀를 반복해줄때 현재 인덱스 값을 넣어주기 때문에 함수의 매개변수로 idx를 넣어준다.
2.2 중복이 되면 안되므로 check값으로 방지한다.
2.3 값을 넣어주는 answer 리스트 길이가 m과 같아지면 출력하고 return
"""


def solution(idx):
    check = 0
    if len(answer) == m:
        print(*answer)
        return
    for i in range(idx, n):
        if check != num[i]:
            check = num[i]
            answer.append(num[i])
            solution(i)
            answer.pop()


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
answer = []
solution(0)
