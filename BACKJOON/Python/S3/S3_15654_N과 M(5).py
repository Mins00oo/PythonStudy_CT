from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))
for i in sorted(permutations(num, m)):
    print(*i)
