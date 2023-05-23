"""수도코드
1. 입력받기
2. 함수정의
2.1 알파벳 전체를 문자열로 선언해준다.
2.2 스킵해야하는 문자는 알파벳 전체에서 제외해준다
2.3 index만큼 늘려야하는 s를 반복하면서 answer에 추가해준다.
"""


def solution(s, skip, index):
    answer = ''
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for sk in skip:
        alpha = alpha.replace(sk, "")

    for i in s:
        answer += alpha[(alpha.index(i) + index) % len(alpha)]

    return answer


print(solution("aukks", "wbqd", 5))
