board = []  # 2차원 배열 선언
# print(board)
for _ in range(9):
    board.append(list(map(int, input().split())))

# print(board)
Max = 0
x = 0  # 행의 위치를 위헤 선언
y = 0  # 열의 위치를 위해 선언

for i in range(9):  # 행을 가르킨다
    for j in range(9):  # 열을 가르킨다
        if board[i][j] >= Max:
            Max = board[i][j]
            x = i + 1  # x는 최댓값의 행 위치이기 때문에 x + 1
            y = j + 1  # y늰 최댓값의 열의 위치이기 때문에 y + 1

print(Max)
print(x, y)
