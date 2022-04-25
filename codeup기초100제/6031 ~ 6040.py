#6031 정수입력받아 유니코드로 전환
a = int(input())
print(chr(a))

#6032 정수입력받고 등호 바꿔서 출력하기
a = int(input())
print(-a)

#6033 문자 입력받고 다음문자 출력하기 유니코드로 전환
b = ord(input())
print(chr(b + 1))

#6034 정수의 뺄셈 계산하기
a , b = input().split()
c = int(a) - int(b)
print(c)

#6035 실수 입력받아 곱셈 출력하기
a , b = map(float , input().split())
c = a * b
print(c)

#6036 정수곱하기 문자 출력
w , a = input().split()
print(w * int(a))

#6037
a = input()
w = input()
print(int(a) * w)

#6038 거듭제곱 출력하기
a , b = input().split()
a = int(a)
b = int(b)
c = a**b
print(c)

#6039 실수 2개 입력받고 거듭제곱 출력
a , b = input().split()
a = float(a)
b = float(b)
c = a**b
print(c)

#6040 몫 계산 6041 나머지 계산
a , b = input().split()
a = int(a)
b = int(b)
c = a//b
print(c)