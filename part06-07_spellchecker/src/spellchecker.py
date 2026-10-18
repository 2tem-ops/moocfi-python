text = input("Write text: ")
final = text.split()
check = text.lower().split()

lst = []

with open("wordlist.txt") as file:
    for line in file:
        line = line.replace("\n", "").split()
        for i in line:
            lst.append(i)
        
lst = set(lst)
res = []
indices = []

for word in check:
    if word not in lst:
        res.append("*" + word + "*")
        indices.append(check.index(word))
        continue
    res.append(word)
    
for index in indices:
    final[index] = res[index]

print(" ".join(final))
