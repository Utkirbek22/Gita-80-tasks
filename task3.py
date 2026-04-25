x = 6
y = 8
temp_x = x
temp_y = y
if x < y:
    x = (temp_x + temp_y) // 2
    y =  (temp_x * temp_y) * 2
    print(x, y)
elif y > x:
    y = (temp_x + temp_y) // 2
    x = (temp_x * temp_y) * 2
    print(x, y)
else:
    x = x
    y = y
    print(x, y)
