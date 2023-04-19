def solution(idx):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(idx, n):
        answer.append(num[i])
        solution(i)
        answer.pop()


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
answer = []
solution(0)