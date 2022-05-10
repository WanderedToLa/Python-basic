w , h = map(int , input().split())
d = []
n = int(input())

for i in range(w):
    d.append([])
    for j in range(h):
        d[i].append(0)

for i in range(n):
    l , b , x , y = map(int , input().split())
    for j in range(l):
        if b == 0:
            for k in range(l):
                d[x -1][y - 1 + k] = 1 # + k와 m은 좌표를 한칸씩 당기고 반복문만큼 길이를 증가시킴
        elif b == 1:
            for m in range(l):
                d[x - 1 + m][y - 1] = 1
            
for i in range(w):
    for j in range(h):
        print(d[i][j], end=' ')
    print()