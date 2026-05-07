from dnf.util import empty

num = [1,3,2,4,6,5,9,1]

res = []

for i in range(1,len(num) -1):
    if num[i] > num[i - 1] and num[i] > num[i + 1]:
        res.append(num[i])
if res:
    print(min(res))
print(res)

print(bool([]))
print(bool([1]))
