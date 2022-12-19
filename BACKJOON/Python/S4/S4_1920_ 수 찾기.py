from collections import Counter

N = int(input())
a_li = list(map(int, input().split()))

M = int(input())
b_li = list(map(int, input().split()))

c = Counter(a_li)

for i in b_li:
    if i in c:
        print(1)
    else:
        print(0)
