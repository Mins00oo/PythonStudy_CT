"""수도코드
1. 입력값 받기: 특정 n번째 피보나치 수
2. n이 0이라면 피보나치 수열의 맨 앞인 0을 출력하고 그 외에는 값을 하나씩 저장해나가며 수열을 생성한다.
3. 수열이 생성되었다면 n번째 인덱스 값을 가져오도록 한다.
"""

n = int(input())
if n == 0:
    print(0)
else:
    arr = [0] * (n + 1)
    arr[0] = 0
    arr[1] = 1

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    print(arr[n])