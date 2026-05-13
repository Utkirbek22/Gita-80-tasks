from os.path import split

s = r"D:\flag.png"

word = s.split("\\")

res = word[-1].split(".")
print(res[-1])
