num = [1,2,3,4,5]

left = 0
right = len(num) - 1

while left <= right:
    if left == right:
        print(num[left],end=" ")
    else:
        print(num[left], num[right], end=" ")
    left += 1
    right -= 1