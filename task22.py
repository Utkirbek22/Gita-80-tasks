def prime_number(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

count = 0
nums = [10, 11, 12, 13, 14]
for j in nums:
    if prime_number(j):
        count += 1
print(count)
