def solution(k, score):
    answer = []
    temp = [] * k
    if k > len(score):
        temp = [] * len(score)
        for _ in range(len(score)):
            temp.append(score[_])
            answer.append(min(temp))
        return answer
    for _ in range(k):
        temp.append(score[_])
        answer.append(min(temp))
    for _ in range(k, len(score)):
        temp.sort()
        if min(temp) < score[_]:
            temp[0] = score[_]
        answer.append(min(temp))
    return answer


print(solution(5, [2, 3, 1]))
