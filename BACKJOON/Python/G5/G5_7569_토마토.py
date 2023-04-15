"""수도코드
1. 입력받기: 행을 나타내는 n, 열을 나타내는 m, 높이를 나타내는 h / 토마토에 대한 정보는 h만큼 반복해서 받는다.
2. h만큼 graph를 만들어놓고 입력값은 위에서부터 순서대로 주어지니깐 순서대로 graph에 입력값을 넣는걸로
3.

"""
n, m, h = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
