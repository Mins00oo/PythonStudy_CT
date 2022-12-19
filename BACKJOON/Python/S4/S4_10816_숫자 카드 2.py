from collections import Counter

N = int(input())  # 가지고 있는 카드 개수
a_li = list(map(int, input().split()))

M = int(input())  # 비교 대상인 카드 개수
b_li = list(map(int, input().split()))

c = Counter(a_li)  # count 함수 대신 사용
# print(c)
for i in b_li:
    if i in c:
        print(c[i], end=' ')
    else:
        print(0, end=' ')
