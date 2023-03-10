from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for word in goal:
        if word in cards1:
            if word == cards1[0]:
                cards1.popleft()
            else:
                return 'No'
        elif word in cards2:
            if word == cards2[0]:
                cards2.popleft()
            else:
                return 'No'
        else:
            return 'No'

    return 'Yes'


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
