def solution(food):
    answer = ''
    for i in range(1, len(food)):
        food[i] = food[i] // 2
    for j in range(1, len(food)):
        f = str(j)
        answer += (f * food[j])
    answer += '0'
    for k in range(len(food) - 1, 0, -1):
        f = str(k)
        answer += (f * food[k])
    return answer


print(solution([1, 7, 1, 2]))
