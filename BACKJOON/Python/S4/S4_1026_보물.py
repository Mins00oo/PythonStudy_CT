n = int(input())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

# a 리스트의 최소 * b 리스트의 최대 연산 후 리스트에서 요소 제거하고 반복문
# 요소 제거는 pop
s = 0
for i in range(n):
    s += min(a_li) * max(b_li)
    a_li.pop(a_li.index(min(a_li)))  # a 리스트에서 최솟값 제거
    b_li.pop(b_li.index(max(b_li)))  # b 리스트에서 최댓값 제거

print(s)
