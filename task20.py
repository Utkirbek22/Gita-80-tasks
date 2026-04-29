nums = [4,3,5,8,12,54,32,12,4,2,65,23,7]
first_min = nums[0]
second_min = nums[1]

if first_min > second_min:
    first_min, second_min = second_min, first_min

for i in range(2, len(nums)):
    if nums[i] < first_min:
        second_min = first_min
        first_min = nums[i]
    elif first_min < nums[i] < second_min:
        second_min = nums[i]

print(first_min, second_min)