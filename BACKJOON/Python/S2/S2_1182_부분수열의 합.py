"""수도코드
1. 백트래킹 함수 정의
1.1 깊이를 나타내는 index를 설정하고 누적 결과값, 그리고 횟수 cnt를 설정한다
1.2 이때, cnt는 처음에 0이다. 즉, 빈 요소가 아닐때 확인을 하기 위해 cnt + 1을 해주며 cnt가 0보다 큰지 확인한다.
1.3 누적값이 s와 같다면 result를 하나씩 증가시켜준다
1.4 그렇지 않다면 반복문을 통해 인덱스를 늘려가는데 재귀를 통해 그 안에서 부분수열을 합을 구해나가면 된다.
"""


def solution(index, cur_result, cnt):
    global result
    if cur_result == s and cnt > 0:
        result += 1
    for i in range(index, n):
        solution(i + 1, cur_result + s_li[i], cnt + 1)


n, s = map(int, input().split())
s_li = list(map(int, input().split()))
result = 0
solution(0, 0, 0)
print(result)
