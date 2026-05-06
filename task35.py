num = [10,20,30]

left = 0
right = len(num) - 1

while left <= right:
    print(num[left], end=" ")
    if left + 1 <= right:
        print(num[left + 1],end=" ")
    if left != right:
        print(num[right],end=" ")
    if right - 1 > left + 1:
        print(num[right - 1], end="")
    left += 2
    right -= 2