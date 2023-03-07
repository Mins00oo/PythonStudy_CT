def solution(number, limit, power):
    answer = 0
    sum_divisor = []
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i == 1:
                count = 1
            elif j == i ** (1 / 2):
                count += 1
            elif i % j == 0:
                count += 2
        sum_divisor.append(count)
    for k in range(len(sum_divisor)):
        if sum_divisor[k] > limit:
            sum_divisor[k] = power
        answer += sum_divisor[k]
    return answer


print(solution(10, 3, 2))
