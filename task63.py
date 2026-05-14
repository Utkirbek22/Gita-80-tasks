s = "abxy6878c"
prev = ""
found = False

for i in s:
    if i.isalpha():
        if prev != "" and i < prev:
            print(i)
            found = True
        prev = i
if not found:
    print(0)
