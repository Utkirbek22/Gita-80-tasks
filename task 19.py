nums = [2,13,9,4,7,2,5,3,5,19,26,7,6,11,4]
max_value = nums[0]
index = 0
count = 0
for i in range(len(nums)):
    if nums[i] >= max_value:
        max_value = nums[i]
        index = i
left_elements = len(nums) - index - 1

print(max_value, index, left_elements)