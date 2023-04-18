"""수도코드
1. 순서를 고려해야하는 조합이므로 순열(permutaions)을 사용한다.
"""
from itertools import permutations

n, m = map(int, input().split())
li = [i for i in range(1, n + 1)]
for i in permutations(li, m):
    print(*i)
