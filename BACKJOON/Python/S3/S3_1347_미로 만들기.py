n = int(input())
arr = list(input())
dx = [-1, 0, 1, 0]  # 상 우 하 좌 / 각 방향으로 움직였을때의 좌표
dy = [0, 1, 0, -1]
d = 2  # 현재 남쪽 방향
x, y = 0, 0
q = [[0, 0]]

for a in arr:
    if a == 'F':  # 앞으로 가는 방향이 나오면 dx, dy에서 d에 따라 x, y 좌표 변경
        x += dx[d]
        y += dy[d]
        q.append([x, y])  # 앞으로 가는 경우에만 우선 배열에 추가
        continue
    if a == 'L':
        d -= 1  # 현재 바라보는 방향으로 왼쪽이면 -1
    elif a == 'R':
        d += 1  # 현재 바라보는 방향 기준으로 오른쪽이면 +1
    d = (d + 4) % 4  # 음수인 원소가 생길 수 있기 때문에

# print(q)
max_x = 0
min_x = 99
max_y = 0
min_y = 99

for i in q:
    min_x = min(min_x, i[0])
    min_y = min(min_y, i[1])

# print(min_x)  # 행의 최솟값 -> -1
# print(min_y)  # 열의 최솟값 ->  0

for i in range(len(q)):
    q[i][0] -= min_x
    q[i][1] -= min_y
    max_x = max(max_x, q[i][0])
    max_y = max(max_y, q[i][1])

# print("max_x:", max_x)
# print("max_y:", max_y)
# print("q:", q)

arr = [['#'] * (max_y + 1) for i in range(max_x + 1)]
# print("arr:", arr)

for i in q:
    x, y = i
    arr[x][y] = '.'

for row in arr:
    print(''.join(row))
    # print(*row, sep='')  위와 똑같이 출력됨
