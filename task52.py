m,n = map(int, input("Enter col and column: ").split())
matrix = []

for i in range(m):
    row = list(map(int, input("Enter number: ").split()))
    matrix.append(row)
min_value = matrix[0][0]
row = 0
col = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            row = i
            col = j


for i in range(m):
    matrix[i].pop(col)

for i in range(m):
    print(*matrix[i])

