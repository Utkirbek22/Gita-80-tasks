# def digitnum(num, k):
#     num = str(num)
#     if len(num) < k:
#         return -1
#     for i in range(len(num)):
#         if i == k - 1:
#             return int(num[i])
#
#
# result = digitnum(98765, 1)
# print(result)


def digitnum(num, k):
    num = str(num)
    if len(num) < k -1:
        return -1
    return int(num[k])  # what index goes here?
result = digitnum(98765, 9)
print(result)
