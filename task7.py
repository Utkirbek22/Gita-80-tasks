num = 10000
for i in range(1,num + 1):
    total = 0
    for j in range(1, i):
        if i % j == 0:
            total += j
    total_sum = 0

    for k in range(1, total):
        if total % k == 0:
            total_sum += k
    if total_sum == i and total != i and i < total:
        print(f"{i} {total}")












# num = 19
#
# for i in range(1,num +1):
#     total = 0
#     if num % i == 0:
#         total += i
#     print(total)