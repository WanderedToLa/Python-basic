d = []
for i in range(10):
    d.append(list(map(int, input().split())))

x = 1
y = 1
d[x][y] = 9
while True:
    if d[x][y] == 2: #먹이를 찾았을 경우 반복문 중지
        d[x][y] = 9
        break
    if d[x][y + 1]!=1: #아래로 이동하는 경우 y + 1
        d[x][y] = 9
        y += 1
    elif d[x + 1][y] != 1: # 오른쪽으로 이동하는 경우 x + 1
        d[x][y] = 9
        x += 1
    else:
        d[x][y] = 9
        break

for i in range(10) :
    for j in range(10) : 
        print(d[i][j], end=' ')
    print()