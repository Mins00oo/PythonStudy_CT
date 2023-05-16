def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    l_list = [1, 4, 7]
    left_start = dic['*']
    right_start = dic['#']
    r_list = [3, 6, 9]
    for i in numbers:
        # now는 눌러야 하는 번호의 좌표값
        now = dic[i]
        if i in l_list:
            answer += 'L'
            left_start = now
        elif i in r_list:
            answer += 'R'
            right_start = now
        else:
            left_d = 0
            right_d = 0
            for a, b, c in zip(left_start, right_start, now):
                left_d += abs(a - c)
                right_d += abs(b - c)
            if left_d < right_d:
                answer += "L"
                left_start = now
            elif left_d > right_d:
                answer += "R"
                right_start = now
            else:
                if hand == "left":
                    answer += "L"
                    left_start = now
                else:
                    answer += "R"
                    right_start = now
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
