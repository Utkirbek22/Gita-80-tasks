def minValue(nums):
    minV = nums[0]
    for i in nums:
        if i < minV:
            minV = i
    return minV

nums = list(map(int, input("Enter numbers: ").split()))

print(minValue(nums))


