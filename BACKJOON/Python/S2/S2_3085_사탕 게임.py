"""수도코드
1. n을 입력받고 이차원 배열을 만들어서 값을 넣어준다
2. 색상이 다른 사탕을 바꾸는데 인접한 애들끼리 바꾸기에 아래와 오른쪽만 바꿔본다. 나머지는 겹친다.
3. 먹을 수 있는 사탕의 개수를 구하는 함수를 따로 만든다
3.1 사탕의 개수는 행, 열 각각 따로 구해본다.
3.2 일단, 아래 혹은 오른쪽이랑 바꾼 후 사탕의 개수를 구하는거다. 그러고 다시 복구
4. 아래로 바꿀 수 있을려면 범위 안에 있어야 하니깐 행 i+1이 범위 안에 있어야 한다. 반대로 오른쪽이랑 바꾸는것도 마찬가지
"""

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
maxCnt = 0

for _ in range(n):
    graph[_] = list(map(str, input().rstrip()))


def max_candy():
    global maxCnt
    for i in range(n):
        cnt = 1
        # 각 열을 확인하여 세어본다.
        for j in range(1, n):
            if graph[i][j] == graph[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > maxCnt:
                maxCnt = cnt
        # 각 행을 확인하여 세어본다.
        cnt = 1
        for j in range(1, n):
            if graph[j][i] == graph[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > maxCnt:
                maxCnt = cnt

for i in range(n):
    for j in range(n):
        # 오른쪽하고 변경
        if j + 1 < n:
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
            max_candy()
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
        # 아래하고 변경
        if i + 1 < n:
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            max_candy()
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]

print(maxCnt)
