num = [4,6,2,1,7]

for i in range(1,len(num)):
    current = num[i]
    j = i - 1
    while j >= 0 and num[j] > current:
        num[j + 1] = num[j]
        j -= 1


    num[j + 1] = current

print(num)