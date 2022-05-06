#6091 함께 문제 푸는날
# a , b , c = map(int , input().split())
# d = 1

# while d%a!= 0 or d%b!=0 or d%c!=0: #1부터 입력된값으로 나눔
#     d = d + 1
# print(d) #세가지 경우 전부 0일 때 값 출력 -> 최소 공배수

#6092 출석번호 부르기 1
# n = int(input())
# a = input().split() # 무작위로 부르는 값

# for i in range(n): #출석을 부르는 횟수 만큼 반복
#     a[i] = int(a[i]) # a에 입력된 값을 순서대로 정수형으로 저장
# d = []
# for i in range(24):
#     d.append(0)
# for i in range(n):
#     d[a[i]] += 1 #번호를 부를때마다 카운트 1씩 증가
# for i in range(1 , 24):
#     print(d[i] , end=' ')

#6093 출석번호 부르기2
# n = int(input())
# a = input().split()

# for i in range(n -1 , -1 , -1):
#     print(a[i] , end=' ')

#6094 출석번호 부르기3
# n = int(input())
# a = list(map(int , input().split())) # 리스트로 저장
# result = 0

# for i in a:
#     if result == 0 or i < result :
#         result = i
# print(result)