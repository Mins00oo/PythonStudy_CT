n = int(input())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))

# 여기서 k는 반복문을 도는 정수의 개수
k = 2
for i in range(1, n):
    for j in range(k):
        # 양 끝에 있는 점인지를 먼저 확인하는 두 조건문
        if j == 0:
            t[i][j] += t[i - 1][j]
        elif i == j:
            t[i][j] += t[i - 1][j - 1]
        else:
            t[i][j] += max(t[i - 1][j], t[i - 1][j - 1])
    k += 1

print(max(t[n - 1]))
