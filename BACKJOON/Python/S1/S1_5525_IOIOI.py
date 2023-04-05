"""수도코드
1. 정수 n, 문자열 s의 길이 m, 문자열 s를 각 줄에 입력받는다.
2. 예를 들어 n = 1이면 n_length는 3 for문은 0부터 10까지
2.1 n = 2 이면 length는 5 for문은 0부터 8까지
2.2 n = 3이면 length는 7 for문은 0부터 6까지
3. 0부터 2, 1부터 3, 2부터 4 이런식으로 n_length만큼 일정하게 반복하는데 찾고자하는 문자열이 있는지 확인
4. 문자열은 n = 1일때는 IOI, n = 2일때는 IOIOI, n = 3일때는 IOIOIOI
"""

"""50점
n = int(input())
m = int(input())
s = input()
n_length = (2 * n) + 1
t_str = 'IOI' + (n - 1) * 'OI'
cnt = 0
for i in range(m - 2 * n):
    temp = ''
    for j in range(i, i + n_length):
        temp += s[j]
    if temp == t_str:
        cnt += 1

print(cnt)
"""

"""다른 코드
1. for문으로 하면 시간복잡도 때문에 50점만 되는거같다. 그래서 while문으로 변경
2. for문처럼 0번째 인덱스부터 12번째까지 탐색을 한다. 
3. 만약, 위치한 인덱스에서 예를 들어 0이라면 s[0:3] == 'IOI'라면 인덱스 값을 2만큼 증가시키고 cnt를 1 증가한다
3.1 IOIOI를 찾는다하면 0부터 2까지 IOI가 나오고 2부터 4까지 또 IOI가 나오기 때문에, 만약 IOIOIOI여도 마찬가지다.
3.2 그렇기에 2만큼 처음에 IOI가 나온다면 2씩 증가시켜서 또 IOI가 나오는지는 cnt로 확인해서 n하고 비교
3.3 cnt를 1 감소해줘야 그 다음에 또 IOI가 나온다면 맨 처음에 나온 IOI를 빼고 생각
4. cnt가 n과 일치해지면 result를 1 증가시키고 다시 cnt 감소
"""
n = int(input())
m = int(input())
s = input()
result, cnt, i = 0, 0, 0

while i < m - 1:
    if s[i:i + 3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(result)
