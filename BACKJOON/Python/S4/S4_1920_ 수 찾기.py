from collections import Counter

N = int(input())
a_li = list(map(int, input().split()))

M = int(input())
b_li = list(map(int, input().split()))
a_li.sort()  # 정렬을 해줘야 함!!


# c = Counter(a_li)
# # print(c)
# for i in b_li:
#     if i in c:
#         print(1)
#     else:
#         print(0)
def binary(target, start, end):
    while start <= end:
        mid = (start + end) // 2  # 중간 인덱스 값임 !
        if a_li[mid] == target:
            return True
        elif a_li[mid] > target:
            end = mid - 1
            return binary(target, start, end)
        elif a_li[mid] < target:
            start = mid + 1
            return binary(target, start, end)


for i in range(M):
    if binary(b_li[i], 0, N - 1):
        print(1)
    else:
        print(0)
