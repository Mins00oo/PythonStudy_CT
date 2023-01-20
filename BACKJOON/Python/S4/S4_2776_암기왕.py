t = int(input())  # 테스트 케이스 개수


def binary(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if n_li[mid] == target:
            return True
        elif n_li[mid] > target:
            end = mid - 1
        elif n_li[mid] < target:
            start = mid + 1
    return False


for _ in range(t):
    n = int(input())
    n_li = list(map(int, input().split()))
    m = int(input())
    m_li = list(map(int, input().split()))
    n_li.sort()
    for x in m_li:
        if binary(x, 0, n - 1):
            print(1)
        else:
            print(0)
