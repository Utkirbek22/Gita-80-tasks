def ekub(a,b):
    while b != 0:
        a, b = b,(a % b)
    return a
def ekub_many(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = ekub(result, num)
    return result

print(ekub_many([40,56,72,80,88]))
