balanced = 0

for i in range(1000, 10000):
    n = i
    if "0" not in str(n):
        if int(str(n)[0]) + int(str(n)[-1]) == int(str(n)[1]) + int(str(n)[2]):
            middle = string[1] + string[2]
            if int(middle) % 6 == 0:
                balanced += 1

print(balanced)
print(1122)
            
