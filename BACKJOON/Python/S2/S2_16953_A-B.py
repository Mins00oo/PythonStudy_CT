# a를 b로 바꾸기 위해 필요한 최소한의 (연산 횟수 + 1)를 출력한다
from collections import deque

a, b = map(int, input().split())
q = deque()
# 연산횟수 + 1을 리턴해야해서 0이 아닌 1을 더한 값을 넣었다
q.append((a, 1))

while q:
    n, c = q.popleft()
    if n == b:
        print(c)
        break
    # b보다 n이 더 큰 경우에는 continue로 다음 연산을 넘어간다. 그렇지 않으면 while문이 계속 돌아가는듯
    if n > b:
        continue
    q.append((n * 2, c + 1))
    q.append((int(str(n) + "1"), c + 1))
else:
    print(-1)
