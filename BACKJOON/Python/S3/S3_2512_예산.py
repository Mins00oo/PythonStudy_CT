# 지방의 수 N
import sys

input = sys.stdin.readline
n = int(input())
n_li = list(map(int, input().split()))
m = int(input())


def binary(start, end):
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in n_li:
            if i > mid:
                total += mid
            else:
                total += i
        if total > m:
            end = mid - 1
        else:
            start = mid + 1
    return end


print(binary(0, max(n_li)))
