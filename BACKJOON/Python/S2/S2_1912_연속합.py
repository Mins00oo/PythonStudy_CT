n = int(input())
a = list(map(int, input().split()))
sum_a = [a[0]]

for i in range(len(a) - 1):
    sum_a.append(max(sum_a[i] + a[i + 1], a[i + 1]))
print(max(sum_a))
