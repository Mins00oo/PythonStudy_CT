# 수도코드
# 1. 카드들을 입력받은 후 문자열을 정렬한다. -> 문제점은 카드를 놓을 때 뽑는 순서가 있어서 전체에서 정렬하는것이랑은 다르다
# 2. 파이썬에서 제공하는 deque를 이용한다. -> 양방향에서 데이터를 처리할 수 있는 queue형 자료구조다
# 3. 먼저 첫번째 값을 저장한 후 기준으로 지정해놓고 다음 값들을 비교하면서 왼쪽에 놓을지 오른쪽에 놓을지 지정한다
# 4. 카드들을 마지막으로 출력해준다 -> 그냥 출력하면 원하는대로 문자열만 나오지 않아서 찾아보니 (''.join())을 사용한다..

from collections import deque

T = int(input())  # 테스트 케이스의 개수
for _ in range(T):
    N = int(input())  # 카드의 개수
    card = list(map(str, input().split()))  # 각 카드들의 문자열을 입력받는다
    d = deque()  # 파이썬에서 제공하는 덱 생성
    d.append(card[0])  # 처음 입력받는 값은 저장
    std = card[0]  # 비교하기 위해 기준이 되는 대상 지정

    for i in range(1, len(card)):
        if std >= card[i]:
            d.appendleft(card[i])  # 기준보다 작은 값이 입력되면 기준값의 왼쪽에 놓는다
            std = card[i]  # 기준은 계속해서 변한다
        else:
            d.append(card[i])

    print(''.join(d))
