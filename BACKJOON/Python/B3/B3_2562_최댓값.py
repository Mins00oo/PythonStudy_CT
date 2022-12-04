li = []  # 9개의 숫자를 담을 배열 공간
count = 0  # 최대값이 몇 번째 수인지 저장하기 위한 공간
for _ in range(9):
    N = int(input())  # 숫자들을 입력받는다
    li.append(N)

# print(li)

max_N = max(li)  # max함수를 이용하면 list에서 최댓값을 찾는다
print(max_N)

for i in range(len(li)):  # li의 개수만큼 반복하여
    if max_N == li[i]:  # 최대값과 배열의 요소가 일치한다면 
        count = i  # 일치하는 요소의 인덱스 값을 count에 저장하도록
        break

print(count + 1)
