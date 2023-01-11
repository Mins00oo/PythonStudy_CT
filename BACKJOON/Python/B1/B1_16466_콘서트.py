n = int(input())  # 1차에서 팔린 티켓들의 수
nums = sorted(list(map(int, input().split())))
isSame = True
for i in range(n):
    if (i + 1) != nums[i]:
        print(i + 1)
        isSame = False
        break
if isSame:  # 숫자가 같을 경우 ex) 번호가 5개인데 1 2 3 4 5일때 for문에서도 1 2 3 4 5 순으로 같기 때문에
    print(n + 1)
