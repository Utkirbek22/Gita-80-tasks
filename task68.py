def add(nums, n):
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == n:
            nums.insert(i + 1, nums[i])
    return nums

nums = list(map(int,input("Enter number: ").split()))
print(add(nums,1))
