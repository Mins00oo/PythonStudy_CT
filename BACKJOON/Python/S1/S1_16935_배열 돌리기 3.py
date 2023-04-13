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


def cal_1():
    global graph
    for i in range(n // 2):
        graph[i], graph[n - 1 - i] = graph[n - 1 - i], graph[i]


def cal_2():
    global graph
    for i in range(n):
        for j in range(m // 2):
            graph[i][j], graph[i][m - 1 - j] = graph[i][m - 1 - j], graph[i][j]


def cal_3():
    global graph
    temp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = graph[n - 1 - j][i]
    graph = temp


def cal_4():
    global graph
    temp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = graph[j][m - i - 1]
    graph = temp


def cal_5():
    global graph
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


def cal_6():
    global graph
    temp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            temp[i + n // 2][j] = graph[i][j]
    for i in range(n // 2, n):
        for j in range(m // 2):
            temp[i][j + m // 2] = graph[i][j]
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            temp[i - n // 2][j] = graph[i][j]
    for i in range(n // 2):
        for j in range(m // 2, m):
            temp[i][j - m // 2] = graph[i][j]
    graph = temp


for i in solve:
    if i == 1:
        cal_1()
    elif i == 2:
        cal_2()
    elif i == 3:
        cal_3()
        n, m = m, n
    elif i == 4:
        cal_4()
        n, m = m, n
    elif i == 5:
        cal_5()
    elif i == 6:
        cal_6()

for i in range(len(graph)):
    print(*graph[i])
