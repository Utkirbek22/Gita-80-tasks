m,n = map(int, input("Enter row and columns: ").split())
matrix = []
for i in range(m):
    row = list(map(int, input("Enter the number: ").split()))
    matrix.append(row)
for i in range(m):
    print(*matrix[i])

last_row = []
for i in range(n):
    max_value =  matrix[0][i]
    for j in range(m):
        if matrix[j][i] > max_value:
            max_value = matrix[j][i]
    last_row.append(max_value)

print(*last_row)

