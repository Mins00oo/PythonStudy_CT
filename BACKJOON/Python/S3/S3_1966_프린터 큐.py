""" 수도코드
1. 각 테스트 케이스에 맞춰서 문서 개수 n, 문서의 인덱스 m
2. 각 문서의 중요도를 입력받고, 인덱스 리스트도 만든다.
2.1 인덱스 리스트는 for문으로
3. 문서의 중요도 리스트 p를 반복문을 통해 맨 앞의 값이 최대값일때까지 반복해본다.
3.1 이때, 만약 맨 앞의 값이 최댓값이라면 우리가 찾고자 m의 문서가 인쇄되었는지 확인한다.
3.2 맨 앞에 최댓값이 왔다는건 인쇄가 되었다는것이기 때문에 cnt를 +1 해준다.
3.3 m번째가 인쇄되었는지 확인하려면 p리스트가 fifo로 바뀌는거처럼 인덱스 리스트도 바꿔주면 된다.
4. 만약 최댓값이 아니라면 fifo에 따라 맨 앞의 값을 뒤로 뺀다 -> pop하고 append

"""

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    index_list = [i for i in range(n)]
    cnt = 0
    while p:
        if p[0] == max(p):
            cnt += 1
            if index_list[0] == m:
                print(cnt)
                break
            p.pop(0)
            index_list.pop(0)
        else:
            p.append(p.pop(0))
            index_list.append(index_list.pop(0))
