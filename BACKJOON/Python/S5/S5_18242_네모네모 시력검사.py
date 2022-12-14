# 수도코드
# 정사각형의 한 변의 길이는 3보다 큰 홀수
# 한 변의 길이를 알아내기 위해 처음 색칠되는 좌표를 얻고 길이를 알아내면
#

# n, m = map(int, input().split())  # 높이 n과 너비 m
# row = 0
# column = 0
#
# for i in range(n):
#     a = list(input())  # m개의 그림 문자열이 주어진다
#     for j in range(len(a)):
#         if a[j] == '#':
#             row = i + 1
#             column = j + 1
#             break
#
# print(row, column)

# 수도코드
# 배열에 각 행의 문자열을 우선 전부 넣어둔다
# 정사각형으로 된다는 점과 한 변이 비어있다는 점을 생각해봐야하는거같다.
# 왼쪽 혹은 오른쪽이 비어있는지 볼려면 열을 구성하는 문자열들을 하나씩 검사해야 할거같다.
# 반대로 위 혹은 아래가 비어있는지 볼려면 열이 아닌 행을 구성하는 문자열들을 검사해야 하는거같다.
# '#'이 나오게 된다면 그 열에 빈 문자열이 존재하는지 확인해야한다.
# 왼쪽인지 오른쪽인지 구별은 ->
# 위인지 아래인지 구별은 ->

Y, X = map(int, input().split())  # Y는 행, X는 열
Ychar = []
for i in range(Y):
    Ychar.append(input())

# print(Ychar)
for x in range(X):  # x가 7이라면, 0~6까지
    for y in range(Y - 2):  # 왜 Y-2? -> #이 나온다면 그 y+1에는 #이 없고 y + 2에는 #이 있는지 확인하기 위해 즉, 빈 문자열인지
        if Ychar[y][x] == "#":
            cnt = 0
            if Ychar[y][x] == Ychar[y + 2][x] and Ychar[y][x] != Ychar[y + 1][x]:  # 현재 위치한 y,x 좌표 옆에 빈 문자열인지
                for d in range(x + 1, X):  # 다음 열부터 끝까지 # 이 나오는지 비교해보고 있으면 cnt 증가 즉, 왼쪽이라는 뜻
                    if Ychar[y][d] == "#":
                        cnt += 1
                if cnt >= 1:
                    print("LEFT")
                else:
                    print("RIGHT")

for y in range(Y):
    for x in range(X - 2):
        if Ychar[y][x] == "#":
            cnt = 0
            if Ychar[y][x] == Ychar[y][x + 2] and Ychar[y][x] != Ychar[y][x + 1]:
                for d in range(y + 1, Y):
                    if Ychar[d][x] == "#":
                        cnt += 1
                if cnt >= 1:
                    print("UP")
                else:
                    print("DOWN")

