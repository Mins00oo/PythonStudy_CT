x_list = []
y_list = []
for _ in range(3):
    # x, y 좌표를 받고 각각 저장
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

# 반복문을 돌면서 개수가 1개인 좌표가 4번째 좌표값이 된다
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x4 = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y4 = y_list[i]

print(x4, y4)
