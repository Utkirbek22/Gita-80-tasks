def ekub(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

print(ekub(24, 18))