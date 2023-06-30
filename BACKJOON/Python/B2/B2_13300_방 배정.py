"""수도코드
1. 학생을 학년순서대로 정보를 받아놓는다.
2. 한명씩 순서대로 받으면서 수를 세어나간다.
3. 1학년부터 남녀 차례대로 k와 비교해보면서 방의 개수를 세어준다.
"""

n, k = map(int, input().split())  # n은 총 학생 수, k는 최대로 배정할 수 있는 인원
answer = 0
graph = [[0] * 2 for _ in range(6)]

for _ in range(n):
    s, y = map(int, input().split())  # s가 0이면 여자, 1이면 남자
    graph[y - 1][s - 1] += 1

for i in range(6):
    for j in range(2):
        if graph[i][j] % k == 0:
            answer += graph[i][j] // k
        else:
            answer += (graph[i][j] // k) + 1

print(answer)