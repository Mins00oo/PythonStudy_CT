"""수도코드
1. 점수가 3, 2, 1, 0, 1, 2, 3 순서대로니깐 이 순서대로 점수를 매겨본다
2. choice값이 중간값 기준으로 적으면 첫번째 알파벳, 크면 두번째 알파벳이 점수를 획득한다. -> 3을 기준으로 잡으면 될듯
3. 점수를 기록을 다 하고 지표를 따라서 측정해보는데 같으면 알파벳 순서대로 결정한다.
"""


def solution(survey, choices):
    answer = ''
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for s, c in zip(survey, choices):
        if c > 4:
            dic[s[1]] += c - 4
        elif c < 4:
            dic[s[0]] += 4 - c

    l = list(dic.items())

    for i in range(0, 8, 2):
        if l[i][1] < l[i + 1][1]:
            answer += l[i + 1][0]
        else:
            answer += l[i][0]
    print(answer)


solution(["TR", "RT", "TR"], [7, 1, 3])
