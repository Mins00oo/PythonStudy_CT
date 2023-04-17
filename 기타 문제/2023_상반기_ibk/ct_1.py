"""수도코드
1. [h,i, ,b,y,e, , , , ,   ,  , h, i,  , b, y, e
2. [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18
3. 0~5 / 12~17 / 24~29  -> 문구가 나오는 인덱스
4. 6~11 / 18~23 / 30~35 -> 문구가 나오지 않는 인덱스
"""


def get_display_text(t, n, sec):
    # 1. 길이 n인 공백 문자열을 초기화한다.
    a = []
    res = []
    answer = ""
    cnt = 0
    for _ in t:
        a.append(_)
    for i in range(sec):
        if i >= n:
            index = i - (sec % (len(t) + n + n))
            if 0 <= index < len(t):
                res.append(a[i])
            else:
                res.append(" ")
        else:
            res.append(a[i])
            cnt += 1
    print(res)
    if len(res) < n:
        answer = ''.join(res)
        answer = answer.rjust(6, " ")
        answer = answer.replace(" ", "_")
    elif len(res) == n:
        answer = "".join(res)
        answer = answer.replace(" ", "_")

    return answer


# 예시 사용
text = "hi bye"
n = 6
second = 3
print(get_display_text(text, n, second))
