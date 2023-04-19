def solution(idx):
    global arr
    if len(arr) == m:
        print(*arr)
        return
    for i in range(idx, n):
        arr.append(num[i])
        solution(i + 1)
        arr.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []
solution(0)
