# 수도코드
# 1. 총 개수를 입력받는다.
# 2. 값들을 List에 담는다. 
# 3. List를 오름차순 정렬해준다
# 4. 오름차순된 List를 하나씩 출력

n = int(input())  # 총 개수 N개
li = []  # 모든 수를 배열에 담기 위한 공간
for _ in range(n):
    a = int(input())
    li.append(a)  # 배열에 추가해준다

li.sort()  # 오름차순으로 list를 정렬
for e in li:
    print(e)
