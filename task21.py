nums = [4,3,7,6,2,8]
max_sum = nums[0] + nums[1]


for i in range(len(nums) - 1):
    current_sum = nums[i] + nums[i + 1]
    if max_sum < current_sum:
        max_sum = current_sum

print(max_sum)