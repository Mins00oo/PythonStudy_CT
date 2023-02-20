# 가로길이 n
n = int(input())
d = [0 for _ in range(n+1)]

d[1] = 1
d[2] = 2
if n < 3:
    print(d[n])
else:
    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2]) % 796

    print(d[n])