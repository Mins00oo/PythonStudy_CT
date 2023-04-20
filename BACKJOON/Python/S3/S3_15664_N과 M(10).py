def solution(v):
    check = 0
    if len(answer) == m:
        print(*answer)
        return
    for i in range(v, n):
        print('check:', check)
        if check != num[i]:
            check = num[i]
            answer.append(num[i])
            solution(i + 1)
            answer.pop()


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
answer = []
solution(0)
