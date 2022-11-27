pixels = [[1,0,1], [0,0,1], [1,1,0]]
n = 3
m = 3

ans = 0
rows = []
cols = []

print("hi")

for i in range(n):
    rows = pixels[i]
    cols = []
    for j in range(m):
        cols.append(pixels[i][j])

    print(rows)
    print(cols)
    print()

