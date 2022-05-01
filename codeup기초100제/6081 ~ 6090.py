#6081 16진수 구구단
a = int(input() , 16)

for i in range( 1 , 16 ):
    print('%X*%X=%X' %(a,i,a*i))

#6082 3 6 9 game
a = int(input())

for i in range( 1 , a + 1):
    if i % 10 == 3:
        print('X')
    elif i % 10 == 6:
        print('X')
    elif i % 10 == 9:
        print('X')
    else :
        print(i)

#6083 rgb 경우의 수
r,g,b = map(int , input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i ,j, k ,sep=' ')

print(r*g*b)

#6084 소리파일 저장용량 계산하기
h , b , c , s = map(int , input().split())
n = h * b * c * s / 8 / 1024 / 1024
print(format(n , '0.1f'),'MB')

#6085 그림파일 용량 계산
w , h , b = map(int , input().split())
n = w * h * b / 8 / 1024 / 1024
print(format(n , '.2f') , 'MB')

#6086 거기까지!
n = int(input())
result = 0
b = 0

while True:
    result = result + b
    b = b + 1
    if result >= n:
        break
print(result)

#6087 3의 배수 통과
n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i , end =' ')


#6088 등차 수열
a , b , c = map(int , input().split())

for i in range(1 , c):
    a = a + b
print(a)

#6089 등비 수열
a , b , c = map(int , input().split())

for i in range(1 , c):
    a = a * b
print(a)

#6090 수열 복합
a , m , d , n = map(int , input().split())

for i in range(1 , n):
    a = a * m + d
print(a)