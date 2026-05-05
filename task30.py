def leapYear(a):
    if a % 4 == 0 and a % 100 != 0 or  a % 400 == 0:
        return True
    return False

years = [1300,2020,1900]
count = 0

for i in years:
    if leapYear(i):
        count += 1

print(count)