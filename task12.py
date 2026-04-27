nums = [3,3,5,4,2,55,33,22,33,534,232,122]
min_num = nums[0]

for i in nums:
    if min_num > i:
        min_num = i

print(min_num)
