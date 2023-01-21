from collections import Counter

N = int(input())
a_li = list(map(int, input().split()))

M = int(input())
b_li = list(map(int, input().split()))

a_li.sort()


# c = Counter(a_li)
# # print(c)
# for i in b_li:
#     if i in c:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

def binary(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if a_li[mid] == target:
            return True
        elif a_li[mid] > target:
            end = mid - 1
        elif a_li[mid] < target:
            start = mid + 1
    return False


for x in b_li:
    if binary(x, 0, N - 1):
        print(1, end=" ")
    else:
        print(0, end=" ")
