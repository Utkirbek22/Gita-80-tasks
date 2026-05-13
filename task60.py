s = r"D:\java_book.exe"

word = s.split("\\")

if len(word) > 2:
    print(word[1])
else:
    print("\\")