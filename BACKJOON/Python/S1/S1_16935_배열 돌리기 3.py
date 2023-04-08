"""수도코드
1. 배열의 크기 n,m과 연산의 수 r을 입력받는다.
2. 이차원 배열 graph를 만들고 입력값들을 넣어준다.
3. 1번 연산 -> 상하를 뒤집는다 graph안의 값들이 역순으로 다시 재배치 graph[0] = graph[5], graph[1] = graph[4]..
3.1 for문을 전부 다 하지 않고 행 길이의 반만큼 반복하면 안의 값들이 바뀐다.
4. 2번 연산 -> 행이 재배치된다. graph[0][0] = graph[0][5] graph[0][1] = graph[0][4]
4.1 이중 for문을 통해 1번 연산처럼 swap을 해준다.
5. 3번 연산 -> 각 열이 행으로 재배치된다. graph[5][0], graph[4][0], ... graph[0][0] -> graph[0]에 들어감
5.1 graph[5][1], graph[4][1] ... graph[0][1] -> graph[1]에 들어감
5.2 이중 for문으로 인덱스를 조정
5.3 원래 행의 길이 n이 열의 길이가 되고 열의 길이 m이 행의 길이가 되고 return 된다.
6. 4번 연산 -> 3번과 유사하게 바뀜
6.1 3번연산이 이루어진 다음 4번 연산이라면 2번 연산에서의 결과 그대로다.
7. 5번 연산 -> n // 2, m // 2의 4개 배열로 나누었을때 시계 방향으로 돌아가는거고 6번 연산 -> 반시계 방향으로 돌아가면서 재배열
"""

n, m, r = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph[_] = list(map(int, input().split()))
solve = list(map(int, input().split()))


def solve_1(x):
    global graph
    if x == 1:
        for i in range(n // 2):
            graph[i], graph[n - 1 - i] = graph[n - 1 - i], graph[i]
    elif x == 2:
        for i in range(n):
            for j in range(m // 2):
                graph[i][j], graph[i][m - 1 - j] = graph[i][m - 1 - j], graph[i][j]
    elif x == 3:
        temp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            li = []
            for j in range(n):
                li.append(graph[n - 1 - j][i])
            temp[i] = li
        graph = temp
    elif x == 4:
        if len(graph) == n:
            temp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                li = []
                for j in range(n):
                    li.append(graph[j][m - i - 1])
                temp[i] = li
            graph = temp
        elif len(graph) == m:
            temp = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                li = []
                for j in range(m):
                    li.append(graph[j][n - i - 1])
                temp[i] = li
            graph = temp
    elif x == 5:
        # 3, 4 둘 다 거쳤을 때
        if len(graph) == n:
            temp = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n // 2):
                for j in range(m // 2):
                    temp[i][j + m // 2] = graph[i][j]
            for i in range(n // 2):
                for j in range(m // 2, m):
                    temp[i + n // 2][j] = graph[i][j]
            for i in range(n // 2, n):
                for j in range(m // 2, m):
                    temp[i][j - m // 2] = graph[i][j]
            for i in range(n // 2, n):
                for j in range(m // 2):
                    temp[i - n // 2][j] = graph[i][j]
            graph = temp
        elif len(graph) == m:
            temp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m // 2):
                for j in range(n // 2):
                    temp[i][j + n // 2] = graph[i][j]
            for i in range(m // 2):
                for j in range(n // 2, n):
                    temp[i + m // 2][j] = graph[i][j]
            for i in range(m // 2, m):
                for j in range(n // 2, n):
                    temp[i][j - n // 2] = graph[i][j]
            for i in range(m // 2, m):
                for j in range(n // 2):
                    temp[i - m // 2][j] = graph[i][j]
            graph = temp
    elif x == 6:
        if len(graph) == n:
            temp = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n // 2):
                for j in range(m // 2):
                    # temp[0,1,2][0,1,2,3]
                    temp[i][j] = graph[i][j + m // 2]
            for i in range(n // 2):
                for j in range(m // 2):
                    temp[i + n // 2][j] = graph[i][j]
            for i in range(n // 2, n):
                for j in range(m // 2, m):
                    temp[i][j] = graph[i][j - m // 2]
            for i in range(n // 2):
                for j in range(m // 2, m):
                    temp[i][j] = graph[i + n // 2][j]
            graph = temp
        elif len(graph) == m:
            temp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m // 2):
                for j in range(n // 2):
                    temp[i][j] = graph[i][j + n // 2]
            for i in range(m // 2):
                for j in range(n // 2, n):
                    temp[i][j] = graph[i + m // 2][j]
            for i in range(m // 2, m):
                for j in range(n // 2, n):
                    temp[i][j] = graph[i][j - n // 2]
            for i in range(m // 2, m):
                for j in range(n // 2):
                    temp[i][j] = graph[i - m // 2][j]
            graph = temp


for i in range(r):
    solve_1(solve[i])

for i in range(len(graph)):
    print(*graph[i])
