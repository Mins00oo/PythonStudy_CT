"""수도코드
1. 재료를 순서대로 들어오게 만든다.
2. 들어오는 재료가 1, 2, 3, 1 순서대로 있다면 개수 + 1을 하고
3. 만드는데 사용된 재료 4개는 지우고 계속 추가한다.
"""


def solution(ingredient):
    answer = 0
    q = []
    for _ in ingredient:
        q.append(_)
        if q[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                q.pop()

    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
