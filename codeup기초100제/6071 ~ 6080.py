#6071 0 이 될때까지 무한 출력
n = 1
while n!=0:
    n = int(input())
    if n !=0:
        print(n)

#6072 카운트 다운
n = int(input())

while n !=0:
    print(n)
    n = n -1

#6073 0까지 카운트 다운
n = int(input())

while n !=0:
    print(n -1)
    n = n-1

#6074 문자 알파벳 출력
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

#6075 정수 입력받고 그 수까지 출력
a = int(input())
b = 0

while b <= a :
    print(b)
    b = b + 1

#6076 그 수 까지 출력2
a = int(input())
b = 0

for i in range(a + 1):
    print(b)
    b = b + 1

#6077 짝수의 합 구하기 1 2 3 4 5 6 7 8
a = int(input())
result = 0

for i in range(a+1):
    if i % 2 == 0:
        result += i

print(result)

#6078 q가 입력될때 까지 출력하기
w = 'a'

while w != 'q':
    w = input()
    if w != 'q':
        print(w)
    elif w == 'q':
        print(w)

#6079 언제까지 더할까? 
a = int(input())
b = 0
result = 0

while  b != a :
    b = b + 1
    result += b
    if result == a :
        print(b)
        break
    elif result >= a :
        print(b)
        break

#6080 주사위 두개 던지기
n , m = map(int , input().split())
for i in range (1 , n + 1):
    for j in range(1 , m + 1):
        print(i , j)