d = [] # 크기가 19 * 19인 바둑판 생성
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19) : #바둑판 입력 받기
    a = input().split()
    for j in range(19) :
        d[i+1][j+1] = int(a[j])

n = int(input()) #뒤집을 횟수

for i in range(n):
    x , y = map(int , input().split()) # 좌표 n 번만큼 반복
    for j in range(1 , 20):
        if d[j][int(y)] == 0: # 1부터 커지면서 0인지를 비교함
            d[j][int(y)] = 1
        else:
            d[j][int(y)] = 0

        if d[int(x)][j] == 0:
            d[int(x)][j] = 1
        else:
            d[int(x)][j] = 0
for i in range(1, 20) : # 바둑판 출력
    for j in range(1, 20) : 
        print(d[i][j], end=' ')
    print()