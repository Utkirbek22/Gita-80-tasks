def rev(nums):
    return nums[::-1]

nums = list(map(int, input("Enter numbers: ").split()))

print(*rev(nums))