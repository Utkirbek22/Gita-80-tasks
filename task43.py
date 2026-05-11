num = [2,3,1,1,2,2,2,2,2]
b = []
c = []
count = 1
for i in range(1,len(num)):
    if num[i] == num[i - 1]:
        count += 1
    else:
        b.append(count)
        c.append(num[i - 1])
        count = 1
b.append(count)
c.append(num[-1])
print(b)
print(c)