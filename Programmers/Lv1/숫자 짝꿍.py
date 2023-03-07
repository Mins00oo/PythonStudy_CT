def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))
    # 처음에 answer이 비어있는지 확인을 한 다음, answer이 0으로 되어있는지 확인해야함
    # 조건절 순서가 바뀌게 되면 answer이 빈 문자열이어도 다른 조건문에 걸리게 됨
    if answer == '':
        return '-1'
    elif answer.count('0') == len(answer):
        return '0'
    else:
        return answer


print(solution("100", "2345"))
