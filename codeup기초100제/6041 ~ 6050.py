#6041 나머지 계산
a , b = input().split()
a = int(a)
b = int(b)
c = a%b
print(c)

#6042 실수 입력받고 소수점 자리에서 반올림
a = input()
a = float(a)
print(format(a , '.2f'))

#6043 실수 두개 입력받고 나눈 값 출력
a , b = input().split()
a = float(a)
b = float(b)
c = a/b
print(format(c , '.3f'))

#6044 합 차 곱 몫 나머지 나눈 값
a , b = input().split()
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a/b , '.2f'))

#6045 정수 3개의 합과 평균 구하기
a , b , c = map(int , input().split())
d = a + b + c
e = d/3
print(d , format(e , '.2f'))

#6046 비트시프트 연산
a = input()
a = int(a)
print(a<<1)

# 6047 시프트연산2
a , b = map(int , input().split())
print(a << b)

#6048 비교연산 왼쪽이 더 작으면 트루
a , b = map(int , input().split())
print(a<b)
print(a>=b)

#6049 비교 연산 두 숫자가 같으면 트루 아니면 폴스
a , b = map(int , input().split())
print(a == b)

#6050 비교연산
a , b = map(int , input().split())
print(a<=b)