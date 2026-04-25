num = 1200
if num % 4 == 0:
    if num % 100 == 0 and num % 400 == 0:
        print(f"{num} is cabise year")
    else:
        print("say smth")
else:
    print(f"{num} is not cabise year, sorry")