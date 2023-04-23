"""수도코드
1. 이름과 점수를 입력받기 때문에 이를 합쳐서 각각 맞게 새로운 2차원 배열을 만들어준다. -> zip 함수를 이용
2. photo 2차원 배열을 탐색하며 하나하나 값을 꺼내가며 새로운 2차원 배열의 값과 일치하면 cnt를 증가시켜 최종적으로 answer에 추가
"""


def solution(name, yearning, photo):
    answer = []
    c = [[a_elem, b_elem] for a_elem, b_elem in zip(name, yearning)]
    for i in range(len(photo)):
        cnt = 0
        for j in photo[i]:
            for k in c:
                if j == k[0]:
                    cnt += k[1]
        answer.append(cnt)
    return answer
