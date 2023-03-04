def solution(k, m, score):
    answer = 0
    # 내림차순 정렬
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        # m개만큼의 tmp 생성
        tmp = score[i:i + m]
        # tmp의 길이가 담기는 과일 개수인 m과 같으면 answer에 추가
        if len(tmp) == m:
            answer += min(tmp) * m
    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
