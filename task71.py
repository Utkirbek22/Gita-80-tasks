def sumColumn(a,k):
    if k > n:
        return 0

    total = 0
    for i in range(m):
        total += a[i][k]
    return total


m,n = map(int, input("enter row and col numbers: ").split())
matrix = []

for i in range(m):
    row = list(map(int, input("Enter matrix numbers: ").split()))
    matrix.append(row)

a = int(input("enter columns: "))

print(sumColumn(matrix,a))