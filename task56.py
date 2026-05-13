s = "Assalomu alaykum aziz do'stlar"
word = s.split()
print(word)
min_value = word[0]
for i in range(1,len(word)):
    if len(word[i]) < len(min_value):
        min_value = word[i]

print(min_value, len(min_value))
