#6051 비교연산
a , b = map(int , input().split())
print(a!=b)

#6052 불 연산
n = int(input())
print(bool(n))

#6053 참 거짓 바꾸기
a  = bool(int(input()))
print(not a)

#6054 and 연산 두개 다 트루면 트루 출력
a , b = input().split()
print(bool(int(a)) and bool(int(b)))

#6055 or 연산
a , b = input().split()
print(bool(int(a)) or bool(int(b)))

#6056 베타적 논리합 연산
a , b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or (not c) and d)

#6057
a , b = input().split()
c = bool(int(a))
d = bool(int(b))
print(c == d)

#6058
a , b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not(c or d))

#6059 비트단위 논리연산
a = input()
a = int(a)
print((~a))

#6060 비트연산 &
a , b = map(int , input().split())
print(a&b)