s = "assalomu alaykum aziz do'stlar"

word = s.split()

for i in range(len(word)):
    word[i] = word[i].capitalize()
res = " ".join(word)
print(res)
