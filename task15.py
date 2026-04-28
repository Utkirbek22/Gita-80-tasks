nums = [8,2,3,53,4,4,5,5,24,53,34,2]
max_value = nums[0]
max_index = 0

min_value = nums[0]
min_index = 0
for i in range(len(nums)):
    if nums[i] > max_value:
        max_value = nums[i]
        max_index = i
    if nums[i] < min_value:
        min_value = nums[i]
        min_index = i
if min_value < max_value:
    print(min_value,min_index)
else:
    print(max_value,max_index)



# print(max_value, max_index)
# print(min_value,min_index,)
