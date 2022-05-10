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
                d[x][k] = 1
        elif b == 1:
            for m in range(l):
                d[m][y] = 1
            
for i in range(w):
    for j in range(h):
        print(d[i][j], end=' ')
    print()