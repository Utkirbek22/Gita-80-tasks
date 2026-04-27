nums = [1,2,3,4,4,5,5,24,53,2,34]
max_value = nums[0]
max_index = 0
for i in range(len(nums)):
    if nums[i] > max_value:
        max_value = nums[i]
        max_index = i



print(max_value, max_index)

