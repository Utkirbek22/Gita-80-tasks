nums = [8, 9, 1, 2]
pairs = []

for i,value in enumerate(nums):
    pairs.append((value,i))

for i in range(len(nums)):
    for j in range(len(nums) -1):
        if pairs[j][0] > pairs[j + 1][0]:
            pairs[j], pairs[j + 1] = pairs[j + 1],pairs[j]
print(pairs)