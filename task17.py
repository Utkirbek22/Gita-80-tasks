nums = [-9,-1,-4]
min_num = None


for i in nums:
    if i > 0:
        if min_num is None or i < min_num:
            min_num = i

if min_num is None:
    print(0)
else:
    print(min_num)






