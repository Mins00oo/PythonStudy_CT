# 학생 수
n = int(input())
student = []
iq = []
for _ in range(n):
    a, b = map(str, input().split())
    student.append([a, b])

student.sort(key=lambda s: -int(s[1]))

print(student[0][0])
print(student[1][0])
print(student[2][0])
