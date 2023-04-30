"""수도코드
1. 입력받기: 반복할 횟수 m, cup의 번호 1~3번까지 생성
2. 컵의 번호를 a, b로 입력받으면서 파이썬의 리스트 인덱스 위치를 바꾸기 위해 a, b값의 인덱스를 가져온다
3. 가져온 인덱스를 통해 cup에서 swap으로 위치만 바꿔준다.
4. 공의 위치는 고정적으로 맨 앞에 있기 때문에 출력은 0번째 인덱스 값 출력
"""

m = int(input())
cup = [1, 2, 3]
for _ in range(m):
    a, b = map(int, input().split())
    ai = cup.index(a)
    bi = cup.index(b)
    cup[ai], cup[bi] = cup[bi], cup[ai]

print(cup[0])