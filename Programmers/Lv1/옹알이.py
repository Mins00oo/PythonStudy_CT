def solution(babbling):
    # 발음할 수 있는 단어
    speak = ["aya", "ye", "woo", "ma"]
    # 말할 수 있는지 판단하기 위해
    for i in range(len(babbling)):
        for j in range(len(speak)):
            # 말할 수 있는 단어와 연결되어 있다면 발음하지 못하기에 continue
            if speak[j] + speak[j] in babbling[i]:
                continue
            # 말할 수 있는 단어가 있다면 그 부분은 빈 문자열로 바꿔주고 for문을 계속 실행
            # 문자열 자체가 이렇게 빈 문자열로 된다면 발음이 된다는 뜻
            if speak[j] in babbling[i]:
                babbling[i] = babbling[i].replace(speak[j], "")
    return babbling.count("")


print(solution(["aya", "yee", "u", "maa"]))
