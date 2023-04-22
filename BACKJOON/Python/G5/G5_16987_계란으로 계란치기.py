"""수도코드
1. 입력받기: 계란의 수 n, 계란의 정보를 2차원 배열로 저장할 egg / 배열의 0번째는 내구도, 1번째는 무게다
2. 함수정의
2.1 현재 들고있는 계란으로는 다른 계란만 쳐야하므로 인덱스가 일치하지 않는 조건 + 깨지지 않은 조건만 치기 위해서 조건을 걸어준다.
2.2 현재 들고있는 계란이 깨졌다면 다음 계란을 들기 위해 depth를 +1해주고 재귀함수를 호출한다.
2.3 다음계란을 깰 때마다 무게에 따라 내구도를 차감해주고 재귀에서 탈출하면 다시 복구해준다.
2.4 현재 들고있는 계란외에 전부 깨져있다면 그 상태로 상태검사를 하여서 개수를 세어주고 리턴한다
3. 상태 검사 함수
3.1 전달받은 배열을 반복하며 계란안의 0번째 인덱스 값인 내구도가 0이하이면 cnt를 +1 해주도록 한다.
"""


def check(eggs):
    cnt = 0
    for e in eggs:
        if e[0] <= 0:
            cnt += 1
    return cnt


def solution(depth, arr):
    global answer
    if depth == n:
        answer = max(answer, check(arr))
        return
    # 현재 들고있는 계란이 깨졌을때
    if arr[depth][0] <= 0:
        solution(depth + 1, arr)
    else:
        isBroken = True
        for i in range(n):
            if depth != i and arr[i][0] > 0:
                isBroken = False
                arr[depth][0] -= arr[i][1]
                arr[i][0] -= arr[depth][1]
                solution(depth + 1, arr)
                arr[depth][0] += arr[i][1]
                arr[i][0] += arr[depth][1]
        if isBroken:
            solution(n, arr)


n = int(input())
egg = [list(map(int, input().split())) for _ in range(n)]
answer = 0
solution(0, egg)
print(answer)
