# m, n = map(int, input("Enter your number: ").split())
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
    print(*matrix[i])

for j in range(n):
    total = 1
    for i in range(m):
        total *= matrix[i][j]
    print(total, end=" ")