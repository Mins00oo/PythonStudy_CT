# 수도코드
# 1. 개수만큼 글자들을 입력받아서 list에 담는다
# 2. set을 통해 중복제거를 한다
# 3. sort로 정렬을 해준다 -> 알파벳 순서대로 / 문자열 길이 순으로
# 4. 답을 출력

N = int(input())  # 전체 개수
li = []  # 글자를 담을 list

for _ in range(N):
    li.append(input())  # 먼저 글자들을 list에 담는다

# print(li)

set_li = set(li)  # set 타입으로 변경해주면서 중복제거
li = list(set_li)  # 다시 list형태의 li 변수에 담기 위한 코드
li.sort()  # 알파벳 순서대로 정렬
li.sort(key=len)  # 문자열 길이 순으로 정렬
  
for i in li:
    print(i)
