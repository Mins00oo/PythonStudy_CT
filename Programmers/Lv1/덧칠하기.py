"""수도코드
1. 벽의 총 길이 n, 롤러의 길이 m, 칠할 구역 section을 입력받는다.
2. 벽을 칠했는지 확인할 visited를 n개 만큼 생성해주고 아직 칠하지 않았기에 먼저 section부분은 0으로 만들어둔다.
3. visited에서 0인 부분을 찾는데 맨 앞의 값을 가져오고 m개 만큼 칠해준다 -> 이 부분을 반복하다보니 시간복잡도가 증가해서 초과가 발생함
3.1 맨 처음 인덱스부터 반복을 끝까지 하되, 칠해야 할 부분 즉 값이 0이 될 때 visited를 1로 바꿔주고 위치를 증가시켜주며 반복한다
4. 그런 후에 answer을 리턴하면 시간복잡도가 훨씬 낮아진다.
"""


def solution(n, m, section):
    answer = 0
    visited = [1] * n
    for i in section:
        visited[i - 1] = 0
    i = 0
    while i < n:
        if visited[i] == 0:
            for k in range(i, min(i + m, n)):
                visited[k] = 1
            answer += 1
            i += m - 1
        else:
            i += 1
    return answer


print(solution(8, 4, [2, 3, 6]))
