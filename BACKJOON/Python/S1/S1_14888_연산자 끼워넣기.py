"""수도코드
1. 입력받기: n, 수열, 연산자의 수
2. 연산자를 횟수에 맞춰서 저장해준다.
2.1 이 문제는 연산자의 모든 경우에 따라서 값을 계속해서 바꿔주면 되므로 우선 연산자를 저장한다. [+, -, -, *] 이런식으로
3. 저장한 연산자의 경우의 수를 돌리기 위해 permutation을 사용해서 꺼내오고 각 연산자를 반복해서 solution함수에 넣어준다
4. 함수 정의
4.1 첫 값은 arr의 맨 앞의 값이고 연산자에 따라서 값을 계속 바꿔주면 된다,
4.2 그런 다음 반복문이 끝나면 리턴한다.
4.3 나누기 하는 과정에서 음수가 나온다면 양수로 바꿔주고 결과값을 음수로 바꾼다.
5. 최댓값 최솟값을 구하기 위해 result를 계속 저장할 리스트를 하나 만들어서 함수안에서 return 되기 전에 넣어준다,
"""
from itertools import permutations


def solution(operation):
    global result_list, max_result, min_result
    result = arr[0]
    for i, op in enumerate(operation):
        if op == '+':
            result += arr[i + 1]
        elif op == '-':
            result -= arr[i + 1]
        elif op == '*':
            result *= arr[i + 1]
        else:
            if result < 0:
                result = -(-result // arr[i + 1])
            else:
                result //= arr[i + 1]
    max_result = max(max_result, result)
    min_result = min(min_result, result)


n = int(input())
arr = list(map(int, input().split()))
operators = []
operators_count = list(map(int, input().split()))

max_result = -1000000000
min_result = 1000000000
result_list = []

for i, count in enumerate(operators_count):
    operators.extend(['+', '-', '*', '/'][i] * count)

for operators_set in permutations(operators):
    solution(operators_set)

print(max_result)
print(min_result)
