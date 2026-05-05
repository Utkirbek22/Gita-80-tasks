def ekub(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def ekub3(a,b,c):
    first = ekub(a,b)
    result = ekub(first,c)
    return result

print(ekub3(24,18,30))