def solution():
    if len(answer) == m:
        print(*answer)
        return
    for i in range(0, n):
        answer.append(num[i])
        solution()
        answer.pop()


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
answer = []
solution()