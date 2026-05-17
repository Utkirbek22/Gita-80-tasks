def sumRow(a,k):
    if k > len(a):
        return 0
    total = 0
    for i in a[k]:
        total += i
    return total
m,n = map(int,input("Enter numbers: ").split())
matrix = []
for i in range(m):
    row = list(map(int, input("enter number:").split()))
    matrix.append(row)
k = int(input("enter k: "))
print(sumRow(matrix,k))