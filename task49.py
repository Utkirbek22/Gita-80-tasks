m,n = map(int, input("Enter numbers rows and columns: ").split())
matrix = []

for i in range(m):
    row = list(map(int, input("Enter number: ").split()))
    matrix.append(row)


for i in range(m):
    max_value = matrix[i][0]
    print(max_value)
    for j in range(n):
        if matrix[i][j] > max_value:
           max_value = matrix[i][j]
    matrix[i].append(max_value)
    print(*matrix[i])
