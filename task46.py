# m, n = map(int, input("Enter your number: ").split())
m = 4
n = 3
num = 1
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(num)
        num += 1
    matrix.append(row)
count = 0
for i in range(len(matrix)):
    total = 0
    for j in range(n):
        total += matrix[i][j]
    print(*matrix[i], "=>", total)

