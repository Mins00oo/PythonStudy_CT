n, c = map(int, input().split())
n_li = [int(input()) for _ in range(n)]
answer = 0
n_li.sort()


def binary(start, end):
    while start <= end:
        mid = (start + end) // 2
        now = n_li[0]
        count = 1
        global answer
        for i in range(1, len(n_li)):
            if n_li[i] >= mid + now:
                now = n_li[i]
                count += 1
        # 공유기가 mid 거리로 설치가 된다면 최대 거리 구하고
        if count >= c:
            answer = mid
            start = mid + 1
        # 안되면 끝점을 조절
        else:
            end = mid - 1


binary(1, max(n_li) - n_li[0])
print(answer)
