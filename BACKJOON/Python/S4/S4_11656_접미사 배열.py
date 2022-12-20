S = input()
li = []

for _ in S:
    li.append(S)
    S = S[1:]  # 인덱스 1부터 끝까지

# print(li)
for i in sorted(li):
    print(i)
