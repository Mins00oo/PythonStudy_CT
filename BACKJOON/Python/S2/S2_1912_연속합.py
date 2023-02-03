# 정수 n 입력받기
n = int(input())
# n개의 입력받은 수 들을 list에 저장
a = list(map(int, input().split()))
# 리스트에서 반복하기 합을 저장하기 위해 0번째 초기 인덱스 값으로
sum_a = [a[0]]
# print(sum_a)
# 전체 수를 반복하면서 합을 계산하는데, 최댓값을 저장한다
for i in range(n - 1):
    sum_a.append(max(sum_a[i] + a[i + 1], a[i + 1]))
print(sum_a)
