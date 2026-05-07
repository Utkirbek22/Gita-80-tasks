nums = [1,3,2,4,2,1,9,1]

numbers = []
frequency = []

for i in nums:
    if i not in numbers:
        numbers.append(i)
        count = 0
        for j in nums:
            if i == j:
                count += 1
        frequency.append(count)
print(numbers)
print(frequency)