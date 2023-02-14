# n개의 수를 외워야하는데 a만큼 외울 수 있고 b만큼 까먹는다.
import sys

a, b, n = map(int, sys.stdin.readline().split())
# 몇일이 소비되는지 변수
period = 0
# 외운 단어의 총 개수
word_sum = 0

for _ in range(n):
    word_sum += a
    period += 1
    if word_sum == n:
        print(period)
        break
    word_sum -= b

# 시간복잡도는 O(n)
