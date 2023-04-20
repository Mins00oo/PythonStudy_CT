"""수도코드
1. 입력받기: l,c 암호로 구성되는 모음은 정렬해서 받는다.
2. 백트래킹 함수정의
2.1 answer의 길이가 l과 같아지면 출력하고 return하도록 조건 설정
2.2 answer에 넣어준 후, 재귀를 돌리는데 인덱스 값 보다 + 1을 해주면서 추가해줘야 하기 때문에 매개변수로 인덱스를 받고 + 1을 해준다.
2.3 문제에서 자음 최소 1개, 모음 최소 2개를 포함해야 한다고 하므로 개수를 세어준다
2.4 단어가 다 완성이 되었을 때, 자음 모음을 카운트 해주고 자음은 최소 1개 이상, 모음이 최소 2개 이상이면 출력하도록 한다.
2.5 자음은 문제에서 주어졌기에 모음은 단어 중 자음이 아닌 것이 모음이다.
"""


def solution(idx):
    if len(answer) == l:
        vo, co = 0, 0
        for i in range(l):
            if answer[i] in constant:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(answer))
    for i in range(idx, c):
        answer.append(alpha[i])
        solution(i + 1)
        answer.pop()


l, c = map(int, input().split())
alpha = sorted(list(input().split()))
constant = ['a', 'i', 'o', 'u', 'e']
answer = []
solution(0)
