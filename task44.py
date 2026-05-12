n, m = map(int, input("Enter row number and column number: ").split())
matrix = []
for i in range(m):
    row = list(map(int, input("Enter number: ").split()))
    matrix.append(row)
found = False
for i in range(m):
    pos = 0
    neg = 0
    for j in range(n):
        if matrix[i][j] > 0:
            pos += 1
        elif matrix[i][j] < 0:
            neg += 1
    if neg == pos:
        print(i)
        found = True
        break
if not found:
    print("there is no element")