N = int(input())
graph = [list(map(int, input())) for _ in range(N)]  # N행 N열의 정사각형
num = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 상 하 좌 우

# print(graph)

count = 0  # 집이 있는 곳을 세기 위함
result = 0  # 총 몇개가 있는지


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:  # 헹이나 열이 정사각형 범위를 벗어난다면
        return False

    if graph[x][y] == 1:
        # print("x:", x)
        # print("y:", y)
        # print("----")
        global count
        count += 1
        graph[x][y] = 0  # 다시 방문하지 않도록 0으로 변경
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # print(nx)
            # print(ny)
            dfs(nx, ny)  # 현재 위치에서 재귀를 이용해 상하좌우로 이동하여 조건문으로 검증
        return True
    return False


for i in range(N):
    for j in range(N):
        if dfs(i, j) == 1:
            num.append(count)
            result += 1  # 총 단지수를 하나씩 증가
            count = 0  # 인접한 집들이 몇개인지 세는게 끝났다면 다시 0으로 초기화 
# print(num)
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
