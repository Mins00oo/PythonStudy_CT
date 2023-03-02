# a는 줘야하는 병의 개수, b는 받는 개수, n은 처음 보유한 개수
def solution(a, b, n):
    answer = 0
    while n >= a:
        if n % a == 0:
            answer += (n // a) * b
            n = (n // a) * b
        else:
            answer += (n // a) * b
            n = ((n - (n % a)) // a) * b + (n % a)
    return answer


print(solution(2, 1, 20))
