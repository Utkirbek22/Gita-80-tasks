# m,n = map(int,input("Enter number: ").split())
m = 3
n = 3
num = 1
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(num)
        num += 1
    matrix.append(row)

for i in range(m):
    total = 0
    for j in range(n):
        total += matrix[i][j]
    if total == 15:
        print(matrix[i])
