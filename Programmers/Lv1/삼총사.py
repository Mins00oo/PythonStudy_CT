import itertools


def solution(number):
    # combination을 사용해 리스트에서 3개를 뽑는 경우를 가져오고
    number_com = itertools.combinations(number, 3)
    # 반복문을 돌리면서
    answer = sum([1 if sum(num) == 0 else 0 for num in number_com])
    return answer
