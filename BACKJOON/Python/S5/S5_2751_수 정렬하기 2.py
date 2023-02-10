# 수도코드
# 병합정렬은 전체 배열을 반으로 크게 자른 후 다시 또 잘라가며 쪼갤 수 없을 때까지 쪼개고
# 다시 그 위치에서 다시 정렬을 하면서 합친다.
# 전체 배열을 그럼 먼저 끝까지 쪼개서 좌우로 나눈다.

import sys

n = int(input())
li = []

for i in range(n):
    li.append(int(sys.stdin.readline()))


def sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    print("left:", left)
    print("right:", right)
    new_list = []
    i = 0
    j = 0
    # print(new_list)
    while (i < len(left)) & (j < len(right)):
        if left[i] > right[j]:
            new_list.append(right[j])
            j += 1
        else:
            new_list.append(left[i])
            i += 1
    print(new_list)
    # print(i)
    # print(j)
    while j < len(right):
        new_list.append(right[j])
        j += 1
    while i < len(left):
        new_list.append(left[i])
        i += 1
    # print(new_list)
    return new_list


for i in sort(li):
    print(i)
