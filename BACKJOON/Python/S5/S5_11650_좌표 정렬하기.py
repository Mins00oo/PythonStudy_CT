# N = int(input())  # 점의 개수
# array = []  # 전체 값들을 넣을 공간
# for _ in range(N):
#     [a, b] = map(int, input().split())
#     array.append([a, b])  # [[3,4], [1,1]]  이런식으로 들어간다
#
# s_array = sorted(array)  # 2차원 array를 함수를 통해 정렬
#
# print(s_array)
#
# for i in range(N):
#     print(s_array[i][0], s_array[i][1])  # 0번째 인덱스 -> [1,-1]값의 0번째와 1번째 인덱스를 출력한다.

import sys

N = int(input())  # 점의 개수
array = []  # 전체 값들을 넣을 공간
for _ in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    array.append([a, b])  # [[3,4], [1,1]]  이런식으로 들어간다

s_array = sorted(array)  # 2차원 array를 함수를 통해 정렬

# print(s_array)

for i in range(N):
    print(s_array[i][0], s_array[i][1])  # 0번째 인덱스 -> [1,-1]값의 0번째와 1번째 인덱스를 출력한다.

