#6061 비트연산 vertical bar / or 연산 -> 1이 하나라도 있으면 1로변환
#a , b = map(int , input().split())
#print(a | b)

#6062 비트연산 xor ^ 서로 다른부분만 처리가능
#a , b = map(int , input().split())
#print(a ^ b)

#6063 3항 연산
#a , b = map(int , input().split())
#c = (a if (a >= b) else b)
#print(c)

#6064 3항연산2 작은 수 구하기
#n , m , k = map(int , input().split())
#i = (n if (n < m) else m) if ((n if n < m else m)<k) else k
#print(i)

#6065 짝수만 출력
# a , b , c = map(int , input().split())
# if a%2 == 0:
#     print(a)
# if b %2 == 0:
#     print(b)
# if c %2 == 0:
#     print(c)

#6066 홀 짝 출력하기
# a , b , c = map(int , input().split())

# if a % 2 == 0:
#     print('even')
# else:
#     print('odd')

# if b % 2 == 0:
#     print('even')
# else:
#     print('odd')

# if c % 2 == 0:
#     print('even')
# else:
#     print('odd')

#6067 음 양 구분하여 짝 , 홀 출력하기
# a = int(input())
# if a < 0:
#     if a % 2 == 0:
#         print('A')
#     else :
#         print('B')
# elif a > 0 :
#     if a % 2 == 0:
#         print('C')
#     else : 
#         print('D')

#6068 점수 입력받아 평가 출력하기
# a = int(input())

# if 90 <= a <=100 :
#     print('A')
# elif 70 <= a <= 89:
#     print('B')
# elif 40 <= a <= 69:
#     print('C')
# else :
#     print('D')

#6069 문자 입력받고 평가 출력
# a = input()
# if a=='A':
#     print("best!!!") 
# elif a=='B': 
#     print("good!!") 
# elif a=='C':
#     print("run!") 
# elif a=='D': 
#     print("slowly~") 
# else: 
#     print("what?")

#6070 월 입력받고 계절 출력하기 12 1 2 / 3 4 5 / 6 7 8 / 9 10 11
a = int(input())

if a // 3 == 1:
    print('spring')
elif a // 3 == 2 :
    print('summer')
elif a // 3 == 3 :
    print('fall')
else : print('winter')