def solution(s, skip, index):
    answer = ''
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in skip:
        alpha_list.remove(i)
    for i in s:
        now = alpha_list.index(i)
        d = now + index
        length = len(alpha_list)
        if d >= length:
            dn = (now + index) - length
            answer += alpha_list[dn]
        else:
            answer += alpha_list[d]

    return answer


print(solution("aukks", "wbqd", 5))
