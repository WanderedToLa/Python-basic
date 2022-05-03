#6091 함께 문제 푸는날
# a , b , c = map(int , input().split())
# d = 1

# while d%a!= 0 or d%b!=0 or d%c!=0:
#     d = d + 1
# print(d)

#6092 출석번호 부르기 1
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(24):
    d.append(0)

print(d)