# 수도코드
# 1. 기존에는 그냥 (사각형 개수 * 100) - 겹치는 부분으로 구할려고 했는데 이렇게하면 안 겹칠때도 그렇고 생각할 게 너무 많아서 복잡
# 2. 2차원 배열을 생성해줘서 전체 사각형을 돌면서 2차원 배열 값들을 1로 전부 저장해준다
# 3. 나중에는 2차원 배열에서 값이 1인 개수를 세어주면 되고 중복된 부분에 대해서도 똑같이 1로 저장이 되니깐 별도로 해줄 게 없다.

N = int(input())  # 전체 개수를 입력받는다
arr = [[0 for _ in range(101)] for _ in range(101)]  # 2차원 배열을 생성

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(a, a + 10):  # 전체 가로 길이만큼 반복
        for j in range(b, b + 10):  # 전체 세로 길이만큼 반복
            arr[i][j] = 1  # 먼저 세로를 돌면서 값들을 전부 1로 저장해준다. 이렇게 되면 중복되는 부분도 전부 1로 저장된다

count = 0  # 개수가 저장되는 답 변수

for r in arr:
    count += r.count(1)  # 2차원 배열에서 1의 개수를 세주면 된다

print(count)
