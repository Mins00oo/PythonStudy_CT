num = list(map(int, input().split()))

if num == [1, 2, 3, 4, 5, 6, 7, 8]:  # 1~8까지 순서대로일때 
    print('ascending')
elif num == [8, 7, 6, 5, 4, 3, 2, 1]:  # 8 - 1로 순서대로일때
    print('descending')
else:  # 둘 다 아닐때
    print('mixed')
