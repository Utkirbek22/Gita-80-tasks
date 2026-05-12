m,n = map(int,input("Enter row and column nums: ").split())
matrix = []

for i in range(m):
    row = list(map(int, input("Enter numbers: ").split()))
    matrix.append(row)
min_value = matrix[0][0]
min_row = 0
min_col = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_row = i
            min_col = j
print(min_value, min_row, min_col)