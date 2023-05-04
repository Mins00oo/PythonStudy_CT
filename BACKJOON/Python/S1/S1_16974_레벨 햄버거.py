"""수도코드
1. 입력받기: 레벨 n, 먹은 햄버거의 장 수 x
2. 레벨 0 - p, B   P   B 이 사이에 레벨- 1을 넣어준다.
3. 레벨 1 -> BPPPB
4. 레벨 2 -> B  ~  P  ~ B
"""
n, x = map(int, input().split())


def eat(n, x):
    if n == 0:
        return x
    if x == 1:
        return 0
