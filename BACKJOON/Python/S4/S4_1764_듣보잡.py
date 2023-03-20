# 듣도 못한 사람 n, 보도 못한 사람 m
n, m = map(int, input().split())
n_li = [input().strip() for _ in range(n)]
m_li = [input().strip() for _ in range(m)]
result = []
n_li.sort()
m_li.sort()


def binary(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == m_li[mid]:
            return True
        elif target > m_li[mid]:
            start = mid + 1
        elif target < m_li[mid]:
            end = mid - 1
    return False


for i in n_li:
    if binary(i, 0, len(m_li) - 1):
        result.append(i)

result.sort()
print(len(result))
for _ in result:
    print(_)
