num = [3,2,5,7,8,4,3,1,9]
r = 5
min_diff = float("inf")
min_num = None

for i in num:
    current_diff  = abs(i - r)
    if current_diff < min_diff:
       min_diff = current_diff
       min_num = i

print(min_diff, min_num)

