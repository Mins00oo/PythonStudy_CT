# N, K = map(int, input().split())  # N은 응시자 수, K는 상을 받는 사람의 수
# score = list(map(int, input().split()))
#
# # print(score)
#
# score.sort(reverse=True)  # 점수를 우선 내림차순 정렬
#
# print(score[K - 1])  # 인덱스로 값을 찾을거기 때문에 -1

N, K = map(int, input().split())  # N은 응시자 수, K는 상을 받는 사람의 수
score = list(map(int, input().split()))
new_sorted = []


def sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    li = []

    while (i < len(left)) & (j < len(right)):
        if left[i] > right[j]:
            li.append(right[j])
            j += 1
        elif left[i] < right[j]:
            li.append(left[i])
            i += 1

    while i < len(left):
        li.append(left[i])
        i += 1

    while j < len(right):
        li.append(right[j])
        j += 1
    return li


for i in sort(score):
    new_sorted.append(i)

print(new_sorted[N - 2])
