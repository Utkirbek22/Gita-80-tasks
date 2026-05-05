
def isPalindrom(num):
    num = str(num)
    left = 0
    right = len(num) - 1
    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
    return True

one = [1,2,3,2,1]
sec = [1,3,1]
third = [5,4,3,2,5]

all_list = [one,sec,third]
print(all_list)

count = 0

for x in all_list:
    num_str =  "".join(str(i) for i in x)
    if isPalindrom(num_str):
        count += 1
print(count)



# for i in one:
#     results += str(i)
# print(results)
