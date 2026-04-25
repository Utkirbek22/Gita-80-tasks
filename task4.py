month_days = {
    1: 31,  # January
    2: 28,  # February (non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

day = 31
month = 3
max_day = month_days[month]

if month in month_days:
    if day == max_day and month == 12:
        day = 1
        month = 1
        print(f"today is {day}.{month}")
    elif day == max_day:
        month += 1
        day = 1
        print(f"today is {day}.{month}")
    elif month == max_day:
        month += 1
        day = 1
        print(f"today is {day}.{month}")
    elif day < max_day:
        day += 1
        print(f"today is {day}.{month}")
    else:
        print(f"{day} is out of range")
else:
    print("out of range")



























# month = 8
# January = 1
# February = 2
# March = 3
# April = 3
# December = 12
# year = 2025
# day = 21
#
# if month == 12 and day == 31:
#     year += 1
#     month = 1
#     day = 1
#     print(f"0{day}.0{month}.{year}")
#
# elif month < 12 and day == 31:
#     day += 1
#     month += 1
#     print(f"0{day}. 0{month}")
# elif day != 31:
#     day += 1
#     print(f"0{day}. 0{month}")


#
# month_days = {
#     1: 31,  # January
#     2: 28,  # February (non-leap year)
#     3: 31,  # March
#     4: 30,  # April
#     5: 31,  # May
#     6: 30,  # June
#     7: 31,  # July
#     8: 31,  # August
#     9: 30,  # September
#     10: 31, # October
#     11: 30, # November
#     12: 31  # December
# }
# month = 11
# day = 23
# max_days = month_days[month]
#
# if month in month_days:
#     if month == 12 and day == max_days:
#         day = 1
#         month = 1
#         print(f"next day is {day}.{month}")
#     elif day < max_days:
#         day += 1
#         print(f"next day is {day}.{month}")
#     elif day == max_days:
#         day = 1
#         month += 1
#         print(f"next day is {day}.{month}")
#     else:
#         print(f"{day} is out of range")
# else:
#     print(f"{day}.{month} is out of range")
#
# print(f"0{day}.0{ month} is correct")

# if month in month_days:
#     max_days = month_days[month]
#     if day == max_days and month == 12:
#         day = 1
#         month = 1
#         print(f"next day is {day}.{month}")
#     elif day < max_days:
#         day += 1
#         print(f"next day is {day}.{ month}")
#
#     elif day == max_days:
#         day = 1
#         month += 1
#         print(f"next day and month is 0{day}.0{ month}")
#
#     else:
#         print(f"{day} is out of range days")
#
# else:
#     print(f"{month} that is wrong")