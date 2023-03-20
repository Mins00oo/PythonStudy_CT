# 오븐의 깊이 d, 피자 반죽의 개수 n
d, n = map(int, input().split())
d_list = list(map(int, input().split()))
n_list = list(map(int, input().split()))

# 어차피 앞에서 통과를 못하면 안으로 피자가 못 들어온다. 그래서 리스트를 조금 수정
for i in range(1, len(d_list)):
    if d_list[i] > d_list[i - 1]:
        d_list[i] = d_list[i - 1]

# 맨 밑에서부터 탐색
# 오븐에 들어간 피자의 개수
n_count = 0
for i in range(d - 1, -1, -1):
    if n_list[n_count] <= d_list[i]:
        n_count += 1

    if n_count == n:
        print(i + 1)
        break

# 들어간 피자의 수가 전체 피자 수랑 다르다 즉, 모든 피자가 들어가지 않았다면
if n_count != n:
    print(0)