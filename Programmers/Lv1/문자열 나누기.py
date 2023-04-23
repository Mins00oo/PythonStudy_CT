"""수도코드
1. 문자열을 분리하여 담을 word 리스트를 생성하여 저장
2. 다른 개수, 같은 개수를 각각 저장할 변수 생성
3. 맨 왼쪽부터 시작하며 두 변수가 같아지면 answer을 +1 해주고 각 개수들을 0으로 초기화
4. 양옆에 인접한 문자열이 같으면 같은 개수 + 1, 다르면 + 1
"""
from collections import deque


def solution(s):
    answer = 0
    q = deque(s)
    while q:
        cnt1, cnt2 = 1, 0
        x = q.popleft()
        while q:
            n = q.popleft()
            if x == n:
                cnt1 += 1
            else:
                cnt2 += 1
            if cnt1 == cnt2:
                answer += 1
                break
    if cnt1 != cnt2:
        answer += 1
    return answer


print(solution('abracadbrac'))
