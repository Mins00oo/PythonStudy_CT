"""수도코드
1. 입력받기: 테스트 케이스 개수 t, 순열의 크기 n, 순열을 저장하는 리스트 arr
2. 각 노드가 노드를 따라가서 방문하는것이고 순환을 돌 수 있기에 방문 체크를 해줘야 하므로 visited도 만들어준다,
3. 함수정의
3.1 매개변수로 들어온 노드 v는 방문한걸로 체크해준다.
3.2 그 다음으로 갈 노드를 v를 통해 가져온다.
3.3 다음 노드인 next로 갈 수 있다면 재귀를 통해 이동해준다.
"""


def solution(v):
    visited[v] = 1
    next = arr[v]
    if visited[next] == 0:
        solution(next)
    return


t = int(input())
arr = [0]
for _ in range(t):
    cnt = 0
    n = int(input())
    visited = [0] * (n + 1)
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    for i in range(1, n + 1):
        if visited[i] == 0:
            solution(i)
            cnt += 1
    print(cnt)
