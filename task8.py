number = 1000
percentage = 5
month = 0
new_number = number



while (2 * number) >= new_number:
    new_number += (new_number * percentage / 100)
    month += 1

print(month, new_number)