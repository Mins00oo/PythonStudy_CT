# 수도코드
# 1. 2중 배열을 선언해서 문자열들을 넣어준다
# 2. 행의 길이는 고정적으로 5행이고 열은 최대 15열
# 3. 다시 2중 배열을 반복하면서 값이 0이면 건너뛰고 아니면 전부 붙여서 출력하도록

s = [[0] * 15 for i in range(5)]  # 2중 배열을 선언 5행은 고정, 15열은 최대 길이라서

for i in range(5):  # 행은 항상 5행이므로
    li = list(input())
    for j in range(len(li)):  # 입력받은 문자열을 반복
        s[i][j] = li[j]  # 2중 배열에 문자열을 하나씩 추가

for i in range(15):  # 열은 0행부터 고정적으로 행이 바뀌면서 반복
    for j in range(5):
        if s[j][i] == 0:  # 값이 0이면 그냥 건너뜀
            continue
        else:
            print(s[j][i], end='')  # 그 외에는 하나씩 붙여서 한줄로 출력ㄴ
