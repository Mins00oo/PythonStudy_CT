# 수도코드
# 1. 킹, 퀸 등에 따라 각 수를 배열에 담아준다.
# 2. 6개의 수를 입력받아 리스트에 넣는다
# 3. 처음 입력받은 수의 개수와 똑같이 맞춰서 차이만큼 출력

a = [1, 1, 2, 2, 2, 8]
# 구성되어 있는 개수 배열에 담기

li = list(map(int, input().split()))
# 입력받은 수를 list에 담기

for i in range(6):
    print(a[i] - li[i], end=' ')
    # 처음 담겨있는 배열의 개수와 일치하게 맞춰서 list의 값에서 차이만큼 출력
