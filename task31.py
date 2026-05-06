month_days = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

def leapYear(a):
    if a % 4 == 0 and a % 100 != 0 or  a % 400 == 0:
        return True
    return False

def year(month,year):
    if month == 2:
        if leapYear(year):
            return 29
        else:
            return 28
    else:
        return  month_days[month]


month = [2,12,11]
res = []
for i in month:
    k = (year(i,2026))
    res.append(k)

for i in res:
    " ".join(str(i))
    print(i, end=" ")
# print(" ".join(str(i) for i in res))