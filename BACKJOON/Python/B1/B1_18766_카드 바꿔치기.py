t = int(input())  # 테스트 케이스의 개수

for i in range(t):
    n = int(input())  # 카드 개수
    first_card = sorted(list(map(str, input().split())))
    last_card = sorted(list(map(str, input().split())))
    if first_card != last_card:
        print("CHEATER")
    else:
        print("NOT CHEATER")

