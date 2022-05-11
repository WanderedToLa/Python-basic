d = []
for i in range(10):
    d.append(list(map(int, input().split())))

x = 2
y = 2
while True:
    if d[x][y] == 1:
        d[x][y] = 9
    break

for i in range(10) :
    for j in range(10) : 
        print(d[i][j], end=' ')
    print()