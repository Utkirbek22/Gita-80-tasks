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

print(matrix)
for i in range(m):
    if i % 2 == 0:
        print(*matrix[i])
    else:
        print(*matrix[i][::-1])