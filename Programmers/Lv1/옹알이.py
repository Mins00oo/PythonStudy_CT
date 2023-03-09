from itertools import permutations


def solution(babbling):
    # 1차 풀이
    # 발음할 수 있는 단어
    speak = ["aya", "ye", "woo", "ma"]
    answer = 0
    # 나올 수 있는 단어들을 전부 담기 위한 공간
    word_list = []
    # 말할 수 있는지 판단하기 위해
    # for i in range(len(babbling)):
    #     for j in range(len(speak)):
    # # 말할 수 있는 단어와 연결되어 있다면 발음하지 못하기에 continue
    # if speak[j] + speak[j] in babbling[i]:
    #     print("ayaaya", 1)
    #     continue
    # # 말할 수 있는 단어가 있다면 그 부분은 빈 문자열로 바꿔주고 for문을 계속 실행
    # # 문자열 자체가 이렇게 빈 문자열로 된다면 발음이 된다는 뜻
    # if speak[j] in babbling[i]:
    #     babbling[i] = babbling[i].replace(speak[j], "")

    # 2차 풀이
    # for i in range(1, len(speak) + 1):
    #     for j in permutations(speak, i):
    #         word_list.append(''.join(j))
    # for i in range(len(babbling)):
    #     for j in range(len(speak)):
    #         # 연속하는 문자열로 구성되어 있을 때
    #         if speak[j] + speak[j] in babbling[i]:
    #             continue
    #         if speak[j] in babbling[i]:
    #             babbling[i] = babbling[i].replace(speak[j], '')

    # 정답 코드
    for i in babbling:  # babbling 문자열 배열만큼 반복
        for v in speak:  # 4가지 발음으로 반복
            if v * 2 not in i:  # 연속된 같은발음이 없다면
                i = i.replace(v, '')  # ' '으로 발음을 치환
        if i.strip() == '':  # 치환 완료된 문자열의 공백을 제거하고 ''와 같다면
            answer += 1  # 발음가능한 단어로 카운팅
    return answer


print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayayeye", "ayayeaya"]))
