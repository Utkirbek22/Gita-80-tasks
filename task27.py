def ekub(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a


def ekuk (a,b):
    res = ekub(24,18)
    ekuk_res = a * b // res
    return ekuk_res

print(ekuk(24,18))

