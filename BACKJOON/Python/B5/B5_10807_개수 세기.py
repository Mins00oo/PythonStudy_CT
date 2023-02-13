# n개의 정수가 주어질 때, v가 몇개인지 구하는 프로그램
n = int(input())
n_list = list(map(int, input().split()))
# 찾아야 하는 정수 v
v = int(input())
print(n_list.count(v))
