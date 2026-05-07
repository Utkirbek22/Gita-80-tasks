import random

m = 10
n = 4
res = []
if m < n:
    print("impossible")
else:
    while len(res) < n:
        num = random.randint(1, m)
        if num not in res:
            res.append(num)

print(res)