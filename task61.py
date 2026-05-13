s = r"D:\Qudrat_Abdurahimov\books\java_book.exe"

word = s.split("\\")

if len(word) > 2:
    print(word[-2])
else:
    print("\\")