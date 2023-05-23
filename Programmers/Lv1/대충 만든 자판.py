"""수도코드
1. 함수정의
1.1 3중 for문을 통해 target단어를 가져오고 순차적으로 하나하나 확인한다.
1.2 keymap에서 단어들을 입력할 수 있는지 판단해야한다.
1.3 만약 map안에 있다면 index값 + 1이 된 값과 기존의 값 중 최솟값을 선택해 최종 횟수에 계속 더해준다.
1.4 만약 단어를 map으로 입력할 수 없다면 -1을 리턴하고 다음 타겟 문자열을 확인.
"""


def solution(keymap, targets):
    answer = []
    for t in targets:
        times = 0
        for i in t:
            flag = False
            t = 101
            for j in keymap:
                if i in j:
                    t = min(j.index(i) + 1, t)
                    flag = True
            if not flag:
                times = -1
                break
            times += t
        answer.append(times)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
