n = int(input())
li = [[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    for _ in range(2):
        li[i][0] = age
        li[i][1] = name

# print(li)
li.sort(key=lambda x: x[0])
# print(li)
for k in range(len(li)):
    print(li[k][0], li[k][1])
