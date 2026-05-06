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


def prevDate(d,m,y):
    if d < 1 or d > year(m,y):
        return f"there is no date like {d}/{m}/{y}"
    if d > 1:
        d -= 1
    else:
        if m == 1:
            y -= 1
            m = 12
            d = 31
        else:
            m -= 1
            d = year(m, y)

    return f"{d}/{m}/{y}"
print(prevDate(-1,1,2026))



