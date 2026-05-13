s = "Assalomu alaykum"

first = s.find(" ")
last = s.rfind(" ")
if last == first:
    print("there is nothing")
else:
    print(s[first+1:last])
