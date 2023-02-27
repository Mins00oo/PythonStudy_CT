def solution(t, p):
    answer = 0
    len_p = len(p)
    # t에서 p의 길이만큼의 부분 문자열이 나올 수 있는 개수
    for i in range(len(t) - len_p + 1):
        if int(t[i:i + (len_p - 1)]) < int(p):
            answer += 1
    return answer
