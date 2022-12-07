# 수도코드
# 1. 각각 돈을 인출하는데 시간이 나오는데 필요한 시간의 합의 최솟값을 구해야한다
# 2. 각각 필요한 시간들을 먼저 입력받은 다음 오름차순으로 정렬한다
# 3. 그런다음 각자가 기다리는 시간들을 리스트에 넣고 for문으로 더해준다

N = int(input())  # 사람의 수
P = list(map(int, input().split()))  # 돈을 인출하는데 걸리는 시간
time = []  # 각자 기다리는 시간을 담을 공간
t_sum = 0  # 시간들을 계속 누적해서 쌓기 위한 변수
# print(P)

P.sort()  # 오름차순 정렬 1, 2, 3, 3, 4로
# print(P)

for i in range(len(P)):
    t_sum += P[i]
    time.append(t_sum)

# print(time)

result = 0  # 총합을 담을 결과값
for j in time:
    result += j

print(result)
