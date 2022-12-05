li = []
for _ in range(10):
    a = int(input())  # 10째줄까지 숫자를 제시
    li.append(a % 42)  # 나머지들을 모두 li에 저장

arr = set(li)  # set을 통해 중복값들 제거
print(len(arr))  # 중복된 값들을 제외한 값들의 개수
