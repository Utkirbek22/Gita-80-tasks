nums = [4,5,6,3,5,4,43,2,4,43,23,41,]

min_value = nums[0]
min_index = 0

max_value = nums[0]
max_index = 0

for i in range(len(nums)):
    if nums[i] <= min_value :
        min_value = nums[i]
        min_index = i
    if nums[i] >= max_value:
        max_value = nums[i]
        max_index = i

if min_index < max_index:
    print(min_value, min_index)
else:
    print(max_value,max_index)

