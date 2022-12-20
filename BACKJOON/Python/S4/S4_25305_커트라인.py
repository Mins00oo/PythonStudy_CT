N, K = map(int, input().split())  # N은 응시자 수, K는 상을 받는 사람의 수
score = list(map(int, input().split()))

# print(score)

score.sort(reverse=True)  # 점수를 우선 내림차순 정렬

print(score[K - 1])  # 인덱스로 값을 찾을거기 때문에 -1
