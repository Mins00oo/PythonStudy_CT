"""수도코드
1. combinations를 통해 조합을 가져오고 중복제거를 한 다음 정렬하여 반복문을 돌린다
2. 출력을 할 때는 *을 포함하여 출력한다.
"""

from itertools import combinations

n, m = map(int, input().split())
num = [i for i in range(1, n + 1)]
for i in sorted(set(combinations(num, m))):
    print(*i)
