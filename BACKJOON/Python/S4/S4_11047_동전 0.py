# 수도코드
# 1. 동전의 가치들을 같이 넣은 후 내림차순으로 정렬한다
# 2. k원을 제일 높은 동전의 가치 금액부터 나눠보면서 몫이 0보다 크다면 count를 몫만큼 증가시켜준다

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())  # N과 K를 입력받는다.
li = []
for _ in range(N):
    li.append(int(input()))
# print(li)
li.sort(reverse=True)  # 동전의 가치를 내림차순으로 정렬
count = 0  # K원을 만드는데 드는 동전의 개수

for i in li:
    if K // i > 0:
        count += K // i
        K = K % i

print(count)
