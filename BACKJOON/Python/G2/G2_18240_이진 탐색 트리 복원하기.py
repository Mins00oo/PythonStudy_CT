# 가능한 수열인지 먼저 확인, 즉 이전의 노드를 통해서 깊이로 이동했는지 확인
def valid():
    for i in range(n - 1):
        depth = data[i]
        if counts[depth - 1] == 0:
            return 0
        counts[depth] += 1
    return 1


def make():
    nxt_no = list(range(1, n + 2))
    dep = max_depth
    rs = [[0] * counts[i] for i in range(dep + 1)]
    start = 1
    while dep >= 0:
        idx = start
        start = nxt_no[idx]
        for i in range(counts[dep] - 1):
            rs[dep][i] = idx
            nxt = nxt_no[idx]
            n_nxt = nxt_no[nxt]
            nxt_no[nxt] = nxt_no[n_nxt]
            idx = n_nxt

        rs[dep][-1] = idx
        dep -= 1
    print(rs)
    answer = [rs[0][0]] + [0] * (n - 1)
    for i in range(n - 1):
        answer[i + 1] = rs[data[i]].pop(0)
    print(*answer)
    return


n = int(input())
# 각 숫자별 깊이
data = list(map(int, input().split()))

max_depth = max(data)
# 맨 처음 1은 루트노드, 루트노드는 무조건 채워져 있기 때문에
counts = [1] + [0] * max_depth
if valid():
    make()
else:
    print(-1)
