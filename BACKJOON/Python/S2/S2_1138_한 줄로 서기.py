"""수도코드
1. n을 입력받고, n만큼 1부터 n + 1까지의 for문으로 list를 생성한다.
2. index_list와 새롭게 자리를 배치할 answer를 만들어준다.
3. 반복문을 통해 answer에 넣어준다
4. 2 1 1 0 / 1 2 3 4/ 0 0 0 0이 있다고 한다면 0 0 1 0 -> 0 2 1 0 -> 0 2 1 3 -> 4 2 1 3
5. 이 문제에서 cnt와 왼쪽 사람의 수를 비교한다. 즉, 키가 3인 경우에 왼쪽에 1명이 있다. 이때, cnt를 증가시킬려면 빈자리일때만 증가하게 한다.
6. 그렇지 않고 그냥 else로 cnt += 1을 해버리면 cnt가 3까지 증가하기에 왼쪽에 3명이 있다라고 되는거다.
"""
n = int(input())
n_list = list(map(int, input().split()))
index_list = [i for i in range(1, n + 1)]
answer = [0] * n
for i in range(n):
    cnt = 0
    for j in range(n):
        print('i:', i, "j:", j, "cnt:", cnt)
        # 왼쪽에 개수만큼 있고 위치할려는 자리가 비어있는지 확인
        if cnt == n_list[i] and answer[j] == 0:
            answer[j] = index_list[i]
            break
        # 빈자리라면 cnt를 1증가
        elif answer[j] == 0:
            cnt += 1
print(*answer)
