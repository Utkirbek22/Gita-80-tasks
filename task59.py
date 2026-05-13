s = "\Qudrat_Abdurahimov\Books\My_book.exe"

word = s.split("\\")

print(word)

fileName = word[-1]
res = fileName.split(".")
print(res[0])