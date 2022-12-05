N = int(input())  # 정렬하고자 하는 수 
li = []  # 따로 분리해서 담을려는 리스트
for i in str(N):
    li.append(i)

li.sort(reverse=True)  # 내림차순으로 정렬

# print(li)

for i in li:
    print(i, end='')  # 내림차순으로 정렬된 배열을 붙여서 출력
