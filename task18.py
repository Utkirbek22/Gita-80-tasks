nums = [2,13,9,4,7,2,5,3,5,19,26,7,6,11,4]
first_value = None
first_index = 0


for i in range(len(nums)):
    if nums[i] % 2 != 0:
        if first_value is None or nums[i] > first_value:
            first_value = nums[i]
            first_index = i

if first_value is None:
    print(0)
else:
    print(first_value,first_index + 1)