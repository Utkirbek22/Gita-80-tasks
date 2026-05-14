def rem(num, d):
    for i in num:
        if i == d:
            num.remove(i)
    return num
num = list(map(int, input("Enter the number: ").split()))
print(*rem(num,2))

