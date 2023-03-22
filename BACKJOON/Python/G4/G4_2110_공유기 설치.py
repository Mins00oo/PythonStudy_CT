# n은 집, c는 공유기의 수
n, c = map(int, input().split())
home_li = sorted([int(input()) for _ in range(n)])
answer = 0


def binary(start, end):
    while start <= end:
        mid = (start + end) // 2
        now = home_li[0]
        # 맨 앞집부터 공유기 설치, 그 다음부터는 거리에 따라서
        count = 1
        global answer
        # 맨 앞집 다음부터 어느 집에 공유기를 설치할 수 있는지
        for i in range(1, len(home_li)):
            if home_li[i] >= mid + now:
                now = home_li[i]
                count += 1
        # 공유기가 mid 거리로 설치가 된다면 최대 거리 구하고
        if count >= c:
            answer = mid
            start = mid + 1
        # 안되면 끝점을 조절
        else:
            end = mid - 1


binary(1, max(home_li) - home_li[0])
print(answer)
