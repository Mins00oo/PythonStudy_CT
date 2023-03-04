def solution(k, m, score):
    answer = 0
    # 박스의 개수 -> 1개
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        tmp = score[i:i+m]

        if len(tmp) == m:
            answer += min(tmp) * m
    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
