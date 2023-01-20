from collections import Counter

N = int(input())  # 가지고 있는 카드 개수
a_li = list(map(int, input().split()))
a_li.sort()
a_liDisc = dict()
M = int(input())  # 비교 대상인 카드 개수
b_li = list(map(int, input().split()))

for c in a_li:
    if c not in a_liDisc:
        a_liDisc[c] = 1
    else:
        a_liDisc[c] += 1


# c = Counter(a_li)  # count 함수 대신 사용
# # print(c)
# for i in b_li:
#     if i in c:
#         print(c[i], end=' ')
#     else:
#         print(0, end=' ')
#
def binary(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if a_li[mid] == target:
            return True
        elif a_li[mid] > target:
            end = mid - 1
        elif a_li[mid] < target:
            start = mid + 1


for i in b_li:
    if binary(i, 0, N - 1):
        print(a_liDisc[i], end=" ")
    else:
        print(0, end=" ")
