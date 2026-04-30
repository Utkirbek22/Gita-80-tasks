def digit(num):
    count = 0
    while  num != 0:
        num = num // 10
        count += 1
    return count

result = digit(2344)

print(result)
