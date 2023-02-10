t = int(input())  # 테스트 케이스의 개수

for _ in range(t):
    li = list(map(int, input().split()))
    li.sort()
    del li[0]
    del li[3]
    if max(li) - min(li) >= 4:
        print('KIN')
    else:
        print(sum(li))
    li = []

# 점수 입력 받고 정렬한 다음
# 0번째, 4번째 인덱스로 해당 값 제거하고 del로 제거
# min, max의 차이가 4 이상이면 kin을 출력
